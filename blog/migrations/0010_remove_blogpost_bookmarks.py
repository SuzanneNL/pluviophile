# Generated by Django 3.1.7 on 2021-04-13 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='bookmarks',
        ),
    ]
