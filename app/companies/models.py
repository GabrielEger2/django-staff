from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name of the company")
    