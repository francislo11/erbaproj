from django.db import models
from datetime import datetime

# Create datebase records here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(default=True, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
