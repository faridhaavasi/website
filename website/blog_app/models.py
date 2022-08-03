
from msilib.schema import Class
from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    text=models.TextField()
    image=models.ImageField(upload_to='maghalat',null=True)
    views=models.IntegerField(null=True)


    def __str__(self):
        return self.title

class Abute(models.Model):
    name=models.CharField(max_length=50)
    jub=models.CharField(max_length=50)
    age=models.IntegerField()
    madrak=models.CharField(max_length=50)
    description=models.TextField()


class Ticket(models.Model):
    title=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title

