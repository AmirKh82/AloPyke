# Generated by Django 4.2 on 2024-03-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_info',
            name='destination',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='orders_info',
            name='origin',
            field=models.CharField(max_length=150),
        ),
    ]