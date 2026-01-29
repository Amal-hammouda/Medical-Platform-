from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.status = "pending"
            appointment.save()
            return redirect("patient_dashboard")
    else:
        form = AppointmentForm()
    return render(request, "appointments/book.html", {"form": form})


@login_required
def doctor_appointments(request):
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, "appointments/doctor_appointments.html", {"appointments": appointments})


@login_required
def approve_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.status = "approved"
    appointment.save()
    return redirect("doctor_appointments")


@login_required
def reject_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.status = "rejected"
    appointment.save()
    return redirect("doctor_appointments")
