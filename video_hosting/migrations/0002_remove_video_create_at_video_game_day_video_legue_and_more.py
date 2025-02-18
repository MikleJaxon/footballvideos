# Generated by Django 5.0.3 on 2024-03-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='create_at',
        ),
        migrations.AddField(
            model_name='video',
            name='game_day',
            field=models.DateField(default=None, verbose_name='Дата матча'),
        ),
        migrations.AddField(
            model_name='video',
            name='legue',
            field=models.CharField(blank=True, max_length=50, verbose_name='Лига'),
        ),
        migrations.AddField(
            model_name='video',
            name='team1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Команда 1'),
        ),
        migrations.AddField(
            model_name='video',
            name='team2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Команда 2'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок'),
        ),
    ]
