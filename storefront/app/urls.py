from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page),
    path('test_page/', views.second_page, name='test_page')
]