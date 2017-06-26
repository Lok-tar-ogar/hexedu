from django.shortcuts import render
import json
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    tag = 'all'
    cat = 'all'
    tag = req.GET.get("tag", "all")
    cat = req.GET.get("cate", "all")
    news = News.objects.all()
    if tag == 'all' or '':
        pass
    else:
        news = news.filter(tag__name=tag)

    if cat == "all" or '':
        pass
    else:
        news = news.filter(cat__name=cat)

    new = News.objects.all().count()
    cate = Category.objects.all()
    t = Tag.objects.all()

    paginator = Paginator(news, 6)
    page = req.GET.get('page', 1)
    try:
        paged = paginator.page(page)
        pagenum = paginator.num_pages
        page = int(page)

        if 1 <= pagenum <= 5:
            rangedpages = paginator.page_range

        else:
            rangedpages = [page - 2 if page - 2 > 1 else 1, page - 1 if page > 2 else 1, page, page + 1, page + 2,
                           page + 3,
                           page + 4]
        rangedpages = list(set(rangedpages))

    except Exception as e:
        page = 1
        pagenum = paginator.num_pages
        if pagenum == 0:
            lastpagenum = []

        elif 1 <= pagenum <= 5:
            paged = paginator.page(1)
            rangedpages = paginator.page_range
        else:
            paged = paginator.page(1)
            lastpagenum = paginator.num_pages
            rangedpages = [1, 2, 3, 4, 5]
    return render(req, "web/information.html", locals())


def information_detail(req, fid):
    '''
    资讯详情
    '''
    tag = 'all'
    cat = 'all'
    tag = req.GET.get("tag", "all")
    cat = req.GET.get("cate", "all")

    count = News.objects.all().count()
    cate = Category.objects.all()
    t = Tag.objects.all()
    new = News.objects.get(id=fid)
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


def EB5(req):
    '''
    移民落户EB-3
    '''
    return render(req, "web/EB-5.html", locals())


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


def develop(req):
    '''
    一线城市落户
    '''
    return render(req, "web/develop.html", locals())


def app_detail(req):
    '''
    大学详情页面
    '''
    return render(req, "web/apply_detail.html", locals())


def upenn(req):
    '''
    宾夕法尼亚大学
    '''
    return render(req,'web/usa/Pennsylvania.html',locals())


def CA(req):
    '''
    南加州大学
    '''
    return render(req,'web/usa/CA.html',locals())


def Columbia(req):
    '''
    哥伦比亚大学
    '''
    return render(req,'web/usa/Columbia.html',locals())


def Denver(req):
    '''
    丹佛大学
    '''
    return render(req,'web/usa/Denver.html',locals())


def Harvard(req):
    '''
    哈佛大学
    '''
    return render(req,'web/usa/Harvard.html',locals())


def Haven(req):
    '''
    yelu大学
    '''
    return render(req,'web/usa/Haven.html',locals())


def Irvine(req):
    '''
    欧文大学
    '''
    return render(req,'web/usa/Irvine.html',locals())


def Stanford(req):
    '''
    欧文大学
    '''
    return render(req,'web/usa/Stanford.html',locals())

def Baltimore(req):
    '''
    欧文大学
    '''
    return render(req,'web/usa/Baltimore.html',locals())

def Burnaby(req):
    '''
    西蒙弗雷泽大学
    '''
    return render(req,'web/ca/Burnaby.html',locals())

def CAColumbia(req):
    '''
    英属哥伦比亚大学
    '''
    return render(req,'web/ca/CAColumbia.html',locals())

def Victoria(req):
    '''
    维多利亚大学
    '''
    return render(req,'web/ca/Victoria.html',locals())

@csrf_exempt
def message(req):
    '''
    留言信息
    '''
    try:
        r = req.POST
        name = r.get("name")
        tel = r.get("tel", None)
        email = r.get("email", None)
        m = r.get("message", None)

        data = {}
        if name or tel or email or m:
            mess = Message()
            mess.name = name
            mess.tel = tel
            mess.email = email
            mess.message = m
            mess.save()
            data["status"] = "200"

            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data["status"] = "500"
            return HttpResponse(json.dumps(data, ensure_ascii=False))

    except:
        data = {}
        data["status"] = "500"
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")
