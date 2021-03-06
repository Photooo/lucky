# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=11)),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('spell', models.CharField(max_length=20)),
                ('unit_price', models.IntegerField(default=0)),
                ('specifications', models.IntegerField(default=0)),
                ('nums', models.IntegerField(default=0)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField()),
                ('total_price', models.IntegerField()),
                ('detail', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_orders', to='lucky_goods.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_use', to='lucky_goods.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='lucky_goods.Order')),
            ],
        ),
    ]
