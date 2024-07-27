from django.test import TestCase
from Ecommerce.models import CreditCard

class TestModelCreditCard(TestCase):
    creditCard = None

    def setUp(self):
        creditCard = CreditCard.objects.create(
            number ='1234567890123456',
            holder='John Doe',
            expiration_date='2020-01-01',
            cvv='123'
        )

    def test_create_CreditCard(self):
        creditCard = CreditCard.objects.create(
            number='1234567890123457',
            holder='John Doe',
            expiration_date='2020-01-01',
            cvv='123'
        )
        self.assertEqual(True,CreditCard.objects.contains(creditCard), 'Error: Object not exists')

    def test_read_CreditCard(self):
        creditCard = CreditCard.objects.filter(number='1234567890123456').first()
        self.assertIn(creditCard, CreditCard.objects.all(), 'Error: Object is not instance of CreditCard')

    def test_update_CreditCard(self):
        creditCard = CreditCard.objects.filter(number='1234567890123456').first()
        creditCard.number = '1234567890123457'
        creditCard.save()
        self.assertEqual(CreditCard.objects.filter(number='1234567890123457').first(),creditCard, 'Error: Object not updated')

    def test_delete_CreditCard(self):
        creditCard = CreditCard.objects.filter(number='1234567890123456')
        creditCard.delete()
        self.assertTrue(CreditCard.objects.count() == 0, 'Error: Object not deleted')
