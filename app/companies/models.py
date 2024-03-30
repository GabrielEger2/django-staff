from django.db import models
from django.urls import reverse

class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name of the company")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')