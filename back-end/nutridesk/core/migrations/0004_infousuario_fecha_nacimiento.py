# Generated by Django 3.0 on 2020-03-07 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200307_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='infousuario',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 2, 39, 25, 396026), verbose_name='Fecha de nacimiento'),
        ),
    ]