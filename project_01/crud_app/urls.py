from django.urls import path
from crud_app import views


urlpatterns = [
    path("<str:id>/detail", views.detail_view, name="post_detail"),
    path("create/", views.create, name="post_new"),
    path("", views.home, name="home"),
]
