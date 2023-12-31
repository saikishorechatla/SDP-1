# Generated by Django 4.1.1 on 2022-12-03 21:49

from django.db import migrations, models
import sdp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0026_remove_addmovies2_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('price', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=sdp.models.filepath)),
            ],
        ),
    ]
