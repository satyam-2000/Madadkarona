from django.db import models
from corona.models.lucknowarea import LucknowArea

class LucknowDealer(models.Model):
    area= models.ForeignKey(LucknowArea,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_dealers():
        return LucknowDealer.objects.all()

    @staticmethod
    def get_dealers_byarea(area_id):
        if area_id:
            return LucknowDealer.objects.filter(area=area_id)
        
        else:
            return LucknowDealer.get_all_dealers()
