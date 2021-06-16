from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),  # Django admin route
    path("", include("app.urls")),  # UI Kits Html files 
    path("hospital/", include("hospital.urls")),  # Django hospital route
    path('user/', include("user.urls")),  # Django user route  
]

if settings.DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)