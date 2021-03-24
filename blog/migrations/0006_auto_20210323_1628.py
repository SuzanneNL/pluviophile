# Generated by Django 3.1.7 on 2021-03-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='body_part_1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='header_image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='body_part_2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='body_part_3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_1_description',
            field=models.CharField(blank=True, default='', max_length=90),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_2_description',
            field=models.CharField(blank=True, default='', max_length=90),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_3_description',
            field=models.CharField(blank=True, default='', max_length=90),
        ),
    ]