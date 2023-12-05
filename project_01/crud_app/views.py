from django.shortcuts import render
from crud_app.models import Post


# Create your views here.
def home(request):
    post_list = Post.objects.all() # Select all from Post
    
    return render(request, "home.html", {
        "post_list": post_list,
    })

def detail_view(request, id):
    post = Post.objects.get(pk=id) #Select post that matches specific id
    
    return render(request, "detail.html",{
        "post": post,
    })