from django.db import models
from django.views.generic.edit import CreateView
from django.urls import reverse


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.full_name} ({self.birth_year})"


class Friend(models.Model):
    full_name = models.TextField()

    def __str__(self):
        return f"{self.full_name}"


# добавляем новую модель Редакция - Edition
class Edition(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Связываем модель Edition по принципу OneToMany с моделью Книги
    edition = models.ForeignKey(Edition, null=True, on_delete=models.CASCADE)

    copy_count = models.IntegerField(default=1)
    price = models.FloatField(default=0)

    logo = models.ImageField(upload_to='img/books_logo', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('redactions')

    def get_update_url(self):
        return reverse('book_update', kwargs={'pk': self.pk})

    def get_logo_url(self):
        try:
            return self.logo.url
        except:
            return ""


class BookRent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f'Книгу "{self.book}" взял "{self.friend}"'
