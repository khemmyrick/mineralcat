# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import json

from django.db import migrations, models

from ..models import Mineral
# import models from django.db???

# from mineralcat import minerals, models
# Should I be importing models from my app?  
# Does django.db give the models file from my app?

def loadmin(apps, schema_editor):
    """Load JSON file into Django Database?"""
    minelist = []
    with open('minerals/fixtures/minerals_data.json', 'r', encoding="utf8") as mindb:
        data = json.load(mindb)
        # json1_data = json.loads(data)[0]
        for mineral in data:
            try:
                skip_this = Mineral.objects.get(name=mineral['name'])
            except Mineral.DoesNotExist:
                obj = Mineral(name=get('name', ''),
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
            else:
                continue
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

