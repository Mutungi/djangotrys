# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StudentName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=30)),
                ('Level', models.CharField(max_length=30)),
                ('Course', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Student_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.StudentName'),
        ),
    ]