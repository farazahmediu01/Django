from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

        # widgets = {
        #     'body': forms.Textarea(attrs={'rows': 3}),
        # }


# Create your views here.
def create_view(request):
    if request.method == "POST":
        submitted_form = CreatePostForm(request.POST)
        if submitted_form.is_valid():
            # title = submitted_form.cleaned_data["title"]
            # author = submitted_form.cleaned_data["author"]
            # body = submitted_form.cleaned_data["body"]
            
            # data = Post(title=title, author=author, body=body)
            # data.save()

            data = submitted_form.save()

            # messages.success(request, "Post created successfully!")
            return render(request, "create.html", {"form": CreatePostForm(),"post_created":True})
            # return redirect(data.get_absolute_url())
        
            # return HttpResponseRedirect(reverse("home"))

        else:
            return render(request, "create.html",{
                "form": submitted_form
            })
        
    else:
        return render(request, "create.html", {
            "form": CreatePostForm()
    })


def home_view(request): # list_view
    posts = Post.objects.all() # Select all from Post
    
    return render(request, "home.html", {
        "post_list": posts,
    })


def detail_view(request, id):
    post = Post.objects.get(pk=id) #Select post that matches specific id

    return render(request, "detail.html",{
        "post": post,
    })


def fetch_delete_view(request, id):
    post = Post.objects.get(pk=id)
    
    return render(request, "delete.html", {
        "post": post,
    })


def delete_view(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
    # return HttpResponseRedirect( reverse("home") )


def fetch_update_view(request, id):
    post = Post.objects.get(pk=id)
    form = CreatePostForm(instance=post)
    return render(request, "update.html", {
        "form": form,
        "post": post,
    })

def update_view(request, id):
    post = Post.objects.get(pk=id)
    form = CreatePostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()

        return redirect(post.get_absolute_url())
    else:
        return render(request, "update.html",{
            "form": form,
            "post": post,
        })