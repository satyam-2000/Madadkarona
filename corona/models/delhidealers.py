from django.db import models
from corona.models.delhiarea import DelhiArea

class DelhiDealer(models.Model):
    area= models.ForeignKey(DelhiArea,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    @staticmethod
    def get_all_dealers():
        return DelhiDealer.objects.all()
    @staticmethod
    def get_dealers_byarea(area_id):
        if area_id:
            return DelhiDealer.objects.filter(area=area_id)
        
        else:
            return DelhiDealer.get_all_dealers()
