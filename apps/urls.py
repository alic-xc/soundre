from django.urls import path
from .views import merge_view, tagging_view, remove_view


urlpatterns = [
    path('merge', merge_view, name='merge' ),
    path('tagging', tagging_view, name = 'tagging'),
    path('remove', remove_view, name='remove')
]