from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import inlineformset_factory, FileInput
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from mutagen.easyid3 import EasyID3
from mutagen import File
import mutagen
from audioEditing.merge import Merge
from audioEditing.remove import Crop
from audioEditing.tagging import Tagging
from .forms import (CreateUserForm,
                    LoginForm,
                    ShortAudioForm,
                    BaseCoverPictureSet,
                    AudioRangeForm,
                    AudioTagsForm,
                    UploadForm,
                    EditUserForm)
from .models import AudioModel, CoverPictureModel
# Create your views here.


def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        register = CreateUserForm(request.POST)
        if form.is_valid() is True:
            form.save()
            messages.add_message(request, messages.SUCCESS, 'registration successfully!')
            return redirect(to='index')
        messages.add_message(request, messages.ERROR, 'registration not successfully!')
    context = {
        "form": form
    }

    return render(request, "home/registration.html", context)


def login_view(request):
    """"""
    form = LoginForm()

    if request.user.is_authenticated:
        return redirect(to='dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() is True:
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'you are logged in successfully!')
                return redirect(to='dashboard')
        messages.add_message(request, messages.ERROR, 'Logged in failed!. Check your credential')
    context = {
        "form": form,
    }

    return render(request, "home/login.html", context)


@login_required
def profile_view(request):
    userObj = User.objects.get(username=request.user)
    data ={'username':userObj.username, 'email':userObj.email}
    form = EditUserForm(initial=data)
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            try:
                userObj.username = form.cleaned_data['username']
                userObj.email = form.cleaned_data['email']
                userObj.save()
            except Exception as err:
                print(err)

            redirect(to='logout')

        for error in form.errors:
            messages.add_message(request, messages.WARNING, 'Incorrect Details')

    context = {
        "form": form
    }
    return render(request, 'home/profile.html', context )


def index_view(request):
    # get all tags associated with the file
    audio_form = UploadForm()
    audio = ''
    if request.method == "POST":
        audio_form = UploadForm(request.POST, request.FILES)

        if audio_form.is_valid() is True:
            # Do something
            try:
                file = request.FILES['audio']
                audio = EasyID3(file)
            except mutagen.id3.ID3NoHeaderError as err:
                audio = File(file, easy=True)
                audio.add_tags()
                audio.save(audio, v1=2)

    context = {
        "audio": audio_form,
        "audio_tags": audio,
    }
    return render(request, "home/index.html", context)

@login_required
def merge_view(request, hash):
    try:
        form = ShortAudioForm()
        sound1 = get_object_or_404(AudioModel, user=request.user, hash=hash)

        if request.method == 'POST':
            form = ShortAudioForm(request.POST, request.FILES)
            if form.is_valid():
                sound2 = request.FILES['audio']
                position = form.cleaned_data['position']
                action = Merge(sound1.path, sound2, position)
                action.run_process(form.cleaned_data.get('seconds'),form.cleaned_data.get('volume'))
                return redirect(to='merge')

            for error in form.errors:
                messages.add_message(request, messages.WARNING, error)

            return redirect(to='merge')

    except Exception as err:
        messages.add_message(request, messages.WARNING, err)

    context = {
        "form": form,
    }
    return render(request, "home/merge.html", context)


@login_required
def remove_view(request, hash):
    try:

        form = AudioRangeForm()
        if request.method == 'POST':
            form = AudioRangeForm(request.POST)

            if form.is_valid():
                file = AudioModel.objects.get(user=request.user, hash=hash)
                minute = form.cleaned_data.get('minute')
                seconds = form.cleaned_data.get('seconds')
                length = form.cleaned_data.get('length')
                cropping = Crop(file.path, minute, seconds, length)
                cropping.run_process()
                messages.add_message(request, messages.SUCCESS, 'Audio File Edited Successful')

            for error in form.errors:
                messages.add_message(request, messages.WARNING, error)

            return redirect('remove',hash)

    except Exception as err:
        messages.add_message(request, messages.WARNING, err)

    context = {
        "form":form
    }
    return render(request, "home/remove.html", context)


@login_required
def tagging_view(request, hash):
    audio = get_object_or_404(AudioModel,hash=hash)
    audio_tags = Tagging(audio.path)
    form = AudioTagsForm(initial=audio_tags.tags())
    if request.method == 'POST':
        form = AudioTagsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                audio_tags.add_tag(form.cleaned_data, form.cleaned_data['cover'])
                messages.add_message(request, messages.SUCCESS, 'Audio File Tagged Successful')
            except Exception as err:
                print(err)

        for error in form.errors:
            print(error)
            messages.add_message(request, messages.WARNING, error)

        return redirect('tagging', hash)

    context  = {
        "form": form
    }
    return render(request, "home/tagging.html", context)


@login_required
def dashboard_view(request):
    fileFormSet = inlineformset_factory(User, AudioModel, widgets={
                                    'path': FileInput({'accept': '.mp3'})
                                    }, fields=['name', 'path'], exclude=['delete'],
                                        can_delete=False, extra=1, )
    if request.method == 'POST':
        userObj = User.objects.get(username=request.user)
        form = fileFormSet(request.POST, request.FILES, instance=userObj)

        if userObj is not None and form.is_valid() is True:

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Upload Success.')
            return redirect(to='dashboard')

        messages.add_message(request, messages.ERROR, 'Upload Failed!. check your data(audio) ')
        return redirect(to='dashboard')

    context = {
        "form": fileFormSet,
        "files": AudioModel.objects.filter(user=request.user)
    }
    return render(request, "home/dashboard.html", context)

@login_required
def cover_view(request):
    formset = inlineformset_factory(User, CoverPictureModel,
                                    fields=['name','path'],
                                    can_delete=False,
                                    exclude=['delete'],
                                    extra=1,
                                    widgets={'path':FileInput({'accept': '.jpeg, .jpg, .png'})})
    if request.method == 'POST':
        userObj = User.objects.get(username=request.user)
        form = formset(request.POST, request.FILES, instance=userObj)
        if userObj is not None and form.is_valid() is True:
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Upload Success.')
            return redirect(to='dashboard')

        messages.add_message(request, messages.ERROR, 'Upload Failed!. check your data(cover picture) ')
        return redirect(to='cover')


    context = {
        "form":formset
    }
    return render(request, "home/cover.html", context)


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'logged out successful!')
    return redirect(to='index')