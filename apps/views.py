from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def merge_view(request):
    return HttpResponse(" <H1>  merge 2 audio together")

def tagging_view(request):
    return HttpResponse("<H2> tagging a mp3 <H2>")

def remove_view(request):
    return HttpResponse("<h3> remove audio <h3>")