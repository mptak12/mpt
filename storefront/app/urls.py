from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main"),
    path('donate/', views.dotation_page, name='donations'),
    path('bump/<int:pk>', views.bump, name="bump"),
]