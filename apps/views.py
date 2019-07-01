from django.shortcuts import render
from .forms import TagViewForm, TagEditForm
from audioEditing.tagging import Tagging
# Create your views here.


def index_view(request):
    # get all tags associated with the file
    audio_form = TagViewForm()
    context = {
        "audio": audio_form,
        "audio_tags": None,
    }

    if request.method == "POST":
        audio_form = TagViewForm(request.POST, request.FILES)

        if audio_form.is_valid() is True:
            # Do something
            tags = Tagging(request.FILES['audio'])
            tags.view_tags()

    return render(request, "home/index.html", context)


def merge_view(request):
    pass

def remove_view(request):
    pass

def tagging_view(request):
    pass

def register_view(request):
    pass

def login_view(request):
    pass

def profile_view(request):
    pass