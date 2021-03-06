# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180131_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nickname',
            field=models.CharField(default=b'\xe8\xb6\x85\xe5\x80\xbc\xe4\xba\x8c\xe6\x89\x8b\xe6\x9c\xba', max_length=15, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmodel',
            field=models.ForeignKey(verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', to='mysite.PModel'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.PositiveIntegerField(default=2016, verbose_name=b'\xe5\x87\xba\xe5\x8e\x82\xe5\xb9\xb4\xe4\xbb\xbd'),
        ),
    ]
