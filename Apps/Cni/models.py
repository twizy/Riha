from django.db import models
from django.contrib.auth.models import User
from Apps.Locations.models import *
# Create your models here.

class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=1,default="M")
    no_identity = models.CharField(max_length=100,default="Vide")
    given_place = models.CharField(max_length=100,default="Vide")
    given_date = models.CharField(max_length=10,default="00/00/0000")
    birth_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="bp",blank=True,null=True)
    birth_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="bc",blank=True,null=True)
    birth_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="ba",blank=True,null=True)
    birth_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="bd",blank=True,null=True)
    birth_date = models.CharField(max_length=100,default="Vide")
    father_fullname = models.CharField(max_length=100,default="Vide")
    mother_fullname = models.CharField(max_length=100,default="Vide")
    profession = models.CharField(max_length=100, default="Sans")
    phone_number = models.CharField(max_length=100,default="Vide")
    matri_no = models.CharField(max_length=100,default="Vide")
    residence_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="rp",blank=True,null=True)
    residence_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="rc",blank=True,null=True)
    residence_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="ra",blank=True,null=True)
    residence_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="rd",blank=True,null=True)
    civil_state = models.CharField(max_length=100, default="Célibataire")
    nationality = models.CharField(max_length=100, default="Burundaise")
    staff_member = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"

    class Meta:
       unique_together = ('user','no_identity','birth_date','nationality')
