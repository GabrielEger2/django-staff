from django.urls import path
from .views import CompanyCreate

urlpatterns = [
    path('create/', CompanyCreate.as_view(), name='company_create'),
]