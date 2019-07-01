from django.urls import path
from .views import (
        index_view,
        login_view, 
        merge_view, 
        profile_view,
        remove_view, 
        register_view, 
        tagging_view, 
    )


urlpatterns = [
    path('', index_view, name='index'),
    path('apps/merge', merge_view, name='merge' ),
    path('apps/tagging', tagging_view, name = 'tagging'),
    path('apps/remove', remove_view, name='remove'),
    path('user/register', register_view, name='create'),
    path('user/signin', login_view, name='login'),
    path('user/<uuid>/profile',profile_view, name='profile' )
]