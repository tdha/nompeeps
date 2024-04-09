from django.db import models # database name is nompeeps
from django.urls import reverse

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
        

class Reminder(models.Model):
    thatdate = models.DateField('Reminder date')
    place = models.CharField(max_length=128)
    mentalnote = models.TextField('Mental note', max_length=512)

    nompeep = models.ForeignKey(Nompeep, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reminder that on {self.thatdate} at {self.place}, re {self.nompeep}"
    
    class Meta:
        ordering = ['-thatdate']