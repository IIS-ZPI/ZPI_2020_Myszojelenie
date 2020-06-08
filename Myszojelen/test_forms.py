from django.test import TestCase
from Myszojelen.views import *


class TestForms(TestCase):
    def test_FormAmountForm_should_return_true(self):
        test_data = {'ilosc': 2}
        test_form = FormAmountForm(test_data)
        self.assertTrue(test_form.is_valid())

    def test_FormAmountForm_should_return_false(self):
        test_data = {'ilosc': -1}
        test_form = FormAmountForm(test_data)
        self.assertFalse(test_form.is_valid())

    def test_FormInfoHandlerModelForm(self):
        State.objects.create(state_name='test', state_base_tax=1)
        test_state = State.objects.get(state_name='test')
        test_data = {'id_state': test_state, 'selling_price': 5}
        test_form = FormInfoHandlerModelForm(test_data)
        self.assertTrue(test_form.is_valid())

    def test_FormProductModelForm_should_return_true(self):
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        test_data = {'product_price': 5, 'id_cat': test_category, 'product_name': 'test'}
        test_form = FormProductModelForm(test_data)
        self.assertTrue(test_form.is_valid())

    def test_FormProductModelForm_should_return_false1(self):
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        test_data = {'product_price': -1, 'id_cat': test_category, 'product_name': 'test'}
        test_form = FormProductModelForm(test_data)
        self.assertFalse(test_form.is_valid())

    def test_FormProductModelForm_should_return_false2(self):
        Category.objects.create(category_name='test')
        test_category = Category.objects.get(category_name='test')
        test_data = {'product_price': 5, 'id_cat': test_category, 'product_name': 'test' * 200}
        test_form = FormProductModelForm(test_data)
        self.assertFalse(test_form.is_valid())






