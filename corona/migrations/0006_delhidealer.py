# Generated by Django 3.2.2 on 2021-05-18 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0005_delhiarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelhiDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('area', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='corona.delhiarea')),
            ],
        ),
    ]
