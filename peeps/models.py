from django.db import models # database name is nompeeps
from django.urls import reverse
from django.utils import timezone

from datetime import date, timedelta


class Group(models.Model):
    name = models.CharField(max_length=128)
    text_color = models.CharField(max_length=16, default='black')
    bg_color = models.CharField(max_length=16, default='yellow')

    def get_absolute_url(self):
        return reverse('groups_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f"Group '{self.name}'."
    
    class Meta:
        ordering = ['name']


class Nompeep(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    event = models.CharField(max_length=256, blank=True)
    notes = models.TextField(max_length=512, blank=True)
    groups = models.ManyToManyField(Group)

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'peeps_id': self.id })

    def __str__(self):
        if self.event:
            return self.name
        
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
        return f"Reminder re {self.nompeep} on {self.thatdate}."
    
    class Meta:
        ordering = ['-thatdate']
