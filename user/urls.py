
from django.urls import path
from .views import login_view, register_user,ProfileView,RegularView,OxygenView,IcuView,VaccineView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('regular_beds/', RegularView, name='regular'),
    path('oxygen_beds/', OxygenView, name='oxygen'),
    path('icu_beds/', IcuView, name='icu'),
    path('vaccine_slots/', VaccineView, name='vaccine')
]
