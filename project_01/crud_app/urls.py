from django.urls import path
from crud_app import views


urlpatterns = [
    path("<str:id>/detail", views.detail_view, name="detail_view"),
    path("", views.home, name="home"),
]