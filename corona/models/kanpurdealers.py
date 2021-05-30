from django.db import models


class KanpurDealer(models.Model):
    
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    @staticmethod
    def get_all_dealers():
        return KanpurDealer.objects.all()
