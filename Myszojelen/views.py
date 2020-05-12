from django.shortcuts import render
from .forms import *

from .models import *
from .calculations_holder import CalculationsHolder

list_of_calculation_holders = []


def index(request):
    context = {
        "display_list": list_of_calculation_holders,
    }
    if request.method == 'POST':
        data = request.POST.copy()
        selling_price = float(data.get('selling_price'))
        state = State_Category_Tax.objects.filter(id_cat=int(data.get('id_cat')),
                                                  id_state=int(data.get('id_state')))
        product_price = float(data.get('product_price'))
        if state.exists():
            tax = state[0].tax_val
            state_name = state[0].id_state.state_name

        else:
            stan = State.objects.get(id=int(data.get('id_state')))
            state_name = stan.state_name
            tax = stan.state_base_tax
        category = Category.objects.get(id=int(data.get('id_cat')))
        zysk = round((selling_price - product_price * (1 + tax)) / (1 + tax), 4)
        list_of_calculation_holders.append(
            CalculationsHolder(state=state_name,
                               cat=category.category_name,
                               pronam=data.get('product_name'),
                               prounipr=product_price,
                               proselpri=selling_price,
                               calpri=zysk))
        list_of_calculation_holders.sort()

    return render(request, "Myszojelen/index.html", context)


def adding_form(request):
    forminfo = FormInfoHandlerModelForm
    formprod = FormProductModelForm
    context = {
        "forminfo": forminfo,
        "formprod": formprod,
    }
    return render(request, 'Myszojelen/adding.html', context)
