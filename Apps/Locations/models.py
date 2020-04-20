from django.db import models

# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=50)
    fullname_district_chief = models.CharField(max_length=50, default="District chief")

    def __str__(self):
        return f"{self.district}"

class Area(models.Model):
    area = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    fullname_area_chief = models.CharField(max_length=50, default="Area chief")

    def __str__(self):
        return f"{self.area}"


class City(models.Model):
    city = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fullname_city_chief = models.CharField(max_length=50, default="City chief")

    def __str__(self):
        return f"{self.city}"

class Province(models.Model):
    province = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    fullname_province_chief = models.CharField(max_length=50, default="Province chief")

    def __str__(self):
        return f"{self.province}"