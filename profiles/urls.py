from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ProfileView, EditProfileView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('profile/edit/<int:pk>', EditProfileView.as_view(), name="edit_profile"),
    path('error', views.error, name='error')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
