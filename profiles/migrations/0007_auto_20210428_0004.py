# Generated by Django 3.1.8 on 2021-04-28 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210414_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
