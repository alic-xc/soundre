from django.urls import path
from .views import *


urlpatterns = [
    path('account/register', RegistrationView.as_view(), name='register'),
    path('account/login', LoginView.as_view(), name='login'),
    path('account/logout', logout_view, name='logout'),
    path('account/profile', ProfileView.as_view(), name='profile'),
    path('dashboard', DashboardView.as_view(), name='dashboard')
]