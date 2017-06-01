"""hexedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^apply$', views.apply),
    url(r'^information$', views.information),
    url(r'^information/1$', views.information_detail),
    url(r'^guidance$', views.guidance),
    url(r'^tour$', views.tour),
    url(r'^certification$', views.certification),
    url(r'^live$', views.live),
    url(r'^eb$', views.EB),
    url(r'^eb3$', views.EB3),
    url(r'^usa$', views.usa),
    url(r'^ca$', views.ca),
    url(r'^europe$', views.europe),
    url(r'^asia', views.asia),
    url(r'^profession', views.profession),
    url(r'^about', views.about),
    url(r'^cooperate', views.cooperate),
    url(r'^elite', views.elite),
    url(r'^contact', views.contact),
]
