# Generated by Django 4.1.1 on 2022-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0016_marriage_movie_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('problem', models.CharField(max_length=600)),
            ],
        ),
    ]
