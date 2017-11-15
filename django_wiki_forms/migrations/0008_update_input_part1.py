# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 05:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def cleanup(apps, schema_editor):
    InputOld = apps.get_model('django_wiki_forms', 'InputOld')
    InputNew = apps.get_model('django_wiki_forms', 'InputNew')

    db_alias = schema_editor.connection.alias

    for i in InputOld.objects.using(db_alias).all():
        InputNew(article=i.article, owner=i.owner, created=i.created, created_by=i.created_by, name=i.name, val=i.val).save()

    for i in InputNew.objects.using(db_alias).all():
        n = InputNew.objects.using(db_alias).filter(article=i.article, owner=i.owner, name=i.name, created__gt=i.created).order_by('created').first()
        if i.newer != n:
            i.newer = n
            i.save()



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_wiki_forms', '0007_inputdocker_fixes'),
        ('wiki', '0002_urlpath_moved_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Input',
            new_name='InputOld',
        ),
        migrations.AlterField(
            model_name='inputold',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_inputs_old', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inputold',
            name='owner',
            field=models.ForeignKey(help_text='The author of the input. The owner always has both read access.', on_delete=django.db.models.deletion.CASCADE, related_name='owned_inputs_old', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.CreateModel(
            name='InputNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('name', models.CharField(max_length=28)),
                ('val', models.TextField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='article')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_inputs', to=settings.AUTH_USER_MODEL)),
                ('newer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_wiki_forms.InputNew')),
                ('owner', models.ForeignKey(help_text='The author of the input. The owner always has both read access.', on_delete=django.db.models.deletion.CASCADE, related_name='owned_inputs', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Input',
                'verbose_name_plural': 'Inputs',
                'get_latest_by': 'created',
            },
        ),
        migrations.RunPython(cleanup),
     ]
