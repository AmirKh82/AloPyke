# Generated by Django 4.2 on 2024-04-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_rename_person_orders_info_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_info',
            name='duration',
            field=models.TimeField(default=20),
        ),
        migrations.AddField(
            model_name='orders_info',
            name='price',
            field=models.CharField(default=20, max_length=15),
        ),
    ]
