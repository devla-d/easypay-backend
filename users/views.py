from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes


from enapp import utils

from accounts.serializers import ProfileSerializer
from accounts.models import Referral, LoginHistory, Account
from .models import Investments, Transactions, Bank, Packages
from .serializer import (
    InvestmentSerializer,
    PackagesSerializer,
    TransactionSerializer,
    LoginhistorySerializer,
)


class DashAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        context = {}
        try:
            investment = Investments.objects.get(user=user)
            in_serializer = InvestmentSerializer(investment)
            context["investment"] = in_serializer.data
        except Investments.DoesNotExist:
            investment = None
            context["investment"] = investment

        return Response(context, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_pacakges(request):
    packages = Packages.objects.all()
    serializer = PackagesSerializer(packages, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_investment(request):
    user = request.user
    context = {}
    package_id = int(request.data.get("packId"))
    amount = int(request.data.get("amount"))
    package = get_object_or_404(Packages, pk=package_id)
    if user.deposit_balance >= amount:
        if amount not in range(package.min_amount, package.max_amount):
            context["error"] = "Input Amount Between the Selected Plan Price Range"
            return Response(context)

        else:
            investment, created = Investments.objects.get_or_create(user=user)

            investment.end_date = utils.get_investment_end(package.hours)
            investment.start_date = timezone.now()
            investment.status = "active"
            investment.amount_invested = amount
            investment.package = package
            user.deposit_balance -= amount
            user.save()
            investment.save()
            context["success"] = "Your investment Has been Activated"
            return Response(context)

    else:
        context["error"] = "INSUFFICIENT FUNDS,PLEASE DEPOSIT"
        return Response(context)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def end_user_investment(request):
    user = request.user
    investment = get_object_or_404(Investments, user=user)
    investment.status = "completed"
    investment.amount_earn += utils.earnings(
        investment.amount_invested, investment.package.percent
    )
    user.balance += utils.earnings(
        investment.amount_invested, investment.package.percent
    )
    user.save()
    investment.save()
    serializer = InvestmentSerializer(investment)
    return Response({"msg": "Account Credited", "investment": serializer.data})


class WithdrawApiview(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        user = request.user
        paymethod = request.data.get("mode")
        # print(user.btc_id, user.usdt_id)

        amount = int(request.data.get("amount"))
        serializer = ProfileSerializer(user)
        if paymethod == "Perfect money" and user.perfect_money_id == None:
            return Response({"error": "Please add your perfect money in settings"})

        if paymethod == "Bitcoin" and user.btc_id == None:
            print("No res")
            return Response({"error": "Please add your bitcoin wallet in settings"})

        if paymethod == "USDT" and user.usdt_id == None:
            return Response({"error": "Please add your Usdt wallet in settings"})

        if user.balance >= amount:
            transaction = Transactions.objects.create(
                user=user, amount=amount, mode=utils.W, paymethod=paymethod
            )

            if paymethod == "Bank transfer":
                bank = Bank.objects.create(
                    acc_name=request.data.get("acc_name"),
                    acc_num=request.data.get("acc_num"),
                    ty_pe=request.data.get("ty_pe"),
                )

                transaction.bank_details = bank
                transaction.save()

            user.balance -= amount
            user.total_withdraw += amount
            user.save()
            return Response(
                {
                    "msg": "Your Withdraw Request has been submited",
                    "user": serializer.data,
                }
            )

        return Response({"error": "Insufficient Funds"})


class TransactionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        transactions = Transactions.objects.filter(user=user).order_by("-date")
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        transactionId = int(request.data.get("id"))
        transaction = get_object_or_404(Transactions, pk=transactionId, user=user)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)


class SettingsApiview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        loginhistory = LoginHistory.objects.filter(user=user).order_by("-date")
        l_serializer = LoginhistorySerializer(loginhistory, many=True)

        return Response(l_serializer.data)

    def post(self, request, format=None):
        user = request.user
        btc_id = request.data.get("btc_id")
        perfect_money_id = request.data.get("perfect_money_id")
        usdt_id = request.data.get("usdt_id")
        serializer = ProfileSerializer(user)

        user.perfect_money_id = perfect_money_id
        user.btc_id = btc_id
        user.usdt_id = usdt_id
        user.save()
        return Response(serializer.data)
