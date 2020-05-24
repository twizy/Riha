from django.db import models

# Create your models here.

class Province(models.Model):
    province = models.CharField(max_length=50)
    fullname_province_chief = models.CharField(max_length=50, default="Province chief")

    def __str__(self):
        return f"{self.province}"

    class Meta:
       unique_together = ('province',)

class City(models.Model):
    city = models.CharField(max_length=50)
    fullname_city_chief = models.CharField(max_length=50, default="City chief")
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}"

    class Meta:
       unique_together = ('province','city',)


class Area(models.Model):
    area = models.CharField(max_length=50)
    fullname_area_chief = models.CharField(max_length=50, default="Area chief")
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.area}"

    class Meta:
       unique_together = ('area','city',)

class District(models.Model):
    district = models.CharField(max_length=50)
    fullname_district_chief = models.CharField(max_length=50, default="District chief")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.district}"

    class Meta:
       unique_together = ('area','district',)

class Testing(models.Model):
    testing = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.testing}"
