# Generated by Django 5.0.3 on 2024-04-26 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_roomactivity_room_host_message_room_roomactivity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='roomactivity',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
