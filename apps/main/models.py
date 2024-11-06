from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(upload_to="logo/")
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Основные настройки"
    