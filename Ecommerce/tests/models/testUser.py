from django.test import TestCase
from Ecommerce.models import User, Client, Employee, Identification, CreditCard, Address


class TestModelUser(TestCase):
    user = None
    client = None
    employee = None

    def setUp(self):
        user = User.objects.create(
            is_client=True,
            username='JohnDoe',
            first_name='John',
            last_name='Doe',
            password='1234',
            email='jhondoe@gmail.com',
            phone='123456789',
            identification= Identification.objects.create(NIF_NIE='12345678A',is_National=True)
        )
        client = Client.objects.create(user=user,
                                        credit_card=CreditCard.objects.create(number='123456789',
                                                                              holder='John Doe',
                                                                              expiration_date='2020-01-01',
                                                                              cvv='123'))
        employee = Employee.objects.create(user=user,is_manager=True)

    def test_create_user(self):
        user = User.objects.create(
            is_client=True,
            username='JohnDoe2',
            first_name='John',
            last_name='Doe',
            password='1234',
            email='jhondoe2@gmail.com',
            phone='123456789',
            identification= Identification.objects.create(NIF_NIE='12345678B',is_National=True)
        )
        self.assertTrue(User.objects.contains(user))

    def test_read_user(self):
        user = User.objects.filter(username='JohnDoe').first()
        self.assertIn(user, User.objects.all())

    def test_update_user(self):
        user = User.objects.filter(username='JohnDoe').first()
        user.username = 'JohnDoe2'
        user.save()
        self.assertEqual(User.objects.filter(username='JohnDoe2').first(),user)

    def test_delete_user(self):
        employee = Employee.objects.filter(user__username='JohnDoe')
        employee.delete()
        client = Client.objects.filter(user__username='JohnDoe')
        client.delete()
        user = User.objects.filter(username='JohnDoe')
        user.delete()
        self.assertTrue(User.objects.count()==0)

    def test_create_client(self):
        user = User.objects.create(
            is_client=True,
            username='JohnDoe2',
            first_name='John',
            last_name='Doe',
            password='1234',
            email='jhondoe2@gmail.com',
            phone='123456789',
            identification= Identification.objects.create(NIF_NIE='12345678C',
                                                          is_National=True),
            address= Address.objects.create(street='Calle Falsa',
                                            door=1,
                                            floor=1,
                                            city='Springfield',
                                            postal_code='12345',
                                            province='Springfield',
                                            country='USA')
        )
        client = Client.objects.create(user=user,
                                       credit_card=CreditCard.objects.create(number='1234567890123456',holder='John Doe',expiration_date='2020-01-01',cvv='123'))
        self.assertTrue(Client.objects.contains(client))

    def test_read_client(self):
        client = Client.objects.filter(user__username='JohnDoe').first()
        self.assertIn(client, Client.objects.all())

    def test_update_client(self):
        client = Client.objects.filter(user__username='JohnDoe').first()
        client.user.username = 'JohnDoe2'
        client.user.save()
        self.assertEqual(Client.objects.filter(user__username='JohnDoe2').first(),client)

    def test_delete_client(self):
        client = Client.objects.filter(user__username='JohnDoe')
        client.delete()
        self.assertTrue(Client.objects.count()==0)

    def test_create_employee(self):
        user = User.objects.create(
            is_client=True,
            username='JohnDoe2',
            first_name='John',
            last_name='Doe',
            password='1234',
            email='jhondoe2@gmail.com',
            phone='123456789',
            identification= Identification.objects.create(NIF_NIE='12345678D',is_National=True),
            address= Address.objects.create(street='Calle Falsa',
                                            door=1,
                                            floor=1,
                                            city='Springfield',
                                            postal_code='12345',
                                            province='Springfield',
                                            country='USA')
        )
        employee = Employee.objects.create(user=user,is_manager=True)
        self.assertTrue(Employee.objects.contains(employee))

    def test_read_employee(self):
        employee = Employee.objects.filter(user__username='JohnDoe').first()
        self.assertIn(employee, Employee.objects.all())

    def test_update_employee(self):
        employee = Employee.objects.filter(user__username='JohnDoe').first()
        employee.user.username = 'JohnDoe2'
        employee.user.save()
        self.assertEqual(Employee.objects.filter(user__username='JohnDoe2').first(),employee)

    def test_delete_employee(self):
        employee = Employee.objects.filter(user__username='JohnDoe')
        employee.delete()
        self.assertTrue(Employee.objects.count()==0)
