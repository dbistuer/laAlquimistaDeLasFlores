from django.test import TestCase
from Ecommerce.models import Identification

class TestModelIdentification(TestCase):
    nif_nie = '78094395B'
    is_national = True

    def setUp(self):
        self.add_identification(nif_nie=self.nif_nie, is_national=self.is_national)

    def test_create_identification(self):
        self.delete_identification()
        iden = Identification()
        iden.NIF_NIE = self.nif_nie
        iden.is_National = self.is_national
        iden.save()
        self.assertEqual(True,Identification.objects.contains(iden), 'Error: Object not created')

    def test_read_identification(self):
        iden = Identification.objects.filter(NIF_NIE=self.nif_nie).first()
        self.assertIsInstance(iden, Identification, 'Error: Object is not instance of Identification')

    def test_update_identification(self):
        iden = Identification.objects.filter(NIF_NIE=self.nif_nie).first()
        iden.is_National = False
        iden.NIF_NIE = '78094395C'
        iden.save()
        self.assertEqual(Identification.objects.filter(NIF_NIE='78094395C').first(),iden, 'Error: Object not updated')

    def test_delete_identification(self):
        iden = Identification.objects.filter(NIF_NIE=self.nif_nie)
        iden.delete()
        self.assertTrue(Identification.objects.count() == 0, 'Error: Object not deleted')

    ###TODO: CHECK NIF,NIE REGEX

    def add_identification(self,nif_nie=nif_nie, is_national=is_national):
        iden = Identification.objects.create(
            NIF_NIE=nif_nie,
            is_National=is_national
        )
        iden.save()

    def delete_identification(self,nif_nie=nif_nie):
        iden = Identification.objects.filter(NIF_NIE=nif_nie).delete()



