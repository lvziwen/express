# coding: utf-8
__author__ = 'lvziwen'

from django.db import models
from django.contrib.auth.models import User

class Express_order(models.Model):
    order_id = models.CharField(max_length=32)
    user = models.ForeignKey(User)
    price = models.FloatField(default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()