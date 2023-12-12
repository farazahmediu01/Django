from django.urls import path
from crud_app import views


urlpatterns = [
    path("detail/<str:id>",    views.detail_view,           name="post_detail"),
    path("todelete/<str:id>",  views.fetch_delete_view,     name="post_delete"),
    path("delete/<str:id>",    views.delete_view,           name="delete"),
    path("toupdate/<str:id>",  views.fetch_update_view,     name="post_update"),
    path("update/<str:id>",    views.update_view,           name="update"),
    path("create/",            views.create_view,           name="post_new"),
    path("",                   views.home_view,             name="home"),
]
