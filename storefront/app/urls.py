from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main"),
    path('dotate/', views.dotation_page, name='dotations'),
    path('bump/<int:pk>', views.bump, name="bump"),
]