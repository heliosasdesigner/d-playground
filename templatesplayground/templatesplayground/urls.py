"""templatesplayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url ,include

from appone import views


urlpatterns = [
    url(r'^$',views.index,name='index'),  # r'^$' mean nothing, so when user landed on domain, will go to views.index = index.html
    
		url(r'^appone/',include('appone.urls')),
    # ^ symbols anything before that slash appone and then the name of the actual page 
    #   or the view such as appone slash relative or appone Other appone flash etc. 
    #   then we tell it OK go to the appone Urls page for the subsequent views to show 
    #   or the subsequent mapping of the Urls which means we come over here to our appone right
    path('admin/', admin.site.urls),
]