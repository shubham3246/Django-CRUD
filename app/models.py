from django.db import models

# Create your models here.
class Event(models.Model):
    type = models.CharField(max_length=100)
    uid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=300)
    schedule = models.DateTimeField(auto_now=True)
    description = models.TextField()
    files = models.ImageField(upload_to='images', blank=True, null=True)
    moderator = models.IntegerField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    rigor_rank = models.IntegerField()
    attendees = models.CharField(max_length=500)