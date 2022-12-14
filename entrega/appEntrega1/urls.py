from django.urls import path

from appEntrega1 import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('about', views.about, name="About"),
    path('contact', views.contact, name="Contact"),
    path('blogpost', views.blogpost, name="Blogpost"),
    path('addblogpost', views.addblogpost, name="AddBlogPost"),
    path('searchpost', views.searchpost, name="SearchPost"),
    path('searchpostsite', views.searchpostsite, name="SearchPostSite"),
]