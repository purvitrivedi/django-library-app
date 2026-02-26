from django.db import models
from django.urls import reverse

# Create your models here.

PUBLISHER_NAMES = (
    ('P', 'Penguin Random House'),
    ('HL', 'Hachette Livre UK' ),
    ('HC', 'Harper Collins'),
)

class Publisher(models.Model):
    name = models.CharField(max_length=2, choices=PUBLISHER_NAMES, default= PUBLISHER_NAMES[0][0])
    website = models.URLField(max_length=200)  

    def __str__(self):
        return self.get_name_display()


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.id})
    

