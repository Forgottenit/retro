from django.shortcuts import render

# Create your views here.


def index(request):
    """Returns Index page"""

    return render(request, "home/index.html")


def privacy_policy(request):
    with open(
        "home/templates/home/privacy_policy/privacy_policy.txt", "r"
    ) as file:
        data = file.read().replace("\n", "<br/>")
    return render(request, "home/privacy_policy.html", {"policy": data})
