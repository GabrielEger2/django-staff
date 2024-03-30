from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('app.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('employees/', include('app.employees.urls')),
    path('companies/', include('app.companies.urls')),
    path('departments/', include('app.departments.urls')),
    path('documents/', include('app.documents.urls')),
]
