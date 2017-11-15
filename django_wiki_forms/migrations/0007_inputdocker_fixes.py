# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def cleanup(apps, schema_editor):
    InputDocker = apps.get_model('django_wiki_forms', 'InputDocker')
    InputDefValue = apps.get_model('django_wiki_forms', 'InputDefValue')
    Input = apps.get_model('django_wiki_forms', 'Input')

    db_alias = schema_editor.connection.alias

    InputDocker.objects.using(db_alias).all().delete()
    InputDefValue.objects.using(db_alias).all().delete()
    Input.objects.using(db_alias).filter(owner__isnull=True).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('django_wiki_forms', '0006_add_inputdefvalue_created'),
    ]

    operations = [
        migrations.RunPython(cleanup, reverse_code=migrations.RunPython.noop),

        migrations.AddField(
            model_name='inputdocker',
            name='idv',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_wiki_forms.InputDefValue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inputdocker',
            name='container_id',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='inputdocker',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='inputdocker',
            name='idef',
        ),
        migrations.RemoveField(
            model_name='inputdocker',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='inputdocker',
            name='val',
        ),
        migrations.AlterField(
            model_name='input',
            name='owner',
            field=models.ForeignKey(help_text='The author of the input. The owner always has both read access.', on_delete=django.db.models.deletion.CASCADE, related_name='owned_inputs', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
            preserve_default=False,
        ),
    ]
