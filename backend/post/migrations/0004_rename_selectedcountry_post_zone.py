# Generated by Django 4.1.7 on 2023-03-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_selectedcountry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='selectedCountry',
            new_name='zone',
        ),
    ]
