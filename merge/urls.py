from django.urls import path
from .views import *


urlpatterns =[
    path('merge/<hash>', MergeView.as_view(), name='merge'),
]