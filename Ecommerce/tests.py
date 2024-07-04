from django.test import TestCase
from Ecommerce.models import Identification

iden = Identification()


class TestModelIdentification(TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        iden.NIF_NIE = '78094395B'
        iden.is_National = True
        iden.save()

    def create_identification(self, nif_nie=iden.NIF_NIE, is_national=iden.is_National):
        print('nif: '+ nif_nie + '; is_nationale: ' + is_national)
        iden = Identification()
        iden.NIF_NIE = nif_nie
        iden.is_National = is_national
        iden.save()
        self.assertTrue(Identification.objects.contains(iden))

    def test_read_identification(self, nif_nie=iden.NIF_NIE):
        print('nif: ' + nif_nie )
        self.assertIsInstance(Identification.objects.filter(NIF_NIE=nif_nie).first(), Identification)

    def test_update_identification(self, nif_nie=iden.NIF_NIE):
        print('nif: ' + nif_nie)
        iden = Identification.objects.filter(NIF_NIE=nif_nie).first()
        iden.is_National = False
        iden.NIF_NIE = '78094395C'
        iden.update()
        print(Identification.objects.filter(NIF_NIE='78094395C').first())
        self.assertEqual(Identification.objects.filter(NIF_NIE='78094395C').first(),iden)

    def test_delete_identification(self, nif_nie=iden.NIF_NIE):
        print('nif: ' + nif_nie)
        iden = Identification.objects.filter(NIF_NIE=nif_nie).first()
        iden.delete()
        self.assertFalse(Identification.objects.contains(iden))
