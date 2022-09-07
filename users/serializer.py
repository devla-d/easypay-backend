from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Investments, Transactions, Packages, Bank
from accounts.models import LoginHistory
from accounts.serializers import ProfileSerializer

User = get_user_model()


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    bank_details = BankSerializer(read_only=True)

    class Meta:
        model = Transactions
        fields = "__all__"


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = "__all__"


class InvestmentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    package = PackagesSerializer(read_only=True)

    class Meta:
        model = Investments
        fields = "__all__"


class LoginhistorySerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = LoginHistory
        fields = "__all__"
