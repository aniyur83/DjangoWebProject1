"""
Definition of models.
"""

from turtle import mode
from xmlrpc.client import DateTime
from django.db import models


from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "title1")
    description = models.TextField(verbose_name = "content")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_url(self): # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title

# Метаданные – вложенный класс, который задает дополнительные параметры модели:

    class Meta:
        db_table = "Blog" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога
admin.site.register(Blog)
class Comment(models.Model):
    text = models.TextField(verbose_name = "Comment")
    #date=models.DateTimeField(default=datetime.now(),db_index=True,verbose_name="dada")
    #post = models.TextField(verbose_name = "comment")
    post = models.ForeignKey(Blog,default=1, on_delete=models.CASCADE,verbose_name="статья")
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.text 
    
    class Meta:
        db_table = "Comment" # имя таблицы для модели
        #ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Comment)
