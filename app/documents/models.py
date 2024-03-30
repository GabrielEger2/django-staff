from django.db import models
from app.employees.models import Employee
from django.urls import reverse

class Document(models.Model):
    name = models.CharField(max_length=100)
    holder = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='documents')

    def get_absolute_url(self):
        return reverse('employee_update', args=[str(self.holder.id)])

    def __str__(self):
        return self.name