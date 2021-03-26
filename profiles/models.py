from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=2000)
    country = CountryField(blank=True, null=True, blank_label='(Select your country)')
    member_since = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(default='default-avatar.jpg',
                               upload_to='avatars')

    def __str__(self):
        return "%s's profile" % (self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save
