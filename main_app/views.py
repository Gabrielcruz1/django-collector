from django.shortcuts import render

from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE

from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView 
from django.urls import reverse
from .models import Band


# class Album:
#     def __init__(self, band, title):
#         self.band = band 
#         self.title = title


# albums = [ 
#     Album("The Red Hot Chilli Peppers", "Stadium Arcadium"),
#     Album("Black Sabbath", "Iron Man"),
#     Album("Led Zeppelin", "Physical Graffiti"),
#     Album("Pink Floyd", "Wish You Were Here"),
#     Album("The Rolling Stones", "Tattoo You"),
#     Album("Sublime", "40 Oz. To Freedom"),
#     Album("Kings of Leon", "Mechanical Bull")

# ]

# Create your views here.

#UPDATED HOME CLASS TO EXTEND TEMPLATEVIEW
class Home(TemplateView):
    template_name = "home.html"

#UPDATED ABOUT CLASS TO EXTEND TEMPLATEVIEW
class About(TemplateView):
    template_name = "about.html"


class BandList(TemplateView):
    template_name = "band_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["bands"] = bands # this is where we add the key into our context object for the view to use
        name = self.request.GET.get("name")
        if name != None:
            context["bands"] = Band.objects.filter(name__icontains=name) # USING THE MODEL TO QUERY THE DATABASE
            context["header"] = f"Searching for {name}"
        else:
            context["bands"] = Band.objects.all()
            context["header"] = "Trending Bands"
        return context


#CRUD BELOW
class BandCreate(CreateView):
    model = Band
    fields = ['name', 'image', 'bio', 'verified_band']
    template_name = "band_create.html"
    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})

class BandDetail(DetailView):
    model = Band
    template_name = "band_detail.html"

class BandUpdate(UpdateView):
    model = Band
    fields = ['name', 'image', 'bio', 'verified_band']
    template_name = "band_update.html"
    def get_success_url(self):
        return reverse('band_detail', kwargs={'pk': self.object.pk})

class BandDelete(DeleteView):
    model = Band
    template_name = "band_delete_confirmation.html"
    success_url = "/bands/"




class AlbumList(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = albums
        return albums