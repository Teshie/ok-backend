from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
#import permission
from rest_framework import permissions

from statistics import mode
from .models import *
from . import serializers
from accounts import models
from rest_framework import generics
from django.contrib.auth.models import User
from .choices import *
from utils.permissions import *



class CreateProfile(APIView):
    """Create User Profile Api"""

    permission_classes = [AllowAny]

    def post(self, request):
        """Handles creating profile object"""
        serializer = serializers.AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    **serializers.AccountDetailSerializer(
                        user, context={"request": request}
                    ).data,
                    "token": token.key,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(ObtainAuthToken):
    """Checks "phone no and password" and returns auth token and user data."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = serializers.AccountDetailSerializer(
            user, context={"request": request}
        )
        return Response(
            {
                "token": token.key,
                "user": user_serializer.data,
            }
        )

class AccountList(generics.ListAPIView):
    """List all users"""
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer
    # permission_classes = [IsClientAdmin]



@api_view(
    ["GET"],
)
def get_user_types(request):
    return Response(
        [
            {"value": UserTypeChoices.CEO, "text": "Chief Executive Officer"},
            {"value": UserTypeChoices.HoD, "text": "Department Head"},
            {"value": UserTypeChoices.SUB, "text": "Sub Department"},
            {"value": UserTypeChoices.CLIENT_ADMIN, "text": "Client Admin"},
        ]
    )


