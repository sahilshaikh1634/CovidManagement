from django.urls import path, include
from .views import login_view,register_user,ProfileView,HospitalStuffView
from django.contrib.auth.views import LogoutView
from . import views
app_name='hospital'

urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name='hpprofile'),
    path('hospitaldata/', HospitalStuffView.as_view(), name='HospitalStuff')
]