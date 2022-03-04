from django.contrib import admin
from django.urls import path, include
from login import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
]