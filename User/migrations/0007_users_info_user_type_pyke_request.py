# Generated by Django 4.2 on 2024-03-08 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_users_info_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_info',
            name='user_type',
            field=models.CharField(choices=[('peyk', 'peyk'), ('person', 'person')], default='person', max_length=100),
        ),
        migrations.CreateModel(
            name='pyke_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.users_info')),
            ],
        ),
    ]
