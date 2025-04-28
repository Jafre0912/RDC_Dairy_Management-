from django.db import models

class Cattle(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    milk_production = models.FloatField()

class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)