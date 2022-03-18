from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title
