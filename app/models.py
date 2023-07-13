from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse_lazy

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "writer and book"
        verbose_name_plural = "writer and books"

    def get_absolute_url(self):
        return reverse_lazy('app:auther_detial', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse_lazy('app:auther_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('app:auther_delete', kwargs={'pk': self.pk})

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.IntegerField()
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name="books")
    cover = models.ImageField("Book Cover" ,upload_to="covers/", blank=True )
    description = models.TextField(blank=True ,verbose_name="c")
    price = models.DecimalField(max_digits=6, decimal_places=2 ,help_text='Description Description')
    is_special = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    def get_absolute_url(self):
        return reverse_lazy('app:book_detial', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse_lazy('app:book_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('app:book_delete', kwargs={'pk': self.pk})


class FavoriteBook(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='favorite_books')
    books = models.ManyToManyField(Book)


    def __str__(self):
        return str(self.user)
    
