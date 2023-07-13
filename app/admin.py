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

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "author", "price", "is_special", "is_trending")
    list_filter = ("is_special", "is_trending", "author")
    search_fields = ("title", "author__name", "year")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    autocomplete_fields =  ("user","books")