# Generated by Django 5.0.3 on 2024-03-22 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0002_remove_video_create_at_video_game_day_video_legue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleHighlights', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('legueHighlights', models.CharField(max_length=50, verbose_name='Лига')),
                ('videoHighlights', models.FileField(blank=True, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Видео')),
                ('image_titleHighlights', models.ImageField(blank=True, upload_to='images', verbose_name='Превью')),
                ('descriptionHighlights', models.TextField(blank=True, verbose_name='Описание')),
                ('highlights_day', models.DateField(verbose_name='Дата хайлайте')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleNews', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('textNews', models.TextField(blank=True, verbose_name='Новость')),
                ('image_titleNews', models.ImageField(blank=True, upload_to='images', verbose_name='Превью')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlePodcasts', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('image_titlePodcasts', models.ImageField(blank=True, upload_to='images', verbose_name='Превью')),
                ('audioPocasts', models.FileField(blank=True, upload_to='audio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name='Аудио')),
                ('descriptionPodcasts', models.TextField(blank=True, verbose_name='Описание')),
                ('podcastTheme', models.CharField(blank=True, max_length=100, verbose_name='Тема')),
            ],
        ),
    ]
