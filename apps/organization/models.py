# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名")
    desc = models.TextField(verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(default="organization", verbose_name=u"机构类别", max_length=20, choices=(("organization", u"培训机构"), ("personal", u"个人"), ("university", u"高校")))
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100)
    address = models.CharField(max_length=200, verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取课程机构教师数量
        return self.teacher_set.all().count()

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    work_years = models.IntegerField(default=0, verbose_name=u"工作年数")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司名称")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    work_points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
