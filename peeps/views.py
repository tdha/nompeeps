from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nompeep, Reminder
from .forms import ReminderForm

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
    reminder_form = ReminderForm()
    return render(request, 'peeps/detail.html', {
        'peeps': peeps,
        'reminder_form': reminder_form
    })

def add_reminder(request, peeps_id):
    nompeep = get_object_or_404(Nompeep, id=peeps_id)

    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            new_reminder = form.save(commit=False)
            new_reminder.nompeep = nompeep  # Correctly associate the Reminder with the Nompeep instance
            new_reminder.save()
            return redirect('detail', peeps_id=peeps_id)
    return redirect('detail', peeps_id=peeps_id)

    # form = ReminderForm(request.POST)
    # if form.is_valid():
    #     new_reminder = form.save(commit=False)
    #     new_reminder.peeps_id = peeps_id
    #     new_reminder.save()
    # return redirect('detail', peeps_id=peeps_id)

class NompeepCreate(CreateView):
    model = Nompeep
    fields = '__all__'

class NompeepUpdate(UpdateView):
    model = Nompeep
    fields = '__all__'

class NompeepDelete(DeleteView):
    model = Nompeep
    success_url = '/peeps/'