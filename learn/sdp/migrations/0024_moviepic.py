# Generated by Django 4.1.1 on 2022-12-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0023_remove_addmovies_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='moviepic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
