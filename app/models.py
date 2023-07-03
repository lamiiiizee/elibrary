from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.IntegerField()
    cover = models.ImageField(upload_to="covers/", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.title} ({self.year})"