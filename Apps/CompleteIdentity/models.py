from django.db import models
from django.contrib.auth.models import User
from Apps.Locations.models import *
from Apps.Cni.models import *
from django.utils import timezone

# Create your models here.

class CompleteIdentity(models.Model):
    beneficiary         = models.ForeignKey(User, on_delete=models.CASCADE,related_name='be')
    area                = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='ar')
    birth_year          = models.IntegerField()
    date                = models.DateTimeField(default=timezone.now)
    transaction_code    = models.CharField(max_length=20, default="1DF56HJ9JK8L6T")
    
    def __str__(self):
        return f"{self.beneficiary}"

