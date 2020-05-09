from django.shortcuts import render
from .forms import *

from .models import *


def index(request):
    zysk = None
    if request.method == 'POST':
        data = request.POST.copy()
        selling_price = float(data.get('selling_price'))
        state = State_Category_Tax.objects.filter(id_cat=int(data.get('id_cat')),
                                                  id_state=int(data.get('id_state')))
        product_price = float(data.get('product_price'))
        if state.exists():
            tax = state[0].tax_val
        else:
            stan = State.objects.get(id=int(data.get('id_state')))
            tax = stan.state_base_tax

        zysk = round((selling_price - product_price * (1 + tax)) / (1 + tax), 4)

    return render(request, "Myszojelen/index.html", {"zysk": zysk})


def adding_form(request):
    forminfo = FormInfoHandlerModelForm
    formprod = FormProductModelForm
    context = {
        "forminfo": forminfo,
        "formprod": formprod,
    }
    return render(request, 'Myszojelen/adding.html', context)
