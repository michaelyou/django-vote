# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-10 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_vote_action'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user_id', 'content_type', 'object_id', 'action')]),
        ),
    ]