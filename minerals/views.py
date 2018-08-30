import random

from django.shortcuts import get_object_or_404, render
from django.db import models as orig_g

from .models import Group, Mineral


def index(request):
    groups = Group.objects.all()
    return render(request,
                  'minerals/index.html',
                  {'groups': groups})


def mineral_list(request):
    """Generate template list of all minerals."""
    minerals = Mineral.objects.all()
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals})


def group_list(request, pk):
    """Generate template list of all minerals in a specific group."""
    group = get_object_or_404(Group, pk=pk)
    minerals = group.get_min()
    return render(request,
                  'minerals/group_list.html',
                  {'minerals': minerals,
                   'group': group})


def mineral_detail(request, pk):
    """Generate template for a specific mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    attrlist = list(filter(lambda a: not a.startswith('__'), dir(mineral)))
    mlist = [dflt for dflt in dir(orig_g.Model)]
    attrlist = list(filter(lambda x: x not in mlist, attrlist))
    no_list = ['DoesNotExist', 'MultipleObjectsReturned', '_state', 'id',
               'name', 'imgcap', 'imgfile', 'objects', 'group', 'category',
               'formula', 'group_id']
    attrlist = list(filter(lambda x: x not in no_list, attrlist))
    for thing in attrlist:
        if thing.startswith('_'):
            attrlist.remove(thing)
    vallist = [getattr(mineral, thing) for thing in attrlist]
    result = zip(attrlist, vallist)
    attrlist = list(result)
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'attrlist': attrlist})


def random_mineral(request):
    pickfrom = len(Mineral.objects.all())
    prikey = random.randint(1, pickfrom)
    return mineral_detail(request, prikey)


def random_ingroup(request, pk):
    group = get_object_or_404(Group, pk=pk)
    minerals = group.get_min()
    m_choice = [mineral.pk for mineral in minerals]
    prikey = random.choice(m_choice)
    return mineral_detail(request, prikey)


def random_group(request):
    pick_group = len(Group.objects.all())
    prikey = random.randint(1, pick_group)
    return group_list(request, prikey)
