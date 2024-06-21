import uuid

from django.db import models

# Create your models here.
from django.db import models


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    rating = models.IntegerField()
    name = models.TextField()
    site = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurants'
