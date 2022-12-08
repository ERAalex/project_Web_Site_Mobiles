from django.db import models
# from PIL import Image
from django.utils.text import slugify




class all_products(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField('Название модели', max_length=50)
    price = models.IntegerField(default=0, verbose_name='Цена')
    full_text = models.TextField('описание')
    date = models.DateTimeField('Дата публикации')
    small_image = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name='Мини-изображение')
    artimage = models.ImageField(null=True, blank=True, upload_to='static/img/top_models', verbose_name=' основное изображение')

    discount_active = models.BooleanField('Есть скидка?', default=False)
    discount = models.IntegerField(default=0, null=True, blank=True, verbose_name='Скидка')

    show_item = models.BooleanField('Наличие товара', default=False)
    show_on_main_page = models.BooleanField('Показать на главной странице', default=False)

    show_apple = models.BooleanField('Apple', default=False)
    show_samsung = models.BooleanField('Samsung', default=False)
    show_huawei = models.BooleanField('Huawei', default=False)
    show_honor = models.BooleanField('Honor', default=False)
    slug = models.SlugField(blank=True)



# скидка
    def get_final_price(self):
        if self.discount == 0:      # если скидки нет (то не идем дальше)
            s = "."
            return s     # заглушка, иначе css сдвигает колонки с фото, не ровно.
        else:
            total = self.price - (self.price * self.discount)/100
            return (f'Скидка {self.discount}%! {round(total)}')  # round - убираем нули после запятой




# авто сохранение поля слаг = по полю title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(all_products, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'




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
