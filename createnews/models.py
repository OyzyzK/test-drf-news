from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

class NewsItem(models.Model):
    objects = models.Manager()
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=50, verbose_name='Название новости', unique=True)
    description = models.TextField(verbose_name='Описание поста')
    image = models.ImageField(verbose_name='Картинка новости', default=None, null=True, blank=True, upload_to='img')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания поста')

    def __str__(self):
        return f'Новость: {self.title}'
