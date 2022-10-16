from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms


class Point(models.Model):
    title = models.TextField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    cat = models.ForeignKey('Add', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['pub_date', 'title']


class Add(models.Model):
    name = models.TextField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Comment(models.Model):
    comment = models.CharField(max_length=200, verbose_name='Оставить комментарий ')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    ident = models.TextField(max_length=100, blank=True)
    user = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['comment', 'date']


class WriteToTraining(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона ')
    datetime = models.DateTimeField(verbose_name='Дата записи', blank=True)

    def get_absolute_url(self):
        return reverse('write')


class AbautModel(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
