from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    image=models.URLField(max_length=200)
    def __str__(self):
        return self.title

        
class BookM(models.Model):
    
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    image=models.URLField(max_length=200)
    def __str__(self):
        return self.title
    