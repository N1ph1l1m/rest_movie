# Generated by Django 5.1 on 2024-08-29 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(default='actors/avatar.jpg', upload_to='actors/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='movies/default.jpg', upload_to='movies/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='image',
            field=models.ImageField(default='movie_shots/short-cat.png', upload_to='movie_shots/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie.movie', verbose_name='фильм'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='movie.review', verbose_name='Родитель'),
        ),
    ]
