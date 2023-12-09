from django.contrib import admin

from pages.models import Room, Booking, Feedback


# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Feedback)