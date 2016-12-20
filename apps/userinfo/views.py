# coding: utf-8
import datetime
from smtplib import SMTPRecipientsRefused

from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail

from models import ActivateCode
from deps.utils.random_string import random_string
from myblog.settings import DEFAULT_FROM_EMAIL


def register(request):
    error = ""
    if request.method == "GET":
        return render(request, 'user_register.html')  
    else:
        username = request.POST.get('username', None).strip()
        email = request.POST.get('email', None).strip()
        password = request.POST.get('password', None).strip()
        re_password = request.POST.get('re_password', None).strip()
        if not username or not password or not email:
            error = u"任何字段都不能为空"
        if password != re_password:
            error = u"两次密码不一致"
        if User.objects.filter(username=username).count() > 0:
            error = u"用户名已存在"
        #if User.objects.filter(email=email).count() > 0:
        #    error = u"该邮箱已注册"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()
            new_string = random_string()
            expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
            code = ActivateCode(owner=user, code=new_string, expire_time=expire_time)
            code.save()

            activate_link = "http://%s/userinfo/activate/%s" % (request.get_host(), new_string)
            try:
                send_mail("激活邮件", "您的激活链接是%s" % activate_link, DEFAULT_FROM_EMAIL, [email])
                return render(request, "user_register_process.html")
            except SMTPRecipientsRefused:
                error = u"邮箱地址不正确，无法正常发送激活邮件"
            
        return render(request, "user_register.html", {'error': error})


def activate(request, activate_code):
    query = ActivateCode.objects.filter(code=activate_code, expire_time__gte=datetime.datetime.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        status = u"激活成功"
    else:
        status = u"激活失败"
    return render(request, "user_activate.html", {"status": status})
