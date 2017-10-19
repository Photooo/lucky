# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
	"""docstring for Test"models.Modelf __init__(self, arg):
		super(Test,models.Model.__init__()
		self.arg = arg
	"""
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	score = models.IntegerField()
