from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nompeep, Reminder, Group
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
    current_groups_ids = peeps.groups.all().values_list('id')
    available_groups = Group.objects.exclude(id__in=current_groups_ids)
    reminder_form = ReminderForm()
    return render(request, 'peeps/detail.html', {
        'peeps': peeps,
        'reminder_form': reminder_form,
        'available_groups': available_groups
    })

def add_group(request, peeps_id, group_id):
    Nompeep.objects.get(id=peeps_id).groups.add(group_id)
    return redirect('detail', peeps_id=peeps_id)

def remove_group(request, peeps_id, group_id):
    Nompeep.objects.get(id=peeps_id).groups.remove(group_id)
    return redirect('detail', peeps_id=peeps_id)

def add_reminder(request, peeps_id):
    nompeep = get_object_or_404(Nompeep, id=peeps_id)

    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            new_reminder = form.save(commit=False)
            new_reminder.nompeep = nompeep 
            new_reminder.save()
            return redirect('detail', peeps_id=peeps_id)
    return redirect('detail', peeps_id=peeps_id)


class NompeepCreate(CreateView):
    model = Nompeep
    fields = ['name', 'date', 'event', 'notes']

class NompeepUpdate(UpdateView):
    model = Nompeep
    fields = '__all__'

class NompeepDelete(DeleteView):
    model = Nompeep
    success_url = '/peeps/'

# GROUP ################################

class GroupList(ListView):
    model = Group
    fields = '__all__'

class GroupDetail(DetailView):
    model = Group

class GroupCreate(CreateView):
    model = Group
    fields = '__all__'

class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'

class GroupDelete(DeleteView):
    model = Group
    success_url = '/groups/'