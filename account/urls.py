from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('account/register', RegistrationView.as_view(), name='register'),
    path('account/login', LoginView.as_view(), name='login'),
    path('account/logout', logout_view, name='logout'),
    path('account/profile', ProfileView.as_view(), name='profile'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('fetch/audio', fetch_audio, name='fetch_audio'),
    path('', HomepageView.as_view(), name='homepage')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)