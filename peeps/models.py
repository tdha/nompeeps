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
            return f"Met {self.name} at {self.event} on {self.date}."
        else:
            return f"Met {self.name} on {self.date}."