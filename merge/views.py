from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from account.models import AudioModel
from audioEditing.merge import Merge
from merge.forms import MergeForm


class MergeView(LoginRequiredMixin, generic.FormView):
    template_name = 'merging/merge.html'
    form_class = MergeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object'] = get_object_or_404(AudioModel, hash=self.kwargs.get('hash'))
        return context

    def get_success_url(self):
        return reverse('merge', kwargs={'hash': self.kwargs.get('hash')})

    def form_valid(self, form):
        main_audio = self.get_context_data()['object'].audio
        stamp_audio = form.cleaned_data['audio']
        position = form.cleaned_data['position']

        try:
            action = Merge(main_audio, stamp_audio, position)
            action.run_process(form.cleaned_data['seconds'])
            messages.success(self.request, "Audio stamped Successfully")
        except Exception as err:
            messages.error(self.request, err)

        return super().form_valid(form)

