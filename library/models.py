# library/models.py
from django.db import models
from django.contrib.auth.models import User


class Library(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "کتابخانه ها"
        verbose_name = "کتابخانه"


class Category(models.Model):
    name = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "کتاب ها"
        verbose_name = "کتاب"


class Member(models.Model):
    name = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "اعضا"
        verbose_name = "عضو"
