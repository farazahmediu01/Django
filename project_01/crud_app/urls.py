from django.urls import path
from crud_app import views


urlpatterns = [
    path("detail/<str:id>", views.detail_view,      name="post_detail"),
    path("delete/<str:id>", views.delete_view,      name="post_delete"),
    path("fetch/<str:id>",  views.fetch_view,       name="post_fetch"),
    path("update/<str:id>", views.update_view,      name="post_update"),
    path("create/",         views.create_view,      name="post_new"),
    path("",                views.home_view,        name="home"),
]
