from django.core.validators import MinValueValidator

from .models import FormInfoHandler, Product
from django.forms import *
from django_select2 import forms as s2forms


class FormInfoHandlerModelForm(ModelForm):
    class Meta:
        model = FormInfoHandler
        fields = ['id_state', 'selling_price']
        widgets = {
            'id_state': s2forms.Select2MultipleWidget
        }

    def __init__(self, *args, **kwargs):
        super(FormInfoHandlerModelForm, self).__init__(*args, **kwargs)
        self.fields['id_state'].label = "Stany"
        self.fields['selling_price'].label = "Za ile chcesz sprzedac jedna sztuke [w $]"


class FormProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_price', 'id_cat', 'product_name']

    def __init__(self, *args, **kwargs):
        super(FormProductModelForm, self).__init__(*args, **kwargs)
        self.fields['product_price'].label = "Cena produktu [w $]"
        self.fields['id_cat'].label = "Kategoria produktu"
        self.fields['product_name'].label = "Nazwa produktu"

class FormAmountForm(Form):
    ilosc = IntegerField(validators=[MinValueValidator(0)])

    def __init__(self, *args, **kwargs):
        super(FormAmountForm, self).__init__(*args, **kwargs)
        self.fields['ilosc'].label = "Ilość"