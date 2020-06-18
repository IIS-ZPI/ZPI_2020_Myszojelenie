from django.test import TestCase

from django.urls import reverse, resolve

from Myszojelen.views import *


class TestUrls(TestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_adding_url_is_resolved(self):
        url = reverse('adding')
        self.assertEquals(resolve(url).func, adding_form)

    def test_removed_url_is_resolved(self):
        url = reverse('removed')
        self.assertEquals(resolve(url).func, removerecord)

    def test_removed_param_url_is_resolved(self):
        url = reverse('removed', args=[1])
        self.assertEquals(resolve(url).func, removerecord)

    def test_table_url_is_resolved(self):
        url = reverse('table')
        self.assertEquals(resolve(url).func, addingAndTable)