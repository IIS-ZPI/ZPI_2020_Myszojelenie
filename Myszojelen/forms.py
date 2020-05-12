from .models import FormInfoHandler, Product
from django.forms import ModelForm
from django_select2 import forms as s2forms


class FormInfoHandlerModelForm(ModelForm):
    class Meta:
        model = FormInfoHandler
        fields = ['id_state', 'selling_price']
        widgets = {
            'id_state': s2forms.Select2MultipleWidget
        }


class FormProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
