from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('merge/<uuid:file>/', merge_view, name='merge' ),
    path('tagging/<uuid:file>/', tagging_view, name='tagging'),
    path('remove/<uuid:file>/', remove_view, name='remove'),
    path('register', register_view, name='create'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile/', profile_view, name='profile' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)