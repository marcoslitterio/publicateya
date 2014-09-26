# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20140917_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cuit',
            field=models.BigIntegerField(null=True),
        ),
    ]
