from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField('Заголовок',max_length=100, blank = True)
    description = models.TextField('Описание', blank = True)
    image = models.ImageField('Превью', upload_to='image/', blank=True)
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    game_day = models.DateField('Дата матча', default = None)
    legue = models.CharField('Лига',max_length=50, blank=True)
    team1 = models.CharField('Команда 1', max_length=100, blank=True)
    team2 = models.CharField('Команда 2', max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class New(models.Model):
    titleNews = models.CharField('Заголовок', max_length=100, blank=True)
    textNews = models.TextField('Новость', blank=True)
    image_titleNews = models.ImageField('Превью', upload_to='image',blank=True)

    def __str__(self):
        return self.titleNews
    
class Highlite(models.Model):
    titleHighlights = models.CharField('Заголовок', max_length=100, blank=True)
    legueHighlights = models.CharField('Лига',max_length=50)
    videoHighlights = models.FileField('Видео', upload_to='videos', validators=[FileExtensionValidator(allowed_extensions=['mp4'])], blank=True)
    image_titleHighlights = models.ImageField('Превью', upload_to='image',blank=True)
    descriptionHighlights = models.TextField('Описание', blank=True)
    highlights_day = models.DateField('Дата хайлайте')

    def __str__(self):
        return self.titleHighlights
    
class Podcast(models.Model):
    titlePodcasts = models.CharField('Заголовок', max_length=100, blank=True)
    image_titlePodcasts = models.ImageField('Превью', upload_to='image',blank=True)
    audioPocasts = models.FileField('Аудио', upload_to='audio', validators=[FileExtensionValidator(allowed_extensions=['mp3'])], blank=True)
    descriptionPodcasts = models.TextField('Описание', blank=True)
    podcastTheme = models.CharField('Тема', max_length=100, blank=True)

    def __str__(self):
        return self.titlePodcasts
