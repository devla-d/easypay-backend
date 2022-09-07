from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="admin-dashboard"),
    path("users/", views.users, name="admin-users"),
    path("users/<int:pk>", views.user_detail, name="admin-user-detail"),
    path("withdrawals/", views.withdrawal_, name="admin-withdrawal"),
    path(
        "withdrawals/<int:pk>", views.withdrawal_detail, name="admin-withdrawal-detail"
    ),
    path("deposits/", views.deposit_, name="admin-deposit"),
    path("investments/", views.investments, name="admin-investments"),
    path(
        "investments/<int:pk>",
        views.investments_detail,
        name="admin-investments-detail",
    ),
]
