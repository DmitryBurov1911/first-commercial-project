from django.db import models
from django.urls import is_valid_path

class Artiles(models.Model):
    title = models.CharField('Название', max_length=100, default="")
    anons = models.CharField('Анонс', max_length=250, default="")
    full_text = models.TextField('Характеристики')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return f'Материал : {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Добавление материалов"
        verbose_name_plural = "Добавление материалов"