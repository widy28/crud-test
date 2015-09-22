# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('gender', models.CharField(max_length=2, verbose_name=b'Gender', choices=[(b'1', b'M'), (b'2', b'S')])),
                ('languages', models.CharField(default=b'English', max_length=20, verbose_name=b'Languages')),
                ('card_number', models.CharField(max_length=15, verbose_name=b'Card number')),
                ('expiry_date', models.DateField(verbose_name=b'Expiry date')),
                ('professional', models.BooleanField(verbose_name=b'Professional')),
            ],
        ),
    ]
