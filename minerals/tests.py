
from django.urls import reverse
from django.test import TestCase

from .models import Group, Mineral

class MineralModelTests(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            name="Crystal Gems"
        )
        
    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Crystal Gems')

    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Pearl",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="white",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.group
        )
        self.assertIn(mineral, self.group.mineral_set.all())


class MineralViewsTests(TestCase):
    def setUp(self):
        self.cg = Group.objects.create(
            name="Crystal Gems"
        )
        self.hg = Group.objects.create(
            name="Homeworld Gems"
        )
        self.pearl = Mineral.objects.create(
            name="Pearl",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="white",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.amethyst = Mineral.objects.create(
            name="Amethyst",
            imgfile="Unusable Garbage",
            imgcap="Various amethysts",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="purple",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.cg
        )
        self.nephrite = Mineral.objects.create(
            name="Nephrite",
            imgfile="Unusable Garbage",
            imgcap="Various pearls",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="yellow",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.hg
        )
        self.jasper = Mineral.objects.create(
            name="Jasper",
            imgfile="Unusable Garbage",
            imgcap="Various jaspers",
            category="Carbonate mineral, protein",
            formula="CaCO<sub>3</sub>",
            strunz_classification="05.AB",
            color="white, pink, silver, cream, etc",
            crystal_system="Orthorhombic",
            unit_cell="",
            crystal_symmetry="",
            cleavage="",
            mohs_scale_hardness="2.5–4.5",
            luster="",
            streak="black and yellow",
            diaphaneity="",
            optical_properties="",
            refractive_index="1.52-1.66",
            crystal_habit="",
            specific_gravity="2.60–2.85",
            group=self.hg
        )
        
    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:mineral_list/'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.pearl, resp.context['minerals'])
        self.assertIn(self.amethyst, resp.context['minerals'])
        self.assertIn(self.nephrite, resp.context['minerals'])
        self.assertIn(self.jasper, resp.context['minerals'])

    