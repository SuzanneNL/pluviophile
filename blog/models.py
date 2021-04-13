from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=90)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=90, default="Author unknown")
    body_part_1 = models.TextField()
    body_part_2 = models.TextField(blank=True, default='')
    body_part_3 = models.TextField(blank=True, default='')
    image_1 = models.ImageField(upload_to='blog_images')
    image_1_description = models.CharField(max_length=90, blank=True, default='')
    image_2 = models.ImageField(blank=True, upload_to='blog_images')
    image_2_description = models.CharField(max_length=90, blank=True, default='')
    image_3 = models.ImageField(blank=True, upload_to='blog_images')
    image_3_description = models.CharField(max_length=90, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    bookmarks = models.ManyToManyField(User, related_name='blog_posts_bookmarks')

    def __str__(self):
        return self.title + ' by ' + str(self.uploaded_by)

    def get_absolute_url(self):
        return reverse('blog_post', args=(str(self.id)))
