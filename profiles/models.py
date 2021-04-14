from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=2000, blank=True, null=True)
    country = CountryField(blank=True, null=True, blank_label='(Select your country)')
    date_of_birth = models.DateField(blank=True, null=True)
    member_since = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True)
    avatar = models.ImageField(default='default-avatar.jpg',
                               upload_to='avatars')

    def __str__(self):
        return "%s's profile" % (self.user)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user)
            if Profile.objects.filter(slug=self.slug).exists():
                uniqueid = str(uuid4()).split('-')[0]
                self.slug = slugify('{}{}'.format(self.user, uniqueid))
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save
