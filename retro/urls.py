"""
URL configuration for retro project.

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler403, handler404, handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls", namespace="products")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("ratings/", include("star_ratings.urls", namespace="ratings")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "retro.views.handler404"
handler404 = "retro.views.handler404"
handler500 = "retro.views.handler404"
