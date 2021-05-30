from django.db import models

class DelhiArea(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_area():
        return DelhiArea.objects.all()