# Generated by Django 4.1.1 on 2022-11-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdp', '0013_delete_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('sname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('pph', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
