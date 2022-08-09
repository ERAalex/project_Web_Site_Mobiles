from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Расширение модели пользователя с помощью связи один-к-одному
#__________
# информация -  https://tproger.ru/translations/extending-django-user-model/
# чтобы в шаблоне обратиться к данным  - <li>Местоположение: {{ user.profile.location }}</li>
# для снижения запросов использовать код  - users = User.objects.all().select_related('profile')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

#__________



class all_products(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('Название модели', max_length=50)
    price = models.CharField('Стоимость модели', null=True, max_length=50)
    full_text = models.TextField('описание')
    date = models.DateTimeField('Дата публикации')
    small_image = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name='Мини-изображение')
    artimage = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name=' основное изображение')
    show_item = models.BooleanField('Показать', default=False)
    show_apple = models.BooleanField('Apple', default=False)
    show_samsung = models.BooleanField('Samsung', default=False)
    show_huawei = models.BooleanField('Huawei', default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'



class Order(models.Model):
    pass


class OrderPosition(models.Model):
    product = models.ForeignKey(all_products, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()



class Top_Models(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
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