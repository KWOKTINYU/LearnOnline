# _*_ encoding:utf-8 _*_
"""LearnOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, IndexView
from organization.views import OrgView
from LearnOnline.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url('^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url('^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构URL配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程URL配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 处理MEDIA信息,配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 用户个人信息
    url(r'^users/', include('users.urls', namespace="users")),

    # 富文本DjangoUeditor
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]
# 404页面配置
handler404 = 'users.views.page_not_found'
# 500页面配置
handler500 = 'users.views.page_error'
