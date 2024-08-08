from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_location = models.CharField(max_length=100, blank=True, null=True)
    TEMPERATURE_UNIT_CHOICES = [
        ('C', 'Celsius'),
        ('F', 'Fahrenheit'),
    ]
    preferred_temperature_unit = models.CharField(max_length=1, choices=TEMPERATURE_UNIT_CHOICES, default='C')

    def __str__(self):
        return self.user.username
