'''
Views.py file for Payments app
'''
import os
from datetime import date

import stripe
from django.shortcuts import HttpResponse, render

from authentication.models import MyUser

from .forms import OrderForm
from .models import Order


def render_payment_form(request):
    '''
    Render the payment form onscreen
    '''
    stripe.api_key = os.getenv('STRIPE_SECRET')

    intent = stripe.PaymentIntent.create(
        amount=30,
        currency='gbp',
    )

    order_form = OrderForm()

    return render(
        request,
        'payment_form.html',
        {
            'cs': intent.client_secret,
            'o_form': order_form
        }
    )


def add_order(request):
    '''
    Add an order to the system
    '''
    if request.method == 'POST':
        if request.user:
            try:
                user = MyUser.objects.get(user_id=request.user.id)
                Order.objects.create(
                    user=user,
                    full_name=request.POST['full_name'],
                    street_address1=request.POST['street_address_1'],
                    street_address2=request.POST['street_address_2'],
                    town_or_city=request.POST['town_or_city'],
                    county=request.POST['county'],
                    country=request.POST['country'],
                    phone_number=request.POST['phone_number'],
                    date=date.today(),
                    amount=request.POST['amount'],
                    confirmation_code=request.POST['confirmation_code']
                )
            except MyUser.DoesNotExist:
                pass
            finally:
                Order.objects.create(
                    full_name=request.POST['full_name'],
                    street_address1=request.POST['street_address_1'],
                    street_address2=request.POST['street_address_2'],
                    town_or_city=request.POST['town_or_city'],
                    county=request.POST['county'],
                    country=request.POST['country'],
                    phone_number=request.POST['phone_number'],
                    date=date.today(),
                    amount=request.POST['amount'],
                    confirmation_code=request.POST['confirmation_code']
                )
        else:
            Order.objects.create(
                full_name=request.POST['full_name'],
                street_address1=request.POST['street_address_1'],
                street_address2=request.POST['street_address_2'],
                town_or_city=request.POST['town_or_city'],
                county=request.POST['county'],
                country=request.POST['country'],
                phone_number=request.POST['phone_number'],
                date=date.today(),
                amount=request.POST['amount'],
                confirmation_code=request.POST['confirmation_code']
            )
        return HttpResponse(status=200)
    return HttpResponse(status=403)
