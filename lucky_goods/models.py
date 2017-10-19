# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# 商品
class Goods(models.Model):
	name = models.CharField(max_length = 20)
	# 简写
	spell = models.CharField(max_length = 20)
	# 单价
	unit_price = models.IntegerField(default = 0)
	# 规格
	specifications = models.IntegerField(default = 0)
	# 库存数量
	nums = models.IntegerField(default = 0)
	# 备注
	detail = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('lucky_goods:goods_detail', kwargs = {'pk':self.pk})

# 商家
class Customer(models.Model):
	name = models.CharField(max_length = 20)
	address = models.CharField(max_length = 20)
	tel = models.CharField(max_length = 11)
	owner = models.CharField(max_length = 20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('lucky_goods:customer_detail', kwargs = {'pk':self.pk})

# 订单
class Order(models.Model):
	# 订单号
	order = models.IntegerField(default = 0)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name="customer_orders")
	create_time = models.DateTimeField()
	total_price = models.IntegerField()
	# 备注
	detail = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', blank=False)

# 订单内容
class Order_Detail(models.Model):
	order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="order_details")
	good = models.ForeignKey('Goods', on_delete=models.CASCADE, related_name="good_use")
	nums = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

#class LuckyUser(AbstractUser):
#	account = models.CharField(max_length=16)
#	name = models.CharField(max_length=20)