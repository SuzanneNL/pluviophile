from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=90)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=90, default="Author unknown")
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.uploaded_by)
