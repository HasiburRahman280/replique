from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=200, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
