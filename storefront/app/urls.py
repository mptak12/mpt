from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main"),
    path('donate/', views.dotation_page, name="donations"),
    path('aboutUs/', views.about_us, name="us"),
    path('auctions/', views.auctions, name="auctions"),
    path('login/', views.login, name="userLogin"),
    #path('bump/<int:pk>', views.bump, name="bump"),

]