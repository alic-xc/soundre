from django.shortcuts import render
from django.views import generic
from tagging.forms import TagForm


class TagView(generic.FormView):
    template_name = 'tagging/tag.html'
    form_class = TagForm