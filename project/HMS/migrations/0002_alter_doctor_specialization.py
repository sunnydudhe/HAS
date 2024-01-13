# Generated by Django 4.2.4 on 2023-12-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('General', 'General'), ('Dentist', 'Dentist'), ('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Neurologist', 'Neurologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Orthopedician', 'Orthopedician')], max_length=15),
        ),
    ]
