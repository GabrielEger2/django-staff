from django.urls import path
from .views import OvertimeRecordList, OvertimeRecordCreate, OvertimeRecordUpdate, OvertimeRecordDelete, ExportCSV

urlpatterns = [
    path('', OvertimeRecordList.as_view(), name='overtime_record_list'),
    path('create/', OvertimeRecordCreate.as_view(), name='overtime_record_create'),
    path('update/<int:pk>/', OvertimeRecordUpdate.as_view(), name='overtime_record_update'),
    path('delete/<int:pk>/', OvertimeRecordDelete.as_view(), name='overtime_record_delete'),
    path('export-csv/', ExportCSV.as_view(), name='overtime_record_export_csv'),
]