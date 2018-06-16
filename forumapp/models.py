from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    join_date = models.DateTimeField()
    age = models.IntegerField()
    banned = models.BooleanField(default=False)

    def ban(self):
        self.banned = True

    def __str__(self):
        return self.name + ' ' + self.surname + '(' + self.username + ')'


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)


class Thread(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)