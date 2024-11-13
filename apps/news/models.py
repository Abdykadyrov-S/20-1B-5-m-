from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='news',
        verbose_name='Фото'
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