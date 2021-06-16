from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.staticfiles.templatetags.staticfiles import static

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="hp_profile", on_delete=models.CASCADE)
    hospital_name = models.CharField(blank=True , max_length=16)
    phone = models.CharField(max_length=32, null=True, blank=True)
    registration_number = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    verified = models.BooleanField(default=False)
    hospital_profile = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return self.user.username
  

class HospitalStuff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docter_name = models.CharField(blank=True , max_length=16)
    docter_details = models.TextField(blank=True , max_length=100)
    regural_beds = models.IntegerField(null=True, blank=True)    
    OCCUPIED_regural_beds= models.IntegerField(null=True, blank=True)
    VACANT_regural_beds= models.IntegerField(null=True, blank=True)
    oxygen_beds = models.IntegerField(null=True, blank=True)  
    OCCUPIED_oxygen_beds = models.IntegerField(null=True, blank=True)
    VACANT_oxygen_beds = models.IntegerField(null=True, blank=True)
    icu_beds = models.IntegerField(null=True, blank=True)    
    OCCUPIED_icu_beds = models.IntegerField(null=True, blank=True)
    VACANT_icu_beds = models.IntegerField(null=True, blank=True)
    covid_lab = models.BooleanField(default=False)
    vaccine = models.BooleanField(default=False)
    total_vaccine_slot = models.IntegerField(null=True, blank=True)    
    OCCUPIED_vaccine_slot = models.IntegerField(null=True, blank=True)
    VACANT_vaccine_slot = models.IntegerField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('HospitalStuff')
        verbose_name_plural = _('HospitalStuffs')

    def __str__(self):
        return self.user.username