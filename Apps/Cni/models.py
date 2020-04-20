from django.db import models
from django.contrib.auth.models import User
from Apps.Locations.models import *
# Create your models here.

class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=1)
    no_identity = models.CharField(max_length=20)
    given_place = models.CharField(max_length=20)
    birth_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="bp")
    birth_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="bc")
    birth_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="ba")
    birth_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="bd")
    birth_date = models.CharField(max_length=20)
    father_fullname = models.CharField(max_length=20)
    mother_fullname = models.CharField(max_length=20)
    profession = models.CharField(max_length=20, default="Sans")
    phone_number = models.CharField(max_length=20)
    matri_no = models.CharField(max_length=20)
    residence_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="pro")
    residence_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cit")
    residence_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="a",default="Ok")
    residence_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="dis")
    civil_state = models.CharField(max_length=100, default="Célibataire")
    nationality = models.CharField(max_length=100, default="Burundaise")

    def __str__(self):
        return f"{self.user}"

    class Meta:
       unique_together = ('user','no_identity','birth_province',)

