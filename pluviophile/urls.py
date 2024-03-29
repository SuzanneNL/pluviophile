from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('forum/', include('forum.urls')),
    path('profiles/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('donation/', include('donation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
