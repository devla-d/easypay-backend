from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db import models

from uuid import uuid4


def transactioncode():
    code = str(uuid4()).replace(" ", "-").upper()[:10]
    return f"{code}"


class Bank(models.Model):
    acc_name = models.CharField(max_length=50, blank=True, null=True)
    acc_num = models.CharField(max_length=50, blank=True, null=True)
    ty_pe = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.ty_pe} "


class Packages(models.Model):

    hours = models.IntegerField()
    name = models.CharField(max_length=40)
    percent = models.IntegerField()
    min_amount = models.IntegerField(default=0)
    max_amount = models.IntegerField(default=0)
    ref_percent = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Transactions(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=40, default="pending")
    mode = models.CharField(max_length=50)
    paymethod = models.CharField(max_length=50, blank=True, null=True)
    ref = models.CharField(
        max_length=50, default=transactioncode(), blank=True, null=True
    )
    bank_details = models.ForeignKey(
        Bank, related_name="trans_bank", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} :  {self.paymethod}"


STATUS = (
    ("active", "active"),
    ("inactive", "inactive"),
    ("completed", "completed"),
)


class Investments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_invested = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=40, choices=STATUS, default="inactive")
    amount_earn = models.IntegerField(default=0)
    package = models.ForeignKey(
        Packages, on_delete=models.CASCADE, related_name="pack", blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} :  {self.amount_invested}"
