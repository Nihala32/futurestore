# Generated by Django 4.0.6 on 2022-10-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_alter_doctors_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='user',
        ),
    ]
