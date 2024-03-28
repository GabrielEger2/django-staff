from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.employees.models import Employee

@login_required
def home(request):
    data = {
        'user': request.user,
    }
    return render(request, 'core/index.html', data)