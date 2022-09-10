from django.conf import settings
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import get_template


from datetime import timedelta
from uuid import uuid4
from django.contrib.auth import get_user_model


User = get_user_model()


EMAIL_ADMIN = settings.DEFAULT_FROM_EMAIL
D = "DEPOSIT"
W = "WITHDRAW"
PED = "PENDING"
ACT = "ACTIVE"
SUC = "SUCCESS"
DEC = "DECLINED"


def earnings(amount, perc):
    p = (perc / 100) * amount
    return p + amount


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def validate_email(email):
    try:
        acc = User.objects.get(email=email)
    except User.DoesNotExist:
        acc = None
    return acc


def validate_username(username):
    account = None
    try:
        account = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if account != None:
        return username


def check_perfect_money_id(user):
    if user.perfect_money_id == "" or user.perfect_money_id == None:
        return None
    return True


def check_btc_id(user):
    if user.btc_id == "" or user.btc_id == None:
        return None
    return True


def check_usdt_id(user):
    if user.usdt_id == "" or user.usdt_id == None:
        return None
    return True


def user_unique_id():
    code = str(uuid4()).replace(" ", "").upper()[:7]
    return code


def tx_ref():
    code = str(uuid4()).replace(" ", "-").upper()[:7]
    return f"ean-{code}"


def get_investment_end(h):
    return timezone.now() + timedelta(hours=h)


def send_regMail(user):
    subject = "EARNALIPAY -- Email verification"
    context = {
        "user": user,
        "domain": "earnalipay.com",
    }
    message = get_template("accounts/welcomeemail.html").render(context)
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=EMAIL_ADMIN,
        to=[user.email],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    mail.send(fail_silently=True)
