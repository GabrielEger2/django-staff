from django.db import models
from django.contrib.auth.models import User
from app.departments.models import Department
from app.companies.models import Company
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('employee_list')
    
    @property
    def total_overtime_record(self):
        total = self.overtimerecord_set.all().aggregate(models.Sum('hours'))['hours__sum']
        return total

    def __str__(self):
        return self.name