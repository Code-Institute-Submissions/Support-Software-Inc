import os

from django.shortcuts import render, HttpResponse
from .models import Order
from .forms import OrderForm
from datetime import date
import stripe


def render_payment_form(request):

    # Set your secret key: remember to switch to your live secret key in
    # production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
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
    if request.method == 'POST':
        Order.objects.create(
            full_name=request.POST['full_name'],
            street_address1=request.POST['street_address_1'],
            street_address2=request.POST['street_address_2'],
            town_or_city=request.POST['town_or_city'],
            county=request.POST['county'],
            country=request.POST['country'],
            phone_number = request.POST['phone_number'],
            date=date.today(),
            amount=request.POST['amount'],
            confirmation_code=request.POST['confirmation_code']   
        )
        return HttpResponse(status=200)  
    return HttpResponse(status=403)