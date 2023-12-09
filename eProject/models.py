from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # Assuming 'type' is either 'guest', 'registered', or 'admin'
#     type = models.CharField(max_length=10)

class Room(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)  # e.g., 'available', 'booked'
    details = models.TextField()
    price  = models.FloatField()
    Catagory = # Single-Room, luxury-Room, Double-Room, dulux-room

class Booking(models.Model):
    user = models.ForeignKey("authUser", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10)  # e.g., 'confirmed', 'cancelled'
    amount = models.CharField(max_length=10)

class Feedback(models.Model):
    user = models.ForeignKey("authUser", on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()  # e.g., 1 to 5