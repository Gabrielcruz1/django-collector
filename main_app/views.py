from django.shortcuts import render

from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE

from django.views.generic.base import TemplateView



# Create your views here.

#UPDATED HOME CLASS TO EXTEND TEMPLATEVIEW
class Home(TemplateView):
    template_name = "home.html"


#UPDATED ABOUT CLASS TO EXTEND TEMPLATEVIEW
class About(TemplateView):
    template_name = "about.html"
