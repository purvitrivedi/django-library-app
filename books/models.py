from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.id})
    


