from django.urls import path
from .views import (
    DashAPIView,
    get_pacakges,
    create_investment,
    end_user_investment,
    WithdrawApiview,
    TransactionsView,
    SettingsApiview,
)


urlpatterns = [
    path("dashboard/", DashAPIView.as_view()),
    path("get-packages/", get_pacakges),
    path("create-investment/", create_investment),
    path("withdrawal-funds/", WithdrawApiview.as_view()),
    path("transaction-log/", TransactionsView.as_view()),
    path("end-investment/", end_user_investment),
    path("settings/", SettingsApiview.as_view()),
]
