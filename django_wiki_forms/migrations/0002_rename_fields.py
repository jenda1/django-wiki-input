# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20171001_0605'),
        ('django_wiki_forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='key',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='inputdefinition',
            old_name='key',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='inputdependency',
            old_name='key',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='inputdefinition',
            unique_together=set([('article', 'name')]),
        ),
    ]
