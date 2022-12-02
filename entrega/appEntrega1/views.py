from distutils.log import info
from email import message
from django.shortcuts import render, HttpResponse
from appEntrega1.models import *
from django.template import loader
from appEntrega1.forms import *

# Create your views here.

def index(request):
    blogposts = BlogPost.objects.all()
    if blogposts:
        return render(request, 'index.html', {'blogposts':blogposts})
    else:
        return render(request, 'index.html')

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
            return render(request,"index.html")
    else:
        myForm=BlogPostForm()
    return render(request,'addblogpost.html', {'myForm':myForm})

    '''  def addnewteammember(request):
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
            return render(request,"index.html")
    else:
        myForm=BlogPostForm()
    return render(request,'addblogpost.html', {'myForm':myForm})'''

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
