from django.urls import path
from . import views

# ADD OUR ROUTES BELOW
# SIMILAR TO APP.USE() IN EXPRESS 
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/',views.About.as_view(), name="about"),
    path('bands/', views.BandList.as_view(), name="band_list")

]