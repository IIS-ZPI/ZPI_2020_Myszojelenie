from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def index(request):
    stany = State.objects.all()
    produkty = Product.objects.all()

    zysk = None
    if request.method == 'POST':
        data = request.POST.copy()
        stan = data.get('id_state')
        produkt = data.get('id_product')

        selling_price = float(data.get('selling_price'))
        product_price = produkty[int(produkt) - 1].product_price
        tax = stany[int(stan) - 1].state_base_tax

        zysk = round((selling_price - product_price * (1 + tax)) / (1 + tax), 4)

    return render(request, "Myszojelen/index.html", {"zysk": zysk})


def adding_form(request):
    form = modelform_factory(FormInfoHandler, fields='__all__')
    return render(request, 'Myszojelen/adding.html', {"formset": form})
