# Generated by Django 4.2 on 2024-03-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_alter_users_info_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyke_request',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]