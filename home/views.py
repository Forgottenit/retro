from django.shortcuts import render

# Create your views here.


def index(request):
    """ "
    Function to return the index page.

    Parameters:
    - request: HTTP request

    Returns:
    - Rendered index page.
    """

    return render(request, "home/index.html")


def privacy_policy(request):
    """
    Function to return the privacy policy page.

    Parameters:
    - request: HTTP request

    Returns:
    - Rendered privacy policy page.
    """
    with open(
        "home/templates/home/privacy_policy/privacy_policy.txt",
        "r",
        encoding="utf-8",
    ) as file:
        data = file.read().replace("\n", "<br/>")
    return render(request, "home/privacy_policy.html", {"policy": data})
