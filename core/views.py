from django.shortcuts import render



def index(req):
    '''
    首页
    '''
    return render(req, "web/index.html", locals())


def apply(req):
    '''
    本研申请
    '''
    return render(req, "web/application.html", locals())