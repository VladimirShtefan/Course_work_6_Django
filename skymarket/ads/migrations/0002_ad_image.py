# Generated by Django 4.1.4 on 2022-12-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='Изображение'),
        ),
    ]
