from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=90)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=90, default="Author unknown")
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='blog_images')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.uploaded_by)

    def get_absolute_url(self):
        return reverse('blog_post', args=(str(self.id)))
