# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-08-21 15:51
# from __future__ import unicode_literals
import json

from django.db import migrations, models


def loadmin(apps, schema_editor):
    """Load JSON file into Django Database?"""
    minelist = []
    with open('minerals_data.json') as mindb:
        data = json.load(mindb)
        for mineral in data:
            if Mineral.objects.get(name=mineral['name']):
                continue
            else:
                obj = models.Mineral(name=get('name', ''),
                                     imgfile=get('image filename', ''),
                                     imgcap=get('image caption', ''),
                                     category=get('category', ''),
                                     formula=get('formula', ''),
                                     strunz_class=get('strunz classification', ''),
                                     color=get('color', ''),
                                     crystal_sys=get('crystal system', ''),
                                     unit_cell=get('unit cell', ''),
                                     crystal_symmetry=get('crystal symmetry', ''),
                                     cleavage=get('cleavage', ''),
                                     ms_hardness=get('mohs scale hardness', ''),
                                     luster=get('luster', ''),
                                     streak=get('streak', ''),
                                     optical_prop=get('optical properties', ''),
                                     refractive_index=get('refractive index', ''),
                                     crystal_habit=get('crystal habit', ''),
                                     specific_gravity=get('specific gravity', ''),
                                     family=get('group', ''),
                                    )
                minelist.append(obj)
            # Add each mineral instance to list.
    Mineral.objects.bulk_create(minelist)
    # Save entire list to database.

# def unloadmin():
#    """Delete all the database entries."""
#    # Is this a thing I have to do?
#    Minerals.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadmin)
    ]
