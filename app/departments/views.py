from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Department

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