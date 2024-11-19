
from django.db import models

# Create your models here.


class Book(models.Model):
    username = models.CharField(max_length=200,null=True)
    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=200,null=True)
    password2 = models.CharField(max_length=200,null=True)

    imge= models.ImageField(upload_to='book_media')


    def __str__(self):
        return '{}'.format(self.username)

class loginTable(models.Model):
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    password2 = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200)

    images= models.ImageField(upload_to='book_media')


    def __str__(self):
        return '{}'.format(self.username)

class BlogPosting(models.Model):

    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=500)
    comment = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog_media')


    user = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.title)

