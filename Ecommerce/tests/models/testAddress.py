from django.test import TestCase
from Ecommerce.models import Address

class TestModelAddress(TestCase):
    address = None

    def setUp(self):
        address = Address.objects.create(
            street='Calle de la piruleta',
            door=1,
            floor=1,
            city='Barcelona',
            province='Barcelona',
            country='Spain',
            postal_code='25617'
        )
    def test_create_Address(self):
        address = Address.objects.create(
            street='Calle de la piruleta1',
            door=1,
            floor=1,
            city='Barcelona',
            province='Barcelona',
            country='Spain',
            postal_code='25617'
        )
        self.assertEqual(True,Address.objects.contains(address), 'Error: Object not exists')


    def test_read_Address(self):
        address = Address.objects.filter(street='Calle de la piruleta').first()
        self.assertIn(address, Address.objects.all(), 'Error: Object is not instance of Address')

    def test_update_Address(self):
        address = Address.objects.filter(street='Calle de la piruleta').first()
        address.street = 'Calle de la piruleta1'
        address.save()
        self.assertEqual(Address.objects.filter(street='Calle de la piruleta1').first(),address, 'Error: Object not updated')

    def test_delete_Address(self):
        address = Address.objects.filter(street='Calle de la piruleta')
        address.delete()
        self.assertTrue(Address.objects.count() == 0, 'Error: Object not deleted')


