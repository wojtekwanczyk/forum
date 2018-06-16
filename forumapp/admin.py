from django.contrib import admin
from .models import Post, Thread, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(User)