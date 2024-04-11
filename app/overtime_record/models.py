from django.db import models
from app.employees.models import Employee
from django.urls import reverse

class OvertimeRecord(models.Model):
    reason = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('overtime_record_list')

    def __str__(self):
        return self.reason