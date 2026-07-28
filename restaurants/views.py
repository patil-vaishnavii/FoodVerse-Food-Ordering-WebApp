from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
  restaurants = Restaurant.objects.all() # Takes every restaurant added to the database.

  # We pass that data to the template through this context dictionary.
  context = {
    "restaurants" : restaurants
  }

  return render(request,"restaurants/restaurant_list.html",context)

