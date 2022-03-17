from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name',max_length=50,default='Enter title text')
    intro = models.CharField('Intro',max_length=250)
    full_text = models.TextField('FullTXT')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        