# Generated by Django 4.2 on 2024-04-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_orders_info_duration_orders_info_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_info',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('peyk_accepted', 'peyk_accepted')], default='pending', max_length=20),
        ),
    ]