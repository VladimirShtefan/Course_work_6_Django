from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Название товара')
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(0)], verbose_name='Цена товара')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Описание товара')
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_ad')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', max_length=1500)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('created_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=1000, blank=False, null=False, verbose_name='Текст отзыва')
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_comment')
    ad = models.ForeignKey(Ad, verbose_name='Объявление', on_delete=models.CASCADE, related_name='ad_comment')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)
