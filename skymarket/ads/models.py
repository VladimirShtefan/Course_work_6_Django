from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Название товара')
    price = models.DecimalField(max_digits=20, decimal_places=0, validators=[MinValueValidator(0)],
                                verbose_name='Цена товара')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание товара')
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_ad')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('created_at',)


class Comment(models.Model):
    text = models.CharField(max_length=500, blank=False, null=False, verbose_name='Текст отзыва')
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_comment')
    ad = models.ForeignKey(Ad, verbose_name='Объявление', on_delete=models.CASCADE, related_name='ad_comment')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
