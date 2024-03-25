from django.db import models
from app.employees.models import Employee

class Document(models.Model):
    name = models.CharField(max_length=100)
    holder = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name