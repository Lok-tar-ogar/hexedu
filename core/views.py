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


def guidance(req):
    '''
    学术辅导
    '''
    return render(req, "web/guidance.html", locals())


def tour(req):
    '''
    游学之旅
    '''
    return render(req, "web/tour.html", locals())


def certification(req):
    '''
    学历学位认证
    '''
    return render(req, "web/certification.html", locals())


def live(req):
    '''
    生活辅助
    '''
    return render(req, "web/live.html", locals())


def EB(req):
    '''
    移民落户
    '''
    return render(req, "web/EB.html", locals())


def EB3(req):
    '''
    移民落户EB-3
    '''
    return render(req, "web/EB-3.html", locals())


def usa(req):
    '''
    美国
    '''
    return render(req, "web/usa.html", locals())


def ca(req):
    '''
    加拿大
    '''
    return render(req, "web/ca.html", locals())


def europe(req):
    '''
    加拿大
    '''
    return render(req, "web/europe.html", locals())


def asia(req):
    '''
    加拿大
    '''
    return render(req, "web/asia.html", locals())


def profession(req):
    '''
    职业规划
    '''
    return render(req, "web/profession.html", locals())


def resume(req):
    '''
    简历咨询
    '''
    return render(req, "web/resume.html", locals())


def personnel(req):
    '''
    人才录入
    '''
    return render(req, "web/personnel.html", locals())


def train(req):
    return render(req, "web/train.html", locals())


def cooperate(req):
    return render(req, "web/cooperate.html", locals())


def elite(req):
    return render(req, "web/elite.html", locals())


def contact(req):
    return render(req, "web/contact.html", locals())


def about(req):
    return render(req, "web/about.html", locals())


def car(req):
    '''
    免税车
    '''
    return render(req, "web/car.html", locals())


def housekeep(req):
    '''
    免税车
    '''
    return render(req, "web/housekeep.html", locals())


def settle(req):
    '''
    一线城市落户
    '''
    return render(req, "web/settle.html", locals())

