# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def fix_input_newer(apps, schema_editor):
    m = apps.get_model("django_wiki_forms", "Input")
    db_alias = schema_editor.connection.alias

    for i in m.objects.using(db_alias).all():
        n = m.objects.filter(article=i.article, owner=i.owner, name=i.name, created__gt=i.created).order_by('created').first()
        if i.newer != n:
            i.newer = n
            i.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_wiki_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='newer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_wiki_forms.Input'),
        ),
        migrations.RunPython(fix_input_newer, migrations.RunPython.noop)
    ]