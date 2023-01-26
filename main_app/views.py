from django.shortcuts import render
from django.views import View #VIEW CLASS HANDLES REQUESTS
from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE


# Create your views here.

#  class Home - extending it from View class
class Home(View):

    # method that will be ran when dealing with a GET request
    def get(self, request):
        # returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Band Collecter Home")


class About(View):

    def get(self, request):
        return HttpResponse("Band Collector About")