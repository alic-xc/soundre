from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from account.forms import RegistrationForm, LoginForm


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
            return redirect('dashobard')

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


class ProfileView(generic.TemplateView):
    """ User profile view """
    template_name = 'account/profile.html'


class DashboardView(generic.TemplateView):
    """ User Dashboard """
    template_name = 'account/dashboard.html'

@login_required
def logout_view(request):
    logout(request)
    return redirect(to='index')