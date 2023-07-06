from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse("cart:view_cart"))

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.update_total()
            order.save()
            messages.success(
                request, "Your order has been placed successfully!"
            )
            # Clear the cart or perform any other necessary actions
            return redirect(reverse("order:order_success"))
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        order_form = OrderForm()

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
    }

    return render(request, template, context)
