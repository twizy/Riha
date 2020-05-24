from django.db import models
from django.contrib.auth.models import User
from Apps.Locations.models import *
from Apps.Cni.models import *
from Apps.Base.models import *
from django.utils import timezone

# Create your models here.

class CompleteIdentity(models.Model):
    beneficiary         = models.ForeignKey(User, on_delete=models.CASCADE,related_name='be')
    province            = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='provinc')
    city                = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cit')
    area                = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='are')
    date                = models.DateTimeField(default=timezone.now)
    payment_type        = models.ForeignKey(PaymentType, on_delete=models.CASCADE,related_name='pa')
    transaction_code    = models.CharField(max_length=20, default="1DF56HJ9JK8L6T")
    treated             = models.BooleanField(default=False)
    correct             = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.beneficiary}"

