# Generated by Django 3.0.8 on 2020-10-24 10:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youtube', '0008_video_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='favouriteyt',
            field=models.ManyToManyField(blank=True, related_name='favouriteyt', to=settings.AUTH_USER_MODEL),
        ),
    ]
