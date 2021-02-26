from django.urls import path
from .views import *


urlpatterns =[
    path('tag/<hash>', TagView.as_view(), name='tag'),
]