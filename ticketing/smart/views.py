from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainRequest
from accounts.models import UserProfile
from datetime import date, timedelta
import time
import hashlib
import json
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.conf import settings

# Create your views here.
@login_required
def index(request):
    try:
        user = request.user
        msg = request.GET.get("msg", "")
        if user.have_active is False:
            return redirect("/active")
    except Exception as e:
        print(e)
    return render(request, "signin.html", locals())

def faq(request):
    try:
        pass
    except Exception as e:
        print(e)
    return render(request, "faq.html", locals())

def md5(str):
    try:
        my_md5 = hashlib.md5()
        my_md5.update(str.encode('utf-8'))
        md5_str = my_md5.hexdigest()
    except BaseException as e:
        print(e)
        return None
    return md5_str.upper()

@login_required
def active(request):
    try:
        user = request.user
        try:
            print(str(user.id))
            print(settings.USER_KEY)
            sec = md5(str(user.id) + settings.USER_KEY)
            print(sec)
            link = settings.NOW_HOST + "go_active?s=" + sec + "&uid=" + str(user.id)
            print(link)
            # res = send_mail('click this link active:  {}'.format(link),
            #                 settings.EMAIL_HOST_USER, [user.email, ])
        except Exception as e:
            print(e)
        return render(request, "active.html", locals())
    except Exception as e:
        print(e)
    return render(request, "active.html", locals())

@login_required
def jrequests(request):
    try:
        if request.method == "GET":
            return render(request, "requests.html", locals())
        if request.method == "POST":
            print("-----")
            user = request.user
            # print(request.POST.get["subject"])
            subject = request.POST.get("subject", "")
            descrition = request.POST.get("descrition", "")
            priority = request.POST.get("priority", "")

            if len(subject) == 0 or len(descrition) == 0 or len(priority) == 0:
                msg = "error!all key should have value"
                return render(request, "requests.html", locals())
            mr = MainRequest()
            mr.subject = subject
            mr.descrition = descrition
            mr.priority = priority
            mr.user = user
            mr.save()
            return redirect("/myrequests")
    except Exception as e:
        print(e)
        msg = "System error"
        return render(request, "error.html", locals())


@login_required
def myrequests(request):
    try:
        user = request.user
        all_my_request = MainRequest.objects.filter(user=user).order_by("id")
    except Exception as e:
        print(e)
    return render(request, "myrequests.html", locals())

@login_required
def teacher(request):
    try:
        user = request.user
        all_my_request = MainRequest.objects.filter().order_by("id")
    except Exception as e:
        print(e)
    return render(request, "adminmyrequests.html", locals())

@login_required
def detail(request):
    try:
        user = request.user
        now_date = time.strftime("%Y-%m-%d", time.localtime())
        mid = request.GET.get("rid", "")
        if len(mid) == 0:
            msg = "no rid"
            return render(request, "error.html", locals())
        mainReq = MainRequest.objects.filter(user=user, id=mid)
        if len(mainReq) == 0:
            msg = "no request info"
            return render(request, "error.html", locals())
        mainReq = mainReq[0]
    except Exception as e:
        print(e)
    return render(request, "detail.html", locals())

def go_active(request):
    try:
        s = request.GET.get("s","")
        uid = request.GET.get("uid","")
        sec = md5(uid + settings.USER_KEY)
        if sec != s:
            msg = "error!you link is fork,ip will be close"
            return render(request, "error.html", locals())
        user = UserProfile.objects.filter(id=uid)
        if len(user) == 0:
            msg = "error!user is not exists"
            return render(request, "error.html", locals())
        user = user[0]
        user.have_active = True
        user.save()
        return redirect("/index?msg=active success")
    except Exception as e:
        print(e)
        msg = "System error"
        return render(request, "error.html", locals())

@login_required
def admin_detail(request):
    try:
        user = request.user
        if request.method == "GET":
            now_date = time.strftime("%Y-%m-%d", time.localtime())
            mid = request.GET.get("rid", "")
            if len(mid) == 0:
                msg = "no rid"
                return render(request, "error.html", locals())
            mainReq = MainRequest.objects.filter(id=mid)
            if len(mainReq) == 0:
                msg = "no request info"
                return render(request, "error.html", locals())
            mainReq = mainReq[0]
            return render(request, "admin_detail.html", locals())
        if request.method == "POST":
            replay = request.POST.get("replay", "")
            mid = request.POST.get("rid", "")
            if len(mid) == 0:
                msg = "no rid"
                return render(request, "error.html", locals())
            mainReq = MainRequest.objects.filter(id=mid)
            if len(mainReq) == 0:
                msg = "no request info"
                return render(request, "error.html", locals())
            mainReq = mainReq[0]
            mainReq.reply_user = user
            mainReq.reply_content = replay
            mainReq.save()
            return redirect("/teacher")
    except Exception as e:
        print(e)
        msg = "SystemError"
        return render(request, "error.html", locals())