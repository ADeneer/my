# Generated by Django 4.2.7 on 2023-12-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_project_delete_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(default='no_image.png', upload_to='user_images', verbose_name='Изображение проекта'),
        ),
    ]
