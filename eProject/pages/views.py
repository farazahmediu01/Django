from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Room



# Create your views here.
class RoomListView(ListView):
    model = Room     # room_list
    template_name = "home.html"

class RoomDetailView(DetailView):
    model = Room     # room_list
    template_name = "detail.html"