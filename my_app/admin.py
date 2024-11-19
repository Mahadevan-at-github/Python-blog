from django.contrib import admin
from .models import Book, loginTable,BlogPosting

# Register your models here.

admin.site.register(Book)
admin.site.register(loginTable)
admin.site.register(BlogPosting)


