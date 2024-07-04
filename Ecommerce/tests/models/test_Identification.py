import pytest
from django.test import TestCase
from Ecommerce.models import Identification


@pytest.mark.django_db
class TestModelIdentification(TestCase):
    nif_nie = '78094395B'
    is_national = True

    def setup_class(cls):
        cls.add_identification(cls)

    def test_create_identification(self, nif_nie=nif_nie, is_national=is_national):
        self.delete_identification()
        iden = Identification()
        iden.NIF_NIE = nif_nie
        iden.is_National = is_national
        iden.save()
        self.assertTrue(Identification.objects.contains(iden))

    def test_read_identification(self, nif_nie=nif_nie):
        iden = Identification.objects.filter(NIF_NIE=nif_nie).first()
        print(iden)
        self.assertIsInstance(iden, Identification)

    def test_update_identification(self, nif_nie=nif_nie):
        print('nif: ' + nif_nie)
        iden = Identification.objects.filter(NIF_NIE=nif_nie).first()
        iden.is_National = False
        iden.NIF_NIE = '78094395C'
        iden.save()
        self.assertEqual(Identification.objects.filter(NIF_NIE='78094395C').first(),iden)

    def test_delete_identification(self, nif_nie=nif_nie):
        print('nif: ' + nif_nie)
        iden = Identification.objects.filter(NIF_NIE=nif_nie)
        iden.delete()
        self.assertTrue(Identification.objects.count()==0)

    ###TODO: CHECK NIF,NIE REGEX

    def add_identification(self,nif_nie=nif_nie, is_national=is_national):
        iden = Identification()
        iden.NIF_NIE = nif_nie
        iden.is_National = is_national
        iden.save()

    def delete_identification(self,nif_nie=nif_nie):
        print(nif_nie)
        iden = Identification.objects.filter(NIF_NIE=nif_nie).delete()



