from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Employee, User

class EmployeeList(ListView):
    model = Employee

    def get_queryset(self):
        return Employee.objects.filter(company=self.request.user.employee.company)

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'department']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user.employee.company
        obj.user = User.objects.create_user(username=obj.name.split()[0] + obj.name.split()[1])
        obj.save()
        return super(EmployeeCreate, self).form_valid(form)

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'department']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/employees/'