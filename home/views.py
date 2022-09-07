from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


def packages(request):
    return render(request, "home/packages.html")


def timeline(request):
    return render(request, "home/timeline.html")


def contact(request):
    return render(request, "home/contact.html")
