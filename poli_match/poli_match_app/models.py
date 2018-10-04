from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo_url = models.TextField()


    def __str__(self):
        return self.first_name

class Politician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo_url = models.TextField()


    def __str__(self):
        return self.first_name + self.last_name

class Quote(models.Model):
    content = models.TextField()
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.content