from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about-us/", views.about, name="about"),
    path("packages/", views.packages, name="packages"),
    path("timeline/", views.timeline, name="timeline"),
    path("contact-us/", views.contact, name="contact"),
]
