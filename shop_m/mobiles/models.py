from django.db import models
from PIL import Image
from embed_video.fields import EmbedVideoField


class Top_Models(models.Model):

    title = models.CharField('Название модели', max_length=50)
    price = models.CharField('Стоимость модели', null=True, max_length=50)
    full_text = models.TextField('описание')
    date = models.DateTimeField('Дата публикации')
    small_image = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name='Мини-изображение')
    artimage = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name=' основное изображение')
    show_art1 = models.BooleanField('Показать на 1 позици', default=False)
    show_art2 = models.BooleanField('Показать на 2 позици', default=False)
    show_art3 = models.BooleanField('Показать на 3 позици', default=False)
    show_art4 = models.BooleanField('Показать на 4 позици', default=False)
    show_art5 = models.BooleanField('Показать на 5 позици', default=False)
    show_art6 = models.BooleanField('Показать на 6 позици', default=False)
    show_art7 = models.BooleanField('Показать на 7 позици', default=False)
    show_art8 = models.BooleanField('Показать на 8 позици', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Топ модели'
        verbose_name_plural = 'Топ модели'



class main_images(models.Model):

    title = models.CharField('Название картинки', max_length=50)
    artimage = models.ImageField(null=True, blank=True, upload_to='static/img/home', verbose_name='изображение')
    position1 = models.BooleanField('положение центральное', default=False)# by setting default to 'False' disabled the flag for the existing entries as well
    position2 = models.BooleanField('картинка длинная внизу', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основные изображения'
        verbose_name_plural = 'Основные изображения'