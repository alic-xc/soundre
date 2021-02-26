from django.urls import path
from .views import *


urlpatterns = [
    path('crop/<hash>', CropView.as_view(), name='crop'),
]