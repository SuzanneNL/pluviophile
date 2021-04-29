from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ProfileView, EditProfileView

urlpatterns = [
    path('profile/<slug>', ProfileView.as_view(), name="profile"),
    path('profile/edit/<slug>', EditProfileView.as_view(),
         name="edit_profile"),
    path('account', views.account, name='account'),
    path('error', views.error, name='error'),
]

if settings.DEBUG:
    """
    This stores images to the repository, when DEBUG is True
    """
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
