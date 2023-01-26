from django.shortcuts import render
from django.views import View #VIEW CLASS HANDLES REQUESTS
from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):

    # Here we are adding a method that will be ran when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Band Collecter Home")