from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    # request.session.clear()
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def calculate(request):
    product = Product.objects.get(id = request.POST['product_id'])
    amount = int(request.POST['quantity'])
    request.session['single_charge'] = float(product.price) * amount
    Order.objects.create(quantity_ordered=amount, total_price=request.session['single_charge'])
    return redirect("/checkout")

def checkout(request):
    total_quantity = 0
    total_charges = 0
    for order in Order.objects.all():
        total_quantity += order.quantity_ordered
        total_charges += order.total_price
    context = {
        "quantity_total":total_quantity,
        "charges_amount":total_charges
    }
    return render(request, "store/checkout.html", context)

    # bellow is the method I found on stackoverflow. It's based on using queries, which should be faster than using a for loop
    # "total_quantity": list(Order.objects.aggregate(Sum("quantity_ordered")).values())[0],
    # "total_charges": list(Order.objects.aggregate(Sum("total_price")).values())[0]