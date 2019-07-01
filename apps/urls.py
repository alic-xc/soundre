from django.urls import path
from .views import (
        dashboard_view,
        index_view,
        login_view,
        logout_view,
        merge_view, 
        profile_view,
        remove_view, 
        register_view, 
        tagging_view,
    )


urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard', dashboard_view, name='dashboard'),
    path('merge', merge_view, name='merge' ),
    path('tagging', tagging_view, name='tagging'),
    path('remove', remove_view, name='remove'),
    path('register', register_view, name='create'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile' )
]