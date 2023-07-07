from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Customer
from .forms import CustomerProfileForm


def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(Customer, user=request.user)

    if request.method == "POST":
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = CustomerProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "accounts/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)
