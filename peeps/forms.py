from django.forms import ModelForm
from .models import Reminder

class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ['thatdate', 'place', 'mentalnote']