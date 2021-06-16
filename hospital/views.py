# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login , logout , authenticate
from .forms import SignUpForm , ProfileForm, LoginForm , form_validation_error ,HospitalStuffForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile, HospitalStuff
from django.views import View
from django.contrib import messages
from django import template



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
                return redirect("/hospital/profile/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/loginhp.html", {"form": form, "msg": msg})


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

            msg = 'Hospital Profile created - please <a href="hospital/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/registerhp.html", {"form": form, "msg": msg, "success": success})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'hospital/profile.html', context)

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
        return redirect('hospital:hpprofile')

@method_decorator(login_required(login_url='login'), name='dispatch')
class HospitalStuffView(View):
    HStuff = None

    def dispatch(self, request, *args, **kwargs):
        self.HStuff, __ = HospitalStuff.objects.get_or_create(user=request.user)
        return super(HospitalStuffView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'stuff': self.HStuff}
        return render(request, 'hospital/HospitalStuff.html', context)

    def post(self, request):
        form = HospitalStuffForm(request.POST, request.FILES, instance=self.HStuff)

        if form.is_valid():
            
            HospitalStuff.VACANT_regural_beds = form.cleaned_data.get('first_name')
            HStuff = form.save()

            messages.success(request, 'Data is filled successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('hospital:HospitalStuff')

register = template.Library()
@register.filter
def subtract(value, arg):
    return value - arg
