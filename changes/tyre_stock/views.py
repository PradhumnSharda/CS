from django.shortcuts import render
from tyre_stock.models import tyre_stockmodel, new_stock
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tyre_stock.filters import TyreFilter, New_stock_filter
from django.contrib.auth.mixins import LoginRequiredMixin
from tyre_stock.forms import new_stock_form
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from customers.models import customer_order_model
# Create your views here.


#def tyre_stock(request):
#    tyre = tyre_stockmodel.objects.order_by('tyre_name')
#    return render(request, 'tyre_stock/stock_table.html', {'tyre':tyre})

@login_required
def tyre_stock(request):
    tyre_list = tyre_stockmodel.objects.all()
    tyre_filter = TyreFilter(request.GET, queryset=tyre_list)
    x = 0

    for total in tyre_list:
        x = x+ int(total.number_of_tyres)

    return render(request, 'tyre_stock/stock_table.html', {'filter': tyre_filter, 'tyre_list':tyre_list, 'x':x})

def tyre_page(request):
    return render(request, 'tyre_stock/tyre.html', {})

@login_required
def new_stock_view(request):
    form = new_stock_form()

    if request.method == 'POST':
        form = new_stock_form(request.POST)
        if form.is_valid:

            form.save()

            tyre = tyre_stockmodel.objects.get(tyre_name=form.cleaned_data['tyre_name_new'])
            tyre.number_of_tyres = tyre.number_of_tyres + int(form.cleaned_data['quantity'])
            tyre.save()

            return HttpResponseRedirect(reverse('tyre_stock:all_new_stock'))

    return render(request, 'tyre_stock/new_tyre_stock.html', {'form':form})

class New_Stock_DetailView(LoginRequiredMixin, DetailView):
    model = new_stock
    context_object_name = 'tyre_detail'
    template_name = 'tyre_stock/new_tyre_detail.html'

@login_required
def all_new_stock(request):
    stock = new_stock.objects.all().order_by('-id')

    order_filter = New_stock_filter(request.GET, queryset=stock)
    return render(request, 'tyre_stock/all_new_stock.html', {'filter': order_filter, 'stock':stock})

class TyreDetailView(LoginRequiredMixin, DetailView):
    model = tyre_stockmodel
    context_object_name = 'tyre_detail'
    template_name='tyre_stock/tyre_detail.html'

class TyreCreateView(LoginRequiredMixin, CreateView):
    model = tyre_stockmodel
    fields = ('tyre_name', 'number_of_tyres', 'reorder_number', 'price', 'commercial_vehicle_tyre')
    template_name = 'tyre_stock/tyre_c_u.html'

class TyreUpdateView(LoginRequiredMixin, UpdateView):
    model = tyre_stockmodel
    fields = ('tyre_name', 'number_of_tyres', 'reorder_number', 'price', 'commercial_vehicle_tyre')
    template_name = 'tyre_stock/tyre_c_u.html'

class NewTyreUpdateView(LoginRequiredMixin, UpdateView):
    model = new_stock
    fields = ('bought_from')
    template_name = 'tyre_stock/new_stock_update.html'

class TyreDeleteView(LoginRequiredMixin, DeleteView):
    model = tyre_stockmodel
    context_object_name = 'tyre_delete'
    success_url = reverse_lazy('tyre_stock:tyre_stock')
    template_name = 'tyre_stock/tyre_delete.html'
