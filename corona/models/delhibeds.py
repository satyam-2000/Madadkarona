from django.db import models

class Delhibeds(models.Model):
    Hospital=models.CharField(max_length=200)
    Type=models.CharField(max_length=200)
    Total=models.CharField(max_length=200)
    Vacant=models.CharField(max_length=200,default=1)

    def __str__(self):
        return self.Hospital

    @staticmethod
    def get_all_beds():
        return Delhibeds.objects.all()