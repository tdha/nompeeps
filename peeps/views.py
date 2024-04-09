from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nompeep

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def peeps_index(request):
    peeps = Nompeep.objects.all()
    return render(request, 'peeps/index.html', {
        'peeps': peeps
    })

def peeps_detail(request, peeps_id):
    peeps = Nompeep.objects.get(id=peeps_id)
    return render(request, 'peeps/detail.html', {
        'peeps': peeps
    })

class NompeepCreate(CreateView):
    model = Nompeep
    fields = '__all__'

class NompeepUpdate(UpdateView):
    model = Nompeep
    fields = '__all__'

class NompeepDelete(DeleteView):
    model = Nompeep
    success_url = '/peeps/'