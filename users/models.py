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

    def __unicode__(self):
        return u"%s" % self.user.username


class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nif = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    poblacion = models.CharField(max_length=25, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    telf_fijo = models.CharField(max_length=15, blank=True, null=True)
    telf_movil = models.CharField(max_length=15, blank=True, null=True)
    onesignal_id = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=8, blank=False, null=False, default="django")

    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.user.username