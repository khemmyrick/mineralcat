from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=250)
    imgfile = models.CharField(default='', max_length=250)
    imgcap = models.CharField(default='', max_length=250)
    category = models.CharField(default='', max_length=250)
    formula = models.CharField(default='', max_length=250)
    strunz_class = models.CharField(default='', max_length=250)
    color = models.CharField(default='', max_length=250)
    crystal_sys = models.CharField(default='', max_length=250)
    unit_cell = models.CharField(default='', max_length=250)
    crystal_symmetry = models.CharField(default='', max_length=250)
    cleavage = models.CharField(default='', max_length=250)
    ms_hardness = models.CharField(default='', max_length=250)
    luster = models.CharField(default='', max_length=250)
    streak = models.CharField(default='', max_length=250)
    diaphaneity = models.CharField(default='', max_length=250)
    optical_prop = models.CharField(default='', max_length=250)
    refractive_index = models.CharField(default='', max_length=250)
    crystal_habit = models.CharField(default='', max_length=250)
    specific_gravity = models.CharField(default='', max_length=250)
    group = models.CharField(default='', max_length=250)

    def __str__(self):
        return self.name
