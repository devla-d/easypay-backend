from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from enapp import utils

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,  # validators=[validate_password]
    )

    ref_code = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
            "email",
            "phone",
            "btc_id",
            "usdt_id",
            "perfect_money_id",
            "password",
            "ref_code",
        ]

        extra_kwargs = {
            "btc_id": {"required": False},
            "usdt_id": {"required": False},
            "perfect_money_id": {"required": False},
            "username": {"required": False},
        }

    def save(self):

        account = User(
            full_name=self.validated_data["full_name"],
            username=utils.user_unique_id(),
            email=self.validated_data["email"],
            phone=self.validated_data["phone"],
            btc_id=self.validated_data["btc_id"],
            usdt_id=self.validated_data["usdt_id"],
            perfect_money_id=self.validated_data["perfect_money_id"],
        )
        password = self.validated_data["password"]
        account.set_password(password)

        account.save()
        return account


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
            "email",
            "phone",
            "btc_id",
            "usdt_id",
            "perfect_money_id",
            "balance",
            "deposit_balance",
            "total_withdraw",
            "last_login",
            "date_joined",
            "referral_balance",
            "referral",
        ]
