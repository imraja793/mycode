from django.core.serializers import serialize
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_student=True)


class StudentManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_student=False)


class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    class_in = models.CharField(max_length=50, null=True, blank=True)
    objects = StudentManager()
    objects2 = StudentManager2()
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Books(models.Model):
    Book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_description = models.CharField(max_length=300)
