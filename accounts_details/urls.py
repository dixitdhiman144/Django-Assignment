from django.urls import path
from . import views


urlpatterns = [
    path('create-customer/',views.create_customer, name="create customer"),
    #path('login', views.login, name="login"),
    #path('logout', views.logout, name="logout" )
]