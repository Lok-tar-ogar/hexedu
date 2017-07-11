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
    url(r'^detail$', views.app_detail),

    url(r'^information$', views.information),
    url(r'^information/(?P<fid>\d+)$', views.information_detail),
    url(r'^guidance$', views.guidance),
    url(r'^tour$', views.tour),
    url(r'^certification$', views.certification),
    url(r'^live$', views.live),

    url(r'^eb$', views.EB),
    url(r'^eb3$', views.EB3),
    url(r'^eb5$', views.EB5),

    url(r'^resume', views.resume),
    url(r'^personnel$', views.personnel),
    url(r'^train$', views.train),


    url(r'^usa$', views.usa),
    url(r'^ca$', views.ca),
    url(r'^europe$', views.europe),
    url(r'^asia$', views.asia),

    url(r'^profession$', views.profession),
    url(r'^about$', views.about),
    url(r'^cooperate$', views.cooperate),
    url(r'^elite$', views.elite),
    url(r'^contact$', views.contact),
    url(r'^develop$', views.develop),

    url(r'^car$', views.car),
    url(r'^housekeep$', views.housekeep),
    url(r'^settle$', views.settle),

    url(r'^message$', views.message),

    url(r'^Pennsylvania$', views.upenn),
    url(r'^Denver$', views.Denver),
    url(r'^CA$', views.CA),
    url(r'^Columbia$', views.Columbia),
    url(r'^Harvard$', views.Harvard),
    url(r'^Haven$', views.Haven),
    url(r'^Irvine$', views.Irvine),
    url(r'^Stanford$', views.Stanford),
    url(r'^Baltimore$', views.Baltimore),

    url(r'^CAColumbia$', views.CAColumbia),
    url(r'^Burnaby$', views.Burnaby),
    url(r'^Victoria$', views.Victoria),

    url(r'^(r/index|r)$', views.backend_index),
    url(r'^r/carousel$', views.edit_carousel),
    url(r'^r/addcarousel$', views.add_carousel),
    url(r'^r/delcarousel$', views.del_carousel),
    url(r'^r/getcarousel$', views.ajax_get_carousel),
    url(r'^r/gallery$', views.gallery),
    url(r'^r/getpictures$', views.ajax_get_pictures),
    url(r'^r/addpicture$', views.add_picture),
    url(r'^r/delpicture$', views.del_picture),
    url(r'^r/content$', views.content),
    url(r'^r/getcontent$', views.ajax_get_content),

    url(r'^r/editcontent$', views.edit_content),
    url(r'^r/filebrowser$', views.filebrowser),
    url(r'^r/login$', views.login_backend),
    url(r'^r/logout$', views.logout),
    url(r'^r/xxxuser$', views.add_user),
    url(r'^r/deluser$', views.del_user),
    url(r'^r/user$', views.edit_user),
    url(r'^r/getuser$', views.ajax_get_user),
    url(r'^misc/code$', views.refreshcode),
    url(r'^r/flow$', views.flowform),
    url(r'^r/getflowgroup$', views.ajax_get_flowgroup),
    url(r'^r/getflow$', views.ajax_get_flow),
    # url(r'^r/addflow$', views.add_flow),
    url(r'^r/editflowgroup$', views.edit_flowgroup),
    url(r'^r/editflow$', views.edit_flow),
    url(r'^r/del_flow$', views.del_flow),
    url(r'^r/addflowgroup$', views.ajax_add_flowgroup),
    url(r'^r/user_flow$', views.user_flow),
    url(r'^r/get_user_flow$', views.ajax_get_user_flow),
    url(r'^r/add_user_flow$', views.ajax_add_user_flow),
    url(r'^r/del_user_flow$', views.ajax_del_user_flow),

    url(r'^u$', views.user_index),
    url(r'^u/login$', views.user_login),
    url(r'^u/index$', views.user_index),

]
