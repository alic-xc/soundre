from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, FileUploadForm
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
    pass


def index_view(request):
    # get all tags associated with the file
    # audio_form = UploadFile()
    # context = {
    #     "audio": audio_form,
    #     "audio_tags": None,
    # }
    #
    # if request.method == "POST":
    #     audio_form = UploadFile(request.POST, request.FILES)
    #
    #     if audio_form.is_valid() is True:
    #         # Do something
    #         tags = Tagging(request.FILES['audio'])
    #         tags.view_tags()

    return render(request, "home/index.html", context=None)

@login_required
def merge_view(request):
    pass

@login_required
def remove_view(request):
    pass

@login_required
def tagging_view(request):
    pass

@login_required
def dashboard_view(request):
    form = FileUploadForm()
    if request.method == 'POST':
        pass
    context = {
        "form":form
    }
    return render(request, "home/dashboard.html", context)

@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'logged out successful!')
    return redirect(to='index')