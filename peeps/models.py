from django.db import models # database name is nompeeps
from django.urls import reverse
from django.utils import timezone

from datetime import date, timedelta


class Nompeep(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    event = models.CharField(max_length=256, blank=True)
    notes = models.TextField(max_length=512, blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'peeps_id': self.id })

    def __str__(self):
        if self.event:
            return f"{self.name} from {self.event} back on {self.date}."
        else:
            return f"{self.name} back on {self.date}."
        
    def contact_since(self, days=30):
        today = timezone.now().date()

        if (today - self.date).days <= days:
            return False 
        
        latest_reminder = self.reminder_set.order_by('-thatdate').first()
        if latest_reminder and (today - latest_reminder.thatdate).days <= days:
            return False 
        
        return True

class Reminder(models.Model):
    thatdate = models.DateField('Reminder date')
    place = models.CharField(max_length=128)
    mentalnote = models.TextField('Mental note', max_length=512)

    nompeep = models.ForeignKey(Nompeep, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reminder that on {self.thatdate} at {self.place}, re {self.nompeep}"
    
    class Meta:
        ordering = ['-thatdate']