from django.urls import path
from .views import DocumentCreate

urlpatterns = [
    path('create/<int:employee_id>', DocumentCreate.as_view(), name='document_create'),
]

