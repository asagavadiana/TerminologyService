from django.test import TestCase
from django.urls import reverse
from .models import Refbook, RefbookVersion, RefbookElement

class RefbookAPITestCase(TestCase):

    def setUp(self):
        refbook = Refbook.objects.create(code='MS1', name='Medical Specialties')
        version = RefbookVersion.objects.create(refbook=refbook, version='1.0', start_date='2022-01-01')
        RefbookElement.objects.create(refbook_version=version, code='001', value='Test Value')

    def test_get_refbooks(self):
        response = self.client.get(reverse('refbook-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_elements(self):
        response = self.client.get(reverse('refbook-element-list', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_validate_element(self):
        response = self.client.get(reverse('refbook-element-validate', args=[1]), {'code': '001', 'value': 'Test Value'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['valid'])
