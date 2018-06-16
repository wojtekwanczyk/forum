from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as builtin_user

# Create your models here.

'''
class User():
    # username
    # password
    # email
    # first_name
    # last_name
    join_date = models.DateTimeField()
    age = models.IntegerField()
    banned = models.BooleanField(default=False)

    def ban(self):
        self.banned = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name + '(' + self.username + ')'
'''

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)


class Thread(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)