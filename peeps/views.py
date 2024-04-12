from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Nompeep, Reminder, Group

from .forms import ReminderForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def peeps_index(request):
    peeps = Nompeep.objects.filter(user=request.user)
    return render(request, 'peeps/index.html', {
        'peeps': peeps
    })

@login_required
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

@login_required
def add_group(request, peeps_id, group_id):
    Nompeep.objects.get(id=peeps_id).groups.add(group_id)
    return redirect('detail', peeps_id=peeps_id)

@login_required
def remove_group(request, peeps_id, group_id):
    Nompeep.objects.get(id=peeps_id).groups.remove(group_id)
    return redirect('detail', peeps_id=peeps_id)

@login_required
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


class NompeepCreate(LoginRequiredMixin, CreateView):
    model = Nompeep
    fields = ['name', 'date', 'event', 'notes']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NompeepUpdate(LoginRequiredMixin, UpdateView):
    model = Nompeep
    fields = '__all__'

class NompeepDelete(LoginRequiredMixin, DeleteView):
    model = Nompeep
    success_url = '/peeps/'

# GROUP ################################

class GroupList(LoginRequiredMixin, ListView):
    model = Group
    fields = '__all__'

class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = '__all__'

class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = '__all__'

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups/'

# USER ##################################

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up. Please try again.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
