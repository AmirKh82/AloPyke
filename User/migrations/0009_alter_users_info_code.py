# Generated by Django 4.2 on 2024-03-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_users_info_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_info',
            name='code',
            field=models.IntegerField(default=123),
        ),
    ]