# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_wiki_forms', '0008_update_input_part2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputdocker',
            old_name='idv',
            new_name='value',
        ),
    ]
