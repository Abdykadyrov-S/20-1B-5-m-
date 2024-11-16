from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории для новостей'

class News(models.Model):
    category = models.OneToOneField(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='news',
        verbose_name='Фото', 
        null=True, blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'