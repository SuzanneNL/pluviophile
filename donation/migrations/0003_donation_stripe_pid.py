# Generated by Django 3.1.7 on 2021-04-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_auto_20210405_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
