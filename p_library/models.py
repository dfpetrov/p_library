from django.db import models


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
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Связываем модель Edition по принципу OneToMany с моделью Книги
    edition = models.ForeignKey(Edition, null=True, on_delete=models.CASCADE)

    copy_count = models.IntegerField(default=1)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title

class BookRent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f'Книгу "{self.book}" взял "{self.friend}"'