# Generated by Django 4.1.1 on 2022-12-03 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0022_addmovies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmovies',
            name='avatar',
        ),
    ]
