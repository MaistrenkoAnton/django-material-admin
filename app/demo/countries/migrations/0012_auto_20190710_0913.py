# Generated by Django 2.2.2 on 2019-07-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0011_person_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='google_play',
            field=models.URLField(blank=True, null=True, verbose_name='Google Play Link'),
        ),
        migrations.AddField(
            model_name='person',
            name='itunes',
            field=models.URLField(blank=True, null=True, verbose_name='Itunes Link'),
        ),
        migrations.AddField(
            model_name='person',
            name='spotify',
            field=models.URLField(blank=True, null=True, verbose_name='Spotify Link'),
        ),
        migrations.AddField(
            model_name='person',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Video'),
        ),
    ]