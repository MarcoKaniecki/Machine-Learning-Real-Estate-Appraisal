# Generated by Django 4.1.7 on 2023-04-01 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_delete_post_remove_listing_content_listing_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='foundation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
