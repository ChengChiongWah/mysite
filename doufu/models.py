#coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Doufu(models.Model):
    doufu_name = models.CharField(max_length=200)                              #名称
    publish_date = models.DateTimeField(auto_now_add=True)                     #发布时间
    raw_material = models.CharField(max_length=200)                            #材料
 #   picture = models.CharField()
    introduce = models.CharField(max_length=1000)                               #简介
    methods = models.CharField(max_length=1500)                                 #做法

    def __unicode__(self):
        return "{0},{1}, {2}, {3}, {4}".format(self.doufu_name,self.publish_date,self.raw_material,self.introduce,self.methods)

