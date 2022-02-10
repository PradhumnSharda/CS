

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from customers.forms import customer_order_form
from customers.models import customer_order_model
from django.shortcuts import get_object_or_404
from tyre_stock.models import tyre_stockmodel
from customers.filters import OrderFilter
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.

def employee_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tyre_page'))
        else:
            return HttpResponse('Wrong combination of details!')

    else:
        return render(request, 'customers/customer_login.html', {})

@login_required
def employee_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('customers:employee_login'))


@login_required
def customer_order_view(request):

    order_form = customer_order_form()


    if request.method == 'POST':
        order_form = customer_order_form(request.POST)

        if order_form.is_valid:
            order_form.save(commit=False)
            try:
                validate_email(order_form.cleaned_data['mail_id'])
                valid_email = True
            except ValidationError:
                valid_email = False

            if valid_email==False:
                return render(request, 'customers/mail_error.html')
            else:
                tyre = tyre_stockmodel.objects.get(tyre_name=order_form.cleaned_data['tyre_model'])

                if int(order_form.cleaned_data['quantity']) > int(tyre.number_of_tyres):
                    return HttpResponse('Tyre quantity for sale is greater than the available tyres')
                else:
                    tyre.number_of_tyres = tyre.number_of_tyres - int(order_form.cleaned_data['quantity'])

                    send_mail(
                        'Tyre receipt for your order of tyre model: '+ str(tyre.tyre_name),
                        "Customer name: "+ str(order_form.cleaned_data['customer_name'])+
                            "\n"+ "Phone number: "+ str(order_form.cleaned_data['phone_number'])+
                            "\n"+ "Tyre model: "+ str(tyre.tyre_name)+
                            "\n" + "Quantity bought: "+str(order_form.cleaned_data['quantity'])+
                            "\n" +"Tyre price: "+ str(tyre.price)+
                            "\n" +"Total price: "+ str(int(tyre.price)*int(order_form.cleaned_data['quantity'])),
                            'jktyrenbh@gmail.com',
                            [str(order_form.cleaned_data['mail_id'])],
                            fail_silently=False,
                    )

                    tyre.save()
                    order_form.save()

            if int(tyre.reorder_number) >= int(tyre.number_of_tyres):

                send_mail(
                    'Tyre quantity below the pre-set reorder number of '+ str(tyre.tyre_name),
                    "Tyre model: "+ str(tyre.tyre_name)+ "\n" + "Number of tyres available: "+str(tyre.number_of_tyres),
                    'jktyrenbh@gmail.com',
                    ['pradhumn.ansh@gmail.com'],
                    fail_silently=False,
                )

            return HttpResponseRedirect(reverse('customers:all_orders'))
    else:
        return render(request, 'customers/customer_order.html', {'order_form':order_form})


#@login_required
#def all_orders(request):
#    orders = customer_order_model.objects.order_by('date')
#    return render(request,'customers/all_orders.html', {'orders':orders})

@login_required
def all_orders(request):
    orders = customer_order_model.objects.all().order_by('-id')

    order_filter = OrderFilter(request.GET, queryset=orders)

    x=0
    for money in orders:
        if money.payment_done == False:
            x = x+ int(int(money.quantity) * int(money.tyre_model.price))


    return render(request, 'customers/all_orders.html', {'filter': order_filter, 'orders':orders, 'x':x})

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = customer_order_model
    context_object_name = 'order_detail'
    template_name='customers/order_detail.html'

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = customer_order_model
    fields = ['customer_name', 'company_name', 'phone_number', 'payment_done', 'vehicle_number', 'location', 'tyre_number', 'fitment_position']
    template_name = 'customers/order_c_u.html'

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = customer_order_model
    context_object_name = 'order_delete'
    success_url = reverse_lazy('customers:all_orders')
    template_name = 'customers/order_delete.html'

    def delete(self, *args, **kwargs):

        self.object = self.get_object()
        dummy_number = self.object.quantity


        tyre = tyre_stockmodel.objects.get(tyre_name=self.object.tyre_model)
        tyre.number_of_tyres = tyre.number_of_tyres + int(dummy_number)
        tyre.save()
        self.object.delete()
        success_url = reverse_lazy('customers:all_orders')

        return HttpResponseRedirect(success_url)

        #return super(OrderDeleteView, self).delete(*args, **kwargs)
