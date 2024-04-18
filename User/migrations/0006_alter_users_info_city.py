# Generated by Django 4.2 on 2024-03-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_delete_users_of_allopeyk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_info',
            name='city',
            field=models.CharField(choices=[('TEH', 'Tehran'), ('MHD', 'Mshhad'), ('ESF', 'Esfahan'), ('Urmo', 'Urmia')], max_length=10),
        ),
    ]