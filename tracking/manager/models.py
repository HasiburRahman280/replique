from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Device(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status_choices = (
        ('available', 'Available'),
        ('checked_out', 'Checked Out'),
        ('damaged', 'Damaged'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='available')
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_from = models.DateTimeField(default=timezone.now)
    assigned_until = models.DateTimeField(null=True, blank=True)
    condition_choices = (
        ('new', 'New'),
        ('used', 'Used'),
        ('damaged', 'Damaged'),
    )
    condition = models.CharField(max_length=20, choices=condition_choices, default='new')


    def __str__(self):
        return f"{self.name}"