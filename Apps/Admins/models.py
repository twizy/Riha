from django.db import models
from django.contrib.auth.models import User
from Apps.Locations.models import *

# Create your models here.
class AdminiUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    is_city_admin = models.BooleanField(default=False)
    is_area_admin = models.BooleanField(default=False)
    is_district_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"