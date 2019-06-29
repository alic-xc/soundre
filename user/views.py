from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register_view(request):
    return render(request, "user/index.html", context=None)


def login_view(request):
    return HttpResponse("login")


def profile_view(request):
    return HttpResponse('profile')