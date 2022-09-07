from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes


from enapp import utils

from .serializers import RegisterSerializer, ProfileSerializer
from .models import Referral, LoginHistory, Account


class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        ref_code = request.data.get("ref_code", "0")

        if serializer.is_valid():
            if ref_code and utils.validate_username(ref_code) != None:
                instance = serializer.save()
                try:
                    old_user = Account.objects.get(username=ref_code)
                except Account.DoesNotExist:
                    return Response({"error": "UNKNOWN ERROR IN REFERRALS"})

                referred_by = Referral.objects.get(user=old_user)
                my_referral = Referral.objects.get(user=instance)

                referred_by.referrals.add(instance)
                old_user.referral_bonus += 10
                old_user.referral += 1
                old_user.save()
                my_referral.referred_by = old_user
                my_referral.save()
            else:
                serializer.save()
            return Response({"success": "Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ObtainAuthTokenView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        context = {}
        # print(request.data)

        email = request.data.get("email")
        password = request.data.get("password")
        print(email, password)
        browser_type = request.user_agent.browser.family
        browser_version = request.user_agent.browser.version_string

        account = authenticate(email=email, password=password)
        if account:
            LoginHistory.objects.create(
                user=account,
                ip_add=utils.get_client_ip(request),
                device=f"{browser_type} {browser_version}",
            )
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            serializer = ProfileSerializer(account)
            context["success"] = "Successfully authenticated."
            context["user"] = serializer.data
            context["token"] = token.key
        else:
            context["error"] = "Invalid username or password"

        return Response(context)


@api_view(["GET"])
@permission_classes([AllowAny])
def getExistingdata(request):
    existingUserName = []
    existingEmails = []
    users = Account.objects.all()
    for user in users:
        existingEmails.append(user.email)
        existingUserName.append(user.username)

    return Response(
        {"existingEmails": existingEmails, "existingUserName": existingUserName}
    )
