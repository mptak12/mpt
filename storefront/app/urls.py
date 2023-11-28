from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main"),
    path('test_page/', views.second_page, name='test_page'),
    path('bump/<int:pk>', views.bump, name="bump"),
]