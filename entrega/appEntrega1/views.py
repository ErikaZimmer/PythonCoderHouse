from distutils.log import info
from email import message
from django.shortcuts import render, HttpResponse
from appEntrega1.models import *
from django.template import loader
from appEntrega1.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    blogposts = BlogPost.objects.all()
    if blogposts:
        return render(request, 'index.html', {'blogposts':blogposts})
    else:
        return render(request, 'index.html', {'message':"Sorry! We dont have any post."})


def about(request):
    teammembers = TeamMember.objects.all()
    if teammembers:
        return render(request, 'about.html', {'teammembers':teammembers})
    else:
        return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        myForm = ContactMessageForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            name=info['name']
            lastname=info['lastname']
            message=info['message']
            contactmessage = ContactMessage(name=name,lastname=lastname,message=message)
            contactmessage.save()
            return render(request,"contact.html")
    else:
        myForm=ContactMessageForm()
    return render(request,'contact.html', {'myForm':myForm})


def blogpost(request):
    return HttpResponse("Blog Post")

@login_required
def addblogpost(request):
    if request.method == 'POST':
        myForm = BlogPostForm(request.POST)
        if myForm.is_valid():
            info = myForm.cleaned_data
            title=info['title']
            subtitle=info['subtitle']
            content=info['content']
            category=info['category']
            blogpost = BlogPost(title=title, subtitle=subtitle, content=content, category=category)
            blogpost.save()
            return render(request,"index.html", {'message': "New post were added"})
    else:
        myForm=BlogPostForm()
    return render(request,'addblogpost.html', {'myForm':myForm})


def searchpostsite(request):
    return render(request, 'searchpostsite.html')


def searchpost(request):
    if request.GET['title']:
        title = request.GET['title']
        blogposts = BlogPost.objects.filter(title__contains=title)
        return render(request, 'blogpost.html', {'blogposts':blogposts})
    else:
        response = "No information added"
    return HttpResponse(response)

@login_required
def deletepost(request, post_id):
    blogpost = BlogPost.objects.get(id=post_id)
    blogpost.delete()

    blogpost = BlogPost.objects.all()
    blogposts = {'blogpost':blogpost}
    if blogposts:
        return render(request, 'index.html', blogposts, {'message':"The post has been deleted."})
    else:
        return render(request, 'index.html', {'message':"Sorry! We dont have any post."})


def register (request):
    if request.method == 'POST':
        myForm = UserRegisterForm(request.POST)
        if myForm.is_valid():

            username=myForm.cleaned_data['username']
            myForm.save()
            return render(request,"index.html", {"message":"El nuevo usuario fue creado exitosamente!"})
    else:
        myForm=UserRegisterForm()
    return render(request,'register.html', {'myForm':myForm})
   

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)
                return render (request, 'index.html', {'message':f"Bienvenido {usuario}!!"})
            else:
                return render (request, 'index.html', {'message':"Ups, datos incorrectos."})
        else:
            return render (request, 'index.html', {'message':"Error, formulario incorrecto."})
    
    form = AuthenticationForm()
    return render (request, 'login.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')