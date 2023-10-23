from django.urls import path
from . import views


urlpatterns = [
    path('first/', views.say_sth)
]