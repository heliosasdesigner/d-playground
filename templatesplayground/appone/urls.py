from django.conf.urls import url

from appone import views


# Template Tagging
app_name = 'appone'
# referring to as far as like setting that namespace whenever you're going to be using templates tagging
# is set a variable name a global name called app_name and Django going to automatically look for this
# And then you need to set this equal to whatever the name of re-application is app name is equal to appone as a string.
# this is what's going to allow us to use that template tagging to actually tell Django 
# look under the basic app and then find that url you are all that matches.

urlpatterns =[
    url(r'relative/$',views.relative,name='relative'),
    url(r'other/$',views.other,name='other'),
]