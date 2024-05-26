import csv
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import OvertimeRecord, Employee
from django.http import HttpResponse

class OvertimeRecordList(ListView):
    model = OvertimeRecord

    def get_queryset(self):
        return OvertimeRecord.objects.filter(employee__company=self.request.user.employee.company)
    
class OvertimeRecordCreate(CreateView):
    model = OvertimeRecord
    fields = ['reason', 'hours', 'employee']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['employee'].queryset = Employee.objects.filter(company=self.request.user.employee.company)
        return form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.employee = self.request.user.employee
        obj.save()
        return super(OvertimeRecordCreate, self).form_valid(form)

class OvertimeRecordUpdate(UpdateView):
    model = OvertimeRecord
    fields = ['reason', 'hours']

class OvertimeRecordDelete(DeleteView):
    model = OvertimeRecord
    success_url = '/overtime-record/'

class ExportCSV(ListView):
    model = OvertimeRecord

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="overtime_record.csv"'

        writer = csv.writer(response)
        writer.writerow(['Employee', 'Reason', 'Hours'])

        for obj in OvertimeRecord.objects.filter(employee__company=self.request.user.employee.company):
            writer.writerow([obj.employee, obj.reason, obj.hours])

        return response