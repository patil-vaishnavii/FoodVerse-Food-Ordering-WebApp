from django.db import models

class Restaurant(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  address = models.TextField()
  image = models.ImageField(upload_to="restaurants/")
  rating = models.DecimalField(max_digits=3,decimal_places=1)

  def __str__(self):
    return self.name

# add these models in admin.py if using admin panel

class MenuItem(models.Model):
  restaurant = models.ForeignKey(
    Restaurant,
    on_delete=models.CASCADE
  )

  name = models.CharField(max_length=100)

  price = models.IntegerField()

  def __str__(self):
    return self.name