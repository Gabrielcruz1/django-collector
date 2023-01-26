from django.shortcuts import render

from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE

from django.views.generic.base import TemplateView



# Create your views here.

#UPDATED HOME CLASS TO EXTEND TEMPLATEVIEW
class Home(TemplateView):
    template_name = "home.html"


# class About(View):

#     def get(self, request):
#         return HttpResponse("Band Collector About")