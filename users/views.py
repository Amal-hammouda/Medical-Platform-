from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm

# --------------------------

# --------------------------
def home(request):

    if request.user.is_authenticated:
        if request.user.user_type == "doctor":
            return redirect("doctor_dashboard")
        else:
            return redirect("patient_dashboard")

    return render(request, "users/home.html")

# --------------------------
# Signup
# --------------------------
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})

# --------------------------
# Login
# --------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            if user.user_type == "doctor":
                return redirect("doctor_dashboard")
            else:
                return redirect("patient_dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

# --------------------------
# Logout
# --------------------------
def logout_view(request):
    auth_logout(request)
    return redirect("login")

# --------------------------

# --------------------------
def is_doctor(user):
    return user.user_type == "doctor"

def is_patient(user):
    return user.user_type == "patient"

# --------------------------
# Doctor Dashboard
# --------------------------
@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    return render(request, "users/doctor_dashboard.html", {"user": request.user})

# --------------------------
# Patient Dashboard
# --------------------------
@login_required
@user_passes_test(is_patient)
def patient_dashboard(request):
    return render(request, "users/patient_dashboard.html", {"user": request.user})


