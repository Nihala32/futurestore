# Generated by Django 4.0.6 on 2022-10-19 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_appointment_mobile_alter_doctors_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.specialities'),
        ),
    ]