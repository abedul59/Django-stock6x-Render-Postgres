"""firstproject URL Configuration

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
from django.urls import path, include, re_path
from myapp import views
from django.conf.urls import url



urlpatterns = [
	    path('admin/', admin.site.urls),
	    #path('', include('config.urls')),
            #path('callback/', views.callback),
            #re_path('^callback', views.callback),
        path('index3/', views.index3),
        path('', views.index),
        path('stock6x/', views.stock6x),
        path('stockPERsegx/', views.stockPERsegx),

        path('index2/', views.index2),
        path('login2/', views.login2),
        path('logout2/', views.logout2),
        path('adduser/', views.adduser),
        path('signup/', views.signup),

        path('login3/', views.login3),    
        path('logout3/', views.logout3),
        path('index/', views.index),
        path('login/', views.login),
        path('logout/', views.logout),

        path('stock6xAdmin/', views.stock6xAdmin),

        path('stock6listall202404/', views.stock6listall202404),
        path('stock6listall202404score/', views.stock6listall202404score),

        path('adminmain/', views.adminmain),

	]



