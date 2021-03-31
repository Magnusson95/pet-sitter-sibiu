from django.test import TestCase
from products.models import Service
from django.core.management import call_command


# Create Tests for Service Models

class TestServiceModel(TestCase):
    """
    Test Service model
    """

    @classmethod
    def setUp(self):
        # set up base Services from json
        call_command('loaddata', 'products/fixtures/service.json', verbosity=0)

    def test_str(self):
        test_name = Service(
            name='A Service',
            cost=1.00,
            description='Test Service description',
            sub_heading='Sub heading test',
            detail_1='detail 1 test',
            detail_2='detail 2 test',
            detail_3='detail 3 test',
            period=50
        )
        self.assertEqual(str(test_name), 'A service')

    def test_default_cost(self):
        # expect failure if trying to create an order without an owner
        test_name = Service(
            name='A Service',
            cost=1.00,
            description='Test Service description',
            sub_heading='Sub heading test',
            detail_1='detail 1 test',
            detail_2='detail 2 test',
            detail_3='detail 3 test',
            period=50
        )
        test_name.save()
        prod = Service.objects.filter(name='A service').first()
        self.assertEqual(prod.cost, 10)
