# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm
from django.db.models.signals import post_save

import os
from django.template.defaultfilters import slugify


PROJECT_PATH = os.path.dirname("__file__")



def user_new_unicode(self):
    return self.username if self.get_full_name() == "" else self.get_full_name()


# Replace the __unicode__ method in the User class with out new implementation
User.__unicode__ = user_new_unicode


class Tokenregister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % self.user.username


class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    nif = models.CharField(max_length=15)
    address = models.CharField(max_length=120, blank=True, null=True, verbose_name="Dirección")
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name="Teléfono")
    photo = models.ImageField(upload_to="web/users", default="web/users/default_user.png", verbose_name="Fotografía")
    darkmode = models.BooleanField(default=False)
    onesignal_id = models.CharField(max_length=40, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % self.user.username