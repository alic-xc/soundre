from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from account.forms import RegistrationForm, LoginForm, UploadAudioForm
from account.models import AudioModel


class RegistrationView(generic.FormView):
    """ Manage user registration """
    template_name = 'account/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class LoginView(generic.FormView):
    """ Manage user login """
    template_name = 'account/login.html'
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        """ Check if a user session is active before logging in """
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('dashboard')

    def form_valid(self, form):
        """ Login user if credentials is valid. """
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, "Email/Password incorrect. please try again")

        return super().form_invalid(form)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """ User profile view """
    template_name = 'account/profile.html'


class DashboardView(LoginRequiredMixin, generic.FormView):
    """ User Dashboard """
    template_name = 'account/dashboard.html'
    form_class = UploadAudioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['audio_objects'] = AudioModel.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse('dashboard')

    def form_valid(self, form):
        total_files = AudioModel.objects.filter(user=self.request.user).count()

        # Check total files uploaded by user
        if total_files > 5:
            messages.error(self.request, "Max upload limit reached.")
            return super().form_invalid(form)

        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Audio added successfully.")
        return super().form_valid(form)


@login_required
def fetch_audio(request):
    """ A AJAX request to pull all audio for a user """
    total_files = AudioModel.objects.filter(user=request.user)
    data = []
    for file in total_files:
        data.append({'id': file.hash, 'name': file.name, 'file': file.audio.url})
    return JsonResponse(data={'data': data}, status=200)



@login_required
def logout_view(request):
    logout(request)
    return redirect(to='index')