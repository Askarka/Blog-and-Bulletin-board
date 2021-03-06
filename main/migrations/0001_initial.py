# Generated by Django 3.2.2 on 2021-05-11 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('text', models.TextField()),
                ('admin_social_network', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('author', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Simbolic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('description', models.CharField(max_length=100, verbose_name='Описание картинки')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='images', to='main.event', verbose_name='Пост события')),
            ],
        ),
    ]
