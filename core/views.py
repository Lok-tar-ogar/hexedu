from django.shortcuts import render



def index(req):
    '''
    首页
    '''
    return render(req, "web/index.html", locals())
