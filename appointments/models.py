from django.db import models
from users.models import CustomUser

class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="pending")  # pending / approved / rejected

    def __str__(self):
        return f"{self.patient} → {self.doctor} ({self.status})"




