from django.db import models


class Contact(models.Model):
    email = models.EmailField(blank=False)
    message = models.TextField()

class ResearchRequest(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
