import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .models import UserProfile
from .forms import LoginForm
import os
import time
import hashlib
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.conf import settings

@login_required
def my_info(request):
    try:
        user = request.user
        if request.method == "GET":
            return render(request, "my_info.html", locals())
        if request.method == "POST":
            username = request.POST.get("username", "")
            mobile = request.POST.get("mobile", "")
            location = request.POST.get("location", "")
            avatar = request.FILES.get('avatar')
            print(username)
            print(mobile)
            if len(location) == 0:
                msg = "Location cannot be empty"
                return render(request, "my_info.html", locals())
            if username == "" or username == None or len(username) < 6:
                msg = "Username can not be empty, must be greater than 6 digits"
                return render(request, "my_info.html", locals())
            if mobile == "" or mobile == None or len(mobile) != 11:
                msg = "Mobile number cannot be empty，must be 11 digits and in the correct format"
                return render(request, "my_info.html", locals())
            if avatar != None:
                stamp = str((int(round(time.time() * 1000))))
                imgname = stamp + avatar.name
                print(imgname)
                path = os.path.join(settings.MEDIA_ROOT, 'avatar', imgname)
                print(path)
                url = "avatar/" + imgname
                print(url)
                with open(path, 'wb') as f:
                    for chunk in avatar.chunks():
                        f.write(chunk)
            user.username = username
            user.mobile = mobile
            user.location = location
            if avatar != None:
                user.avatar = url
            user.save()
            msg = "Successfully modified"
            return render(request, "my_info.html", locals())
    except Exception as e:
        print(e)
        msg = "system error"
        return render(request, "my_info.html", locals())


def md5(str):
    try:
        my_md5 = hashlib.md5()
        my_md5.update(str.encode('utf-8'))
        md5_str = my_md5.hexdigest()
    except BaseException as e:
        print(e)
        return None
    return md5_str.upper()

def do_register(request):
    try:
        msg = ""
        if request.method == "GET":
            return render(request, "signup.html", locals())
        if request.method == "POST":
            user = request.user
            datas = request.POST
            username = request.POST.get("username")
            password = request.POST.get("password")
            if len(username) < 6 or len(password) < 6 or len(password) < 6:
                msg="email or password min length = 7"
                return render(request, "signup.html", locals())
            if str(username).endswith("@kcl.ac.uk") is False:
                msg="email should endwith @kcl.ac.uk!"
                return render(request, "signup.html", locals())
            only = UserProfile.objects.filter(username=username)
            if len(only) > 0:
                msg = "email have registe"
                return render(request, "signup.html", locals())

            new_user = UserProfile()
            new_user.username = username
            new_user.mpassword = password
            new_user.email = username
            new_user.set_password(password)
            new_user.save()
            try:
                sec = md5(str(new_user.id) + settings.USER_KEY)
                print(sec)
                link = settings.NOW_HOST + "go_active?s=" + sec + "&uid=" + str(new_user.id)
                print(link)
                res = send_mail('active','click this link active:  ' + link,
                                settings.EMAIL_HOST_USER, [username, ])
            except Exception as e:
                print(e)
            return redirect("accounts:login")
        else:
            return render(request, "signup.html", locals())
    except Exception as e:
        print(e)
        msg = "system error"
        return render(request, "signup.html", locals())


def user_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("/")
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    # user.backend = 'django.contrib.auth.backends.ModelBackend' # Specify the default login authentication method
                    login(request, user)
                    if user.is_teacher:
                        return redirect("/teacher")
                    else:
                        return redirect("/")
                else:
                    errorinfo = "email or password not right "
                    return render(request, 'index.html', {'login_form': login_form, "errorinfo":errorinfo})

            else:
                errorinfo = "The account number or password is incorrect or in the wrong format"
                return render(request, 'index.html', {'login_form': login_form, "errorinfo":errorinfo})
        else:
            login_form = LoginForm()
            return render(request, 'index.html', {'login_form': login_form})
    except Exception as e:
        login_form = LoginForm()
        print(e)
        errorinfo = "system error"
        return render(request, 'index.html', {'login_form': login_form, "errorinfo":errorinfo})


@login_required
def user_logout(request):
    try:
        logout(request)
        return redirect('accounts:login')
    except Exception as e:
        print(e)
    return render(request, "error.html", {"msg":"logout error"})

