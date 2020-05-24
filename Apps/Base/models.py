from django.db import models

# Create your models here.
class PaymentType(models.Model):
    payment_type = models.CharField(max_length=20, default="EcoCash")
    
    def __str__(self):
        return f"{self.payment_type}"

# class NumberOrder(models.Model):
#     numero = models.CharField(max_length=1000)

#     def __str__(self):
#         return f"{self.numero}"