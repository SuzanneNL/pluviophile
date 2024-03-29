# Generated by Django 3.1.7 on 2021-04-13 20:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_remove_blogpost_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='bookmarks',
            field=models.ManyToManyField(related_name='blog_posts_bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
