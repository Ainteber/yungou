# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.IntegerField(default=1)),
                ('pmdesc', models.CharField(max_length=100)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.CharField(max_length=16)),
                ('childcid', models.CharField(max_length=16)),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=16)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MainMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
                ('categoryid', models.CharField(max_length=16)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=16)),
                ('productid1', models.CharField(max_length=16)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.FloatField(default=0)),
                ('marketprice1', models.FloatField(default=1)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=16)),
                ('productid2', models.CharField(max_length=16)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.FloatField(default=0)),
                ('marketprice2', models.FloatField(default=1)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=16)),
                ('productid3', models.CharField(max_length=16)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.FloatField(default=0)),
                ('marketprice3', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
        migrations.CreateModel(
            name='OrderGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Goods')),
            ],
            options={
                'db_table': 'axf_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.CharField(max_length=64)),
                ('o_status', models.IntegerField(default=0)),
                ('o_create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.AddField(
            model_name='ordergoodsmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.OrderModel'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Goods'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel'),
        ),
    ]
