# Generated by Django 3.2.2 on 2021-05-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0002_dealer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
