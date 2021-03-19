from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    BlogPostsListView,
    BlogPostView,
    AddBlogPostView,
    EditBlogPostView,
    DeleteBlogPostView,
)


urlpatterns = [
    path('', BlogPostsListView.as_view(), name="blog"),
    path('blogpost/<int:pk>', BlogPostView.as_view(), name="blog_post"),
    path('add_blogpost/', AddBlogPostView.as_view(), name="add_blog_post"),
    path('blogpost/edit/<int:pk>', EditBlogPostView.as_view(), name="edit_blog_post"),
    path('blogpost/delete/<int:pk>', DeleteBlogPostView.as_view(), name="delete_blog_post"),
    path('error', views.error, name='error')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
