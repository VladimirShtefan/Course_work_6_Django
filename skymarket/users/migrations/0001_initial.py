# Generated by Django 4.1.4 on 2022-12-17 16:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия пользователя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон для связи')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=5, verbose_name='Роль')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='Аватарка')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
