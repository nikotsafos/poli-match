from django.db import models

# Create your models here.

class Politician(models.Model):
    title = models.CharField(max_length=25, default=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.CharField(max_length=25, default=True)
    gender = models.CharField(max_length=10, default=True)
    party = models.CharField(max_length=10)
    twitter_account = models.CharField(max_length=25, null=True)
    url = models.CharField(max_length=100, default=True)
    total_votes = models.IntegerField(default=0)
    missed_votes = models.IntegerField(default=0, null=True)
    phone = models.CharField(max_length=25, default=True, null=True)
    state = models.CharField(max_length=10, default=True)
    state_rank = models.CharField(max_length=101, default=True, null=True)
    missed_votes_pct = models.FloatField(default=0)
    votes_with_party_pct = models.FloatField(default=0)

    def __str__(self):
        return self.last_name

class Quote(models.Model):
    content = models.TextField()
    source = models.CharField(max_length=50, default='some string')
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return self.content