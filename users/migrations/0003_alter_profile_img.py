# Generated by Django 4.2.7 on 2023-11-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='user_images', verbose_name='Фото пользователя'),
        ),
    ]
