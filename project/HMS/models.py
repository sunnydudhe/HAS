from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Patient(models.Model):


    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15, blank=True, null=True )
    number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()