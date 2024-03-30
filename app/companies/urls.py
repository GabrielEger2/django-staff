from django.urls import path
from .views import CompanyCreate, CompanyUpdate

urlpatterns = [
    path('create/', CompanyCreate.as_view(), name='company_create'),
    path('update/<int:pk>/', CompanyUpdate.as_view(), name='company_update'),
]