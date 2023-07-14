"""
URL configuration for retro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("fixtures/", include("fixtures.urls", namespace="fixtures")),
    path("products/", include("products.urls", namespace="products")),
    path("cart/", include("cart.urls", namespace="cart")),
    # path(
    #     "product_data/",
    #     include("product_data.urls", namespace="product_data"),
    # ),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("ratings/", include("star_ratings.urls", namespace="ratings")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
