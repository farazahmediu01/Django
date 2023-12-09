from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import AbstractUser


class Room(models.Model):
    ROOM_STATUS = [
        (1, "Available"),
        (0, "Booked"),
    ]
    name = models.CharField(max_length=100)
    status = models.IntegerField(max_length=1, choices=ROOM_STATUS, default=1)  # e.g., 'available', 'booked'
    details = models.TextField()
    price  = models.FloatField()
    # Catagory = models.CharField() # Single-Room, luxury-Room, Double-Room, dulux-room

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10)  # e.g., 'confirmed', 'cancelled'
    amount = models.CharField(max_length=10)

class Feedback(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                              MaxValueValidator(5)])  # e.g., 1 to 5