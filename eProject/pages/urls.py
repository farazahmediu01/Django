from django.urls import path
from .views import RoomListView, RoomDetailView

urlpatterns = [
    path("home/", RoomListView.as_view(), name="room_list"),
    path("room/<str:pk>", RoomDetailView.as_view(), name="room_detail"),
]