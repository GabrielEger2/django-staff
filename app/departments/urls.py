from django.urls import path
from .views import DepartmentList, DepartmentCreate, DepartmentUpdate, DepartmentDelete, ExportCSV 

urlpatterns = [
    path('', DepartmentList.as_view(), name='department_list'),
    path('create/', DepartmentCreate.as_view(), name='department_create'),
    path('update/<int:pk>/', DepartmentUpdate.as_view(), name='department_update'),
    path('delete/<int:pk>/', DepartmentDelete.as_view(), name='department_delete'),
    path('export-csv/', ExportCSV.as_view(), name='department_export_csv'),
]