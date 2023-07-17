"""
Module for error Handler views
"""
from django.shortcuts import render


def handler403(request, exception=None):
    """Error Handler 403"""
    return render(request, "error_handlers/403.html", status=403)


def handler404(request, exception=None):
    """Error Handler 404"""
    return render(request, "error_handlers/404.html", status=404)


def handler500(request, exception=None):
    """Error Handler 500"""
    return render(request, "error_handlers/500.html", status=500)
