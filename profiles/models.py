from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=2000)
    member_since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s's profile" % (self.user)
