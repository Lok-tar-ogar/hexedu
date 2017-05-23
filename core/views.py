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


def information(req):
    '''
    资讯中心
    '''
    return render(req, "web/information.html", locals())


def information_detail(req):
    '''
    资讯详情
    '''
    return render(req, "web/information_detail.html", locals())