# Generated by Django 4.2 on 2024-04-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_alter_users_info_code_alter_users_info_personal_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyke_request',
            name='motor_type',
            field=models.CharField(choices=[('C50', 'C50'), ('BM', 'BMW'), ('HU', 'HIUNDA'), ('H2', 'HUNDA'), ('KH', 'KHAVTR')], default='C50', max_length=10),
        ),
        migrations.AlterField(
            model_name='users_info',
            name='user_type',
            field=models.CharField(choices=[('person', 'person'), ('peyk', 'peyk')], default='person', max_length=10),
        ),
    ]
