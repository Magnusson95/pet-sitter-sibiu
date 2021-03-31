from django.test import TestCase
from .models import Service

# Create your tests here.


class ServiceTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Service model
    """

    def test_str(self):
        test_name = Service(name='A service')
        self.assertEqual(str(test_name), 'A service')
