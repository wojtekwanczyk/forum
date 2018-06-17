from django.contrib import admin
from .models import Post, Thread, Message

# Register your models here.

admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Message)