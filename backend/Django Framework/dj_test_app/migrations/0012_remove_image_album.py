# Generated by Django 4.1.3 on 2023-01-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_test_app', '0011_alter_image_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
    ]
