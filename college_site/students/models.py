from django.db import models
from django.contrib.auth.models import User 


class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=1000, blank=True)
    location = models.CharField(max_length=50, verbose_name='location')
    date_registration = models.DateTimeField(verbose_name='date_of_registration', auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    clubs = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', default='default.jpg', null=True)
    clubs = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return self.name  
    

