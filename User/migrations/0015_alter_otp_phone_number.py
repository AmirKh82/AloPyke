# Generated by Django 4.2 on 2024-04-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]