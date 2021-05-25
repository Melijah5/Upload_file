from django.db import models

# Create your models here.
class Book(models.Model):
    caption = models.CharField(max_length=100)
    # pdf = models.FileField(upload_to='books/pdfs/')
    image = models.ImageField(upload_to='images/%y', null=True, blank=True)