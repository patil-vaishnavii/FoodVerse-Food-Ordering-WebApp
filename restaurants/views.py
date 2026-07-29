from django.shortcuts import render,get_object_or_404
from .models import Restaurant

def restaurant_list(request):
  restaurants = Restaurant.objects.all() # Takes every restaurant added to the database.

  # We pass that data to the template through this context dictionary.
  context = {
    "restaurants" : restaurants
  }

  return render(request,"restaurants/restaurant_list.html",context)


def restaurant_detail(request,id):

  restaurant = get_object_or_404(
    Restaurant,
    id=id
  )

  menu_items = restaurant.menuitem_set.all()
  return render(
    request,'restaurants/restaurant_detail.html',
    {
      'restaurant': restaurant,
      'menu_items': menu_items,
    }
  )