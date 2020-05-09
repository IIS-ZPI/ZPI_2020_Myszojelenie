from .models import FormInfoHandler, Product
from django.forms import ModelForm

class FormInfoHandlerModelForm(ModelForm):
    class Meta:
        model = FormInfoHandler
        fields = ['id_state','selling_price']
class FormProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
