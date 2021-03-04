from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from account.models import AudioModel
from audioEditing.remove import Crop
from cropping.forms import CropForm


class CropView(generic.FormView):
    """ This view handle cropping of audio to desired length """
    template_name = 'cropping/crop.html'
    form_class = CropForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['object'] = get_object_or_404(AudioModel, hash=self.kwargs.get('hash'))
        return context

    def get_success_url(self):
        return reverse('crop', kwargs={'hash': self.kwargs.get('hash')})

    def form_valid(self, form):
        """ """

        minute = form.cleaned_data['minute']
        seconds = form.cleaned_data['seconds']
        length = form.cleaned_data['length']

        try:
            cropping = Crop()
            if not cropping.run_process():
                messages.error(self.request, "Unable to process request. Please check crop length and try again")

            messages.success(self.request, "Audio cropped successfully")
        except (AttributeError, Exception) as err:
            messages.error(self.request, "Ops, something went wrong. Please try again")

        return super().form_valid(form)