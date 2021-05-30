from django.db import models

class Lucknowbeds(models.Model):
    condition=models.CharField(max_length=200)
    centre=models.CharField(max_length=200)
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.number

    @staticmethod
    def get_all_beds():
        return Lucknowbeds.objects.all()