from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from account.models import AudioModel
from audioEditing.tagging import Tagging
from tagging.forms import TagForm


class TagView(generic.FormView):
    template_name = 'tagging/tag.html'
    form_class = TagForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object'] = get_object_or_404(AudioModel, hash=self.kwargs.get('hash'))
        return context

    def get_initial(self):
        audio = get_object_or_404(AudioModel, hash=self.kwargs.get('hash'))
        audio_tags = Tagging(audio.audio)
        return audio_tags.tags()

    def get_success_url(self):
        return reverse('tag', kwargs={'hash': self.kwargs.get('hash')})

    def form_valid(self, form):
        try:
            audio = self.get_context_data()['object']
            audio_tags = Tagging(audio.audio)
            audio_tags.add_tag(form.cleaned_data, form.files['cover'])
            messages.success(self.request, 'Audio File Tagged Successful')
            return super().form_valid(form)
        except Exception as err:
            messages.error(self.request, err)

        return super().form_invalid(form)


