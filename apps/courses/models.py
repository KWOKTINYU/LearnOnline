# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField

from django.db import models
from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    degree = models.CharField(verbose_name=u"难度", choices=(("primary", u"初级"), ("middle", u"中级"), ("senior", u"高级")), max_length=7)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    learn_students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"课程点击数")
    category = models.CharField(verbose_name=u"课程种类", max_length=20, default=u"后端开发")
    tag = models.CharField(default="", max_length=10, verbose_name=u"课程标签")
    need_know = models.CharField(default="", max_length=200, verbose_name=u"课程须知")
    teacher_advise = models.CharField(default="", max_length=200, verbose_name=u"讲师建议")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_chapter_nums(self):
        # 获取章节数
        return self.lesson_set.all().count()
    get_chapter_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='https://www.baidu.com/'>跳转</>")
    go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:3]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        # 不会生成表，但又具有model的功能  可在admin中注册不同的数据
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 获取所有视频
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, verbose_name=u'访问地址', default="")
    learn_times = models.IntegerField(default=0, verbose_name=u'视频时长(分钟数)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
