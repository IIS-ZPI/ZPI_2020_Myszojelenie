from django.test import TestCase, Client
from django.urls import reverse

from Myszojelen.views import *


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Myszojelen/index.html')

    def test_adding_form(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Myszojelen/index.html')

    def test_addingAndTable_GET(self):
        response = self.client.get(reverse('table'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Myszojelen/addingAndTable.html')

    def test_addingAndTable_POST_baseTax(self):
        State.objects.create(state_name='test', state_base_tax=1)
        test_state = State.objects.get(state_name='test')
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        response = self.client.post(reverse('table'), {
            'ilosc': 1,
            'id_state': test_state.id,
            'selling_price': 1,
            'id_cat': test_category.id,
            'product_price': 2,
            'product_name': 'test'
        })
        wyniki = response.context['display_list']
        temp = wyniki.pop(0)
        self.assertEquals(-1.5, temp.calculated_price)
        self.assertTemplateUsed(response, 'Myszojelen/addingAndTable.html')

    def test_addingAndTable_POST_specialTax(self):
        State.objects.create(state_name='test', state_base_tax=1)
        test_state = State.objects.get(state_name='test')
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        State_Category_Tax.objects.create(id_cat=test_category, id_state=test_state, tax_val=0.5)

        response = self.client.post(reverse('table'), {
            'ilosc': 1,
            'id_state': test_state.id,
            'selling_price': 1,
            'id_cat': test_category.id,
            'product_price': 2,
            'product_name': 'test'
        })
        wyniki = response.context['display_list']
        temp = wyniki.pop(0)
        self.assertEquals(-1.3333, temp.calculated_price)
        self.assertTemplateUsed(response, 'Myszojelen/addingAndTable.html')

    def test_addingAndTable_POST_thresholdTaxExceeded(self):
        State.objects.create(state_name='test', state_base_tax=1)
        test_state = State.objects.get(state_name='test')
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        State_Category_Tax.objects.create(id_cat=test_category, id_state=test_state, tax_val=0.5, tax_free=1)

        response = self.client.post(reverse('table'), {
            'ilosc': 1,
            'id_state': test_state.id,
            'selling_price': 1,
            'id_cat': test_category.id,
            'product_price': 2,
            'product_name': 'test'
        })
        wyniki = response.context['display_list']
        temp = wyniki.pop(0)
        self.assertEquals(-1.3333, temp.calculated_price)
        self.assertTemplateUsed(response, 'Myszojelen/addingAndTable.html')

    def test_addingAndTable_POST_thresholdTaxNotExceeded(self):
        State.objects.create(state_name='test', state_base_tax=1)
        test_state = State.objects.get(state_name='test')
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        State_Category_Tax.objects.create(id_cat=test_category, id_state=test_state, tax_val=0.5, tax_free=10)
        response = self.client.post(reverse('table'), {
            'ilosc': 1,
            'id_state': test_state.id,
            'selling_price': 1,
            'id_cat': test_category.id,
            'product_price': 2,
            'product_name': 'test'
        })
        wyniki = response.context['display_list']
        temp = wyniki.pop(0)
        self.assertEquals(-1.0, temp.calculated_price)
        self.assertTemplateUsed(response, 'Myszojelen/addingAndTable.html')
