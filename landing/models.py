# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        try:
            return self.name
        except Exception:
            return self.id



class SignIn(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=512)
