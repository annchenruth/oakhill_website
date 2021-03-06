"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from website.forms import LoginForm
from django.contrib.auth.views import login, logout
from .staticserve import serve

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'),name="home"),    
    path('about/', TemplateView.as_view(template_name='about.html'),name="about"),    
    path('faqs/', TemplateView.as_view(template_name='FAQs.html'),name="faqs"),    
    path('admin/', admin.site.urls),
    path('contact/', include('contacts.urls')),
    path('rental/', include('rental.urls')),  
    path('login/', login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login'), # not sure why i had to remove name='login' here???
    path('logout/', logout, name='logout'),   
    re_path(r'^static/(?P<path>.*)$', serve),
]
