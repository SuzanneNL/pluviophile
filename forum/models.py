from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.creator)
