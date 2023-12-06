from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from crud_app.models import Post



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }



# Create your views here.
def create(request):
    if request.method == "POST":
        submitted_form = CreatePostForm(request.POST)
        if submitted_form.is_valid():
            title = submitted_form.cleaned_data["title"]
            author = submitted_form.cleaned_data["author"]
            body = submitted_form.cleaned_data["body"]
            
            data = Post(title=title, author=author, body=body)
            data.save()

            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "create.html",{
                "form": submitted_form
            })
        
    else:
        return render(request, "create.html", {
            "form": CreatePostForm()
    })



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

