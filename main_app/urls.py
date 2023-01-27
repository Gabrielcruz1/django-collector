from django.urls import path
from . import views

# ADD OUR ROUTES BELOW
# SIMILAR TO APP.USE() IN EXPRESS 
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/',views.About.as_view(), name="about"),
    path('bands/', views.BandList.as_view(), name="band_list"),
    path('albums/', views.AlbumList.as_view(), name="album_list"),
    #CREATE ROUTE BELOW
    path('bands/new/', views.BandCreate.as_view(), name="band_create"),
    #NEW ROUTE FOR DETAIL
    path('bands/<int:pk>/', views.BandDetail.as_view(), name="band_detail"),
    path('bands/<int:pk>/update', views.BandUpdate.as_view(), name="band_update")

]