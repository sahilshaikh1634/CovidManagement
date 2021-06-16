from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login , logout , authenticate
from .forms import SignUpForm , ProfileForm, LoginForm, form_validation_error
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from django.views import View
from django.contrib import messages
from hospital.models import Profile as hp_profile,HospitalStuff

def home(request):
    return render(request, 'user/home.html')

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/user/profile/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})




@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'user/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')

@login_required(login_url='login')
def RegularView(request):
    hospital = hp_profile.objects.filter(verified=True)
    
    bed = HospitalStuff.objects.all()
    return render(request, 'user/regular_beds.html', { 'hospitals' : hospital , 'beds' : bed, 'segment' : 'regular' })

@login_required(login_url='login')
def OxygenView(request):
    hospital = hp_profile.objects.filter(verified=True)
    
    bed = HospitalStuff.objects.all()
    return render(request, 'user/oxygen_beds.html', { 'hospitals' : hospital , 'beds' : bed, 'segment' : 'oxygen' })

@login_required(login_url='login')
def IcuView(request):
    hospital = hp_profile.objects.filter(verified=True)
    
    bed = HospitalStuff.objects.all()
    return render(request, 'user/icu_beds.html', { 'hospitals' : hospital , 'beds' : bed, 'segment' : 'icu' })

@login_required(login_url='login')
def VaccineView(request):
    hospital = hp_profile.objects.filter(verified=True)
    
    vaccine = HospitalStuff.objects.all()
    return render(request, 'user/vaccine_slots.html', { 'hospitals' : hospital , 'vaccines' : vaccine , 'segment' : 'vaccine' })
