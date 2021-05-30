from django.db import models

class LucknowArea(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_area():
        return LucknowArea.objects.all()