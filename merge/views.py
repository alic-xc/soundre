from django.shortcuts import render
from django.views import generic
from merge.forms import MergeForm


class MergeView(generic.FormView):
    template_name = 'merging/merge.html'
    form_class = MergeForm