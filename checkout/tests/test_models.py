import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Service
from checkout.models import Order
from django.core.management import call_command


class TestOrderModel(TestCase):
    """
    Test Order Model
    """

    @classmethod
    def setUpTestData(cls):
        # set up base services from json
        call_command('loaddata', 'products/fixtures/service.json', verbosity=0)

        # create 4 users
        for i in range(1, 5):
            user = User(
                username=f'testing_{i}',
                email=f'testing_{i}@test.com',
                password='Tester_1234!'
            )
            user.save()

    @unittest.expectedFailure
    def test_cannot_create_without_user(self):
        # expect failure if trying to create an order without an owner
        service = Service.objects.get(pk=1)
        order = Order.objects.create(
            payment_status="payment_collected",
            total=service.cost,
            service=service
        )

    def test_order_str_method(self):
        # expect failure if trying to create an order without an owner
        service = Service.objects.get(pk=1)
        user = User.objects.get(pk=1)
        order = Order.objects.create(
            payment_status="payment_collected",
            total=service.cost,
            service=service,
            user=user,
        )
        self.assertEquals(str(order), user.username + " " + service.name + " @ " + str(service.costs))

    def test_order_negative_cost_zeros(self):
        # expect failure if trying to create an order without an owner
        service = Service.objects.get(pk=1)
        user = User.objects.get(pk=1)
        order = Order.objects.create(
            payment_status="payment_collected",
            total=service.cost * -1,
            service=service,
            user=user,
        )
        self.assertEqual(str(order), user.username + " " + service.name + " @ 0.00")

    def test_create(self):
        # expect failure if trying to create an order without an owner
        service = Service.objects.get(pk=1)
        user = User.objects.get(pk=1)
        num_orders = Order.objects.filter(user=user).count()
        Order.objects.create(
            payment_status="payment_collected",
            total=service.cost,
            service=service,
            user=user,
        )
        user = User.objects.get(pk=1)
        self.assertEqual(num_orders + 1, Order.objects.filter(user=user).count())