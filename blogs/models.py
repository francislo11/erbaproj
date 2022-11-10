from django.db import models
from datetime import datetime

# Provides data from the database as an Object Relational Mapping (ORM)


class Listing(models.Model):
    title = models.CharField(max_length=200, blank=False)
    sub_title = models.CharField(max_length=250, blank=False, default=True)
    desciption = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # show title as database displace within admin

    def __str__(self):
        return self.title
