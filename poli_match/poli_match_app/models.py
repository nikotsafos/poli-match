from django.db import models

# Create your models here.

class Politician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo_url = models.TextField()
    summary = models.TextField()
    office = models.CharField(max_length=100, default='some string')
    party = models.CharField(max_length=50, default='some string')



    def __str__(self):
        return self.last_name

class Quote(models.Model):
    content = models.TextField()
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.content