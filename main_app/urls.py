from django.urls import path
from . import views

# ADD OUR ROUTES BELOW
# SIMILAR TO APP.USE() IN EXPRESS 
urlpatterns = [
    path('', views.Home.as_view(), name="home")

]