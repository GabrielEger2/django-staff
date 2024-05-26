from django.urls import path
from .views import EmployeeList, EmployeeUpdate, EmployeeDelete, EmployeeCreate, ExportCSV

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee_list'),
    path('create/', EmployeeCreate.as_view(), name='employee_create'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name='employee_update'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employee_delete'),
    path('export-csv/', ExportCSV.as_view(), name='employee_export_csv'),

]
