from django.db import models #zwiazane z awarianem - bazami danych
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
# Create your models here.

class Post(models.Model): #tabela Post
    title = models.CharField(max_length=500, default=0, verbose_name = 'Measurement information')#numer pomiaru w ciągu dnia
    content = models.IntegerField(default=0, verbose_name = 'Glucose level')#poziom cukru zmiana
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
