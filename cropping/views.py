from django.shortcuts import render
from django.views import generic
from cropping.forms import CropForm


class CropView(generic.FormView):
    """ This view handle cropping of audio to desired length """
    template_name = 'cropping/crop.html'
    form_class = CropForm