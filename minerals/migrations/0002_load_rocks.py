# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import json

from django.db import migrations, models

# from ..models import Mineral  ### DJANGO pulls model from operations' arguments apparently?
# import models from django.db???

# from mineralcat import minerals, models
# Should I be importing models from my app?  
# Does django.db give the models file from my app?

def loadmin(apps, schema_editor):
    """Load JSON file into Django Database?"""
    Mineral = apps.get_model('minerals', 'Mineral')
    minelist = []
    with open('minerals/fixtures/minerals_data.json', 'r', encoding="utf8") as mindb:
        data = json.load(mindb)
        # data is a LIST of DICTS
        for mineral in data:
            # try:
            #     skip_this = Mineral.objects.get(name=mineral['name'])
            # except Mineral.DoesNotExist:
            obj = Mineral(name=mineral.get('name', ''),
                          imgfile=mineral.get('image filename', ''),
                          imgcap=mineral.get('image caption', ''),
                          category=mineral.get('category', ''),
                          formula=mineral.get('formula', ''),
                          strunz_classification=mineral.get(
                            'strunz classification', ''),
                          color=mineral.get('color', ''),
                          crystal_system=mineral.get('crystal system', ''),
                          unit_cell=mineral.get('unit cell', ''),
                          crystal_symmetry=mineral.get(
                            'crystal symmetry', ''),
                          cleavage=mineral.get('cleavage', ''),
                          mohs_scale_hardness=mineral.get(
                            'mohs scale hardness', ''),
                          luster=mineral.get('luster', ''),
                          streak=mineral.get('streak', ''),
                          diaphaneity=mineral.get('diaphaneity', ''),
                          optical_properties=mineral.get(
                            'optical properties', ''),
                          refractive_index=mineral.get(
                            'refractive index', ''),
                          crystal_habit=mineral.get('crystal habit', ''),
                          specific_gravity=mineral.get(
                            'specific gravity', ''),
                          group=mineral.get('group', ''),
                         )
            minelist.append(obj)
            # Add each mineral instance to list.
            # else:
            #    continue
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

