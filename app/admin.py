from django.contrib import admin
from .models import Book
from .models import BookAuthor
from .models import FavoriteBook
# Register your models here.



class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ("title","slug", "year", "price", "is_special", "is_trending")

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]


@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    pass