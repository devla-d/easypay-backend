from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    full_name = models.CharField(
        verbose_name="fullname", max_length=100, blank=True, null=True
    )

    balance = models.FloatField(default=0)

    deposit_balance = models.FloatField(default=0, blank=True, null=True)
    total_withdraw = models.FloatField(default=0, blank=True, null=True)

    phone = models.CharField(max_length=30, blank=True, null=True)

    btc_id = models.CharField(max_length=50, blank=True, null=True)
    eth_id = models.CharField(max_length=50, blank=True, null=True)
    usdt_id = models.CharField(max_length=50, blank=True, null=True)

    perfect_money_id = models.CharField(max_length=50, blank=True, null=True)
    referral_balance = models.IntegerField(default=0, blank=True, null=True)
    referral = models.IntegerField(default=0, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class Referral(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="ref_user"
    )
    referred_by = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="ref_by_user",
        null=True,
        blank=True,
    )
    referrals = models.ManyToManyField(Account, related_name="my_referrals")

    def __str__(self):
        return self.user.username


class LoginHistory(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    ip_add = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} {self.ip_add}"
