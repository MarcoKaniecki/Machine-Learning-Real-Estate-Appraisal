# Generated by Django 4.1.7 on 2023-03-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_bedroom_post_bldgtype_post_bsmtfintype1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fstFloorArea',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sndFloorArea',
        ),
        migrations.AddField(
            model_name='post',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
