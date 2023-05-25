from django.db import models
from django.urls import reverse
from django.conf import settings



class Pages(models.Model):
    
    podcherk = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка подчёркивания', blank=True)
    text = models.CharField(max_length=35000, verbose_name='Текст внизу' , null=True)
    title = models.CharField(max_length=150, verbose_name='Название страницы')
    description = models.CharField(max_length=150, verbose_name='Мета описание')
    keywords = models.CharField(max_length=150, verbose_name='Мета слова')
    fotertitle = models.CharField(max_length=350, verbose_name='Заголовок в футере')
    fotercontent = models.CharField(max_length=550, verbose_name='Слова в футере')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Логотип', blank=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Category(models.Model):

    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    glavnoe_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']



class Slider(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок 1 слайда')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото 1 слайда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['title']




class Posts(models.Model):
    categoryid = models.CharField(max_length=6, verbose_name='Номер категории' , null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Категория') 
    title = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True,blank=True,allow_unicode=True)
    price = models.CharField(verbose_name='Цена',max_length=50)
    dopolnitelnie_xapakteristiki = models.CharField( verbose_name='Дополнительные характеристики',max_length=2550,null=True)
    polnoe_opisanie = models.CharField( verbose_name='Полное описание',max_length=10000)
    description = models.CharField(max_length=150, verbose_name='Мета описание',blank=True)
    keywords = models.CharField(max_length=150, verbose_name='Мета слова',blank=True)
    glavnoe_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    photo_na_slider = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото на слайдер',default=None,null=True)




    def get_absolute_url(self):
        return reverse('pages:view_posts', kwargs={"post_id": self.pk})
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['title']





class Photos(models.Model):
    title = models.ForeignKey('Posts', on_delete=models.CASCADE, null=True, verbose_name='Товар') 
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    num = models.CharField(max_length=10, verbose_name='Номер слайда', null=True)
 
    # def __str__(self):
    #     return self.title
    def photo_img(self):
        if self.photo:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.photo.url)
        else:
            return '(Нет изображения)'
    photo_img.short_description = 'Картинка'
    photo_img.allow_tags = True
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['title']



class Subscribers(models.Model):
    email = models.EmailField(max_length=150,blank=True,null=True,default=None)
    name = models.CharField(max_length=150,blank=True,null=True,default=None)
    nmb = models.CharField(default=None,max_length=150,blank=True,null=True)
    mas = models.CharField(default=None,max_length=350,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации',null=True)


    def __str__(self):
        
        return self.name

    class Meta:
        verbose_name = 'Форма' 
        verbose_name_plural = 'Формы' 
        ordering = ['-created_at']








