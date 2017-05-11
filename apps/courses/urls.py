# _*_ encoding:utf-8 _*_
__author__ = 'pearl'
__date__ = '2017/5/10 15:23'

from django.conf.urls import url, include

from .views import CourseListView

urlpatterns = [
    # 课程首页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

]