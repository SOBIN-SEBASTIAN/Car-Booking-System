from unicodedata import name
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('cars/',views.cars,name='cars'),
    path('contact/',views.contact,name='contact'),
    path('cartype/',views.cartype,name='cartype'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login")
]
