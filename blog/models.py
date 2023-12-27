from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    title = models.CharField('Название проекта', max_length=200)
    text = models.TextField('Описание проекта')
    role = models.CharField('Роль в проекте', max_length=200)
    img = models.ImageField('Изображение для заголовка проекта', default='no_image.png', upload_to='project', unique=True)
    img1 = models.ImageField('Изображение проекта', default='no_image.png', upload_to='project', unique=True)
    img2 = models.ImageField('Изображение проекта', default='no_image.png', upload_to='project', unique=True)
    img3 = models.ImageField('Изображение проекта', default='no_image.png', upload_to='project', unique=True)
    img4 = models.ImageField('Изображение проекта', default='no_image.png', upload_to='project', unique=True)
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return f'{self.title}'


    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})



    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

