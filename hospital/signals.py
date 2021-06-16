from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile,HospitalStuff


@receiver(post_save, sender=User, dispatch_uid='save_new_hospital_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_hospital_data')
def save_data(sender, instance, created, **kwargs):
    if created:
        HStuff = HospitalStuff(user=instance)
        HStuff.save()
