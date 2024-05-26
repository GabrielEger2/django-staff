import csv
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Department
from django.http import HttpResponse

class DepartmentList(ListView):
    model = Department

    def get_queryset(self):
        return Department.objects.filter(company=self.request.user.employee.company)
    
class DepartmentCreate(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.employee.company
        obj.save()
        return super(DepartmentCreate, self).form_valid(form)
    
class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name']

class DepartmentDelete(DeleteView):
    model = Department
    success_url = '/departments/'

class ExportCSV(ListView):
    model = Department

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="departments.csv"'

        writer = csv.writer(response)
        writer.writerow(['Company', 'Department'])

        for obj in Department.objects.filter(company=self.request.user.employee.company):
            writer.writerow([obj.company, obj.name])

        return response