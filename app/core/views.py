from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        data = {
            'user': request.user,
        }
        return render(request, 'core/logged_home.html', data)
    else:
        return render(request, 'core/home.html')