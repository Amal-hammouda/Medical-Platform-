from django import forms
from .models import Appointment
from django.contrib.auth import get_user_model

User = get_user_model()

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=User.objects.filter(user_type="doctor"),
        label="Choisir un médecin"
    )

    class Meta:
        model = Appointment
        fields = ["doctor", "date", "time"]
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'Select a date'
            })
        }

