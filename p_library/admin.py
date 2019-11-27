from django.contrib import admin
from p_library.models import Book, Author, Edition, Friend, BookRent

# Register your models here.


# Добавляем новую панель Редакции в админку
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('year_release', 'author')
    list_display = ('title', 'author', 'year_release', 'price', 'edition', 'id')
    # list_display_links = ('author', 'price')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(BookRent)
class BookRentAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')