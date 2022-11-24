from django.contrib import admin
from django.urls import path,include
from zekrinapp import views

urlpatt = [
    path("",views.index),
    path("about",views.about),
    path("contacts",views.contacts)
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlpatt))
]

