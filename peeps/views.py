from django.shortcuts import render

peeps = [
  {'name': 'Jim', 'title': 'Lead instructor', 'nickname': 'Jimbo', 'age': 50},
  {'name': 'Laura', 'title': 'Associate instructor', 'nickname': 'Pez', 'age': 32},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def peeps_index(request):
    return render(request, 'peeps/index.html', {
        'peeps': peeps
    })