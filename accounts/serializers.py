from dataclasses import field
from locale import currency
from django.forms import models
from django.test import client
from django.contrib.auth.models import User
from numpy import source
from requests import delete
from rest_framework import serializers
from .models import Account
from .choices import UserTypeChoices
from . import models




class AccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = Account
        exclude = ('user_permissions', 'groups',
                   'is_admin', 'is_staff', 'is_superuser',)

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = Account(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


class AccountEditSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    username = serializers.CharField()
    user_type = serializers.ChoiceField(UserTypeChoices)

    class Meta:
        model = Account
        fields = ("email", "username", "department_name", "user_type")

        extra_kwargs = {"password": {"write_only": True}}




class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        exclude = ('user_permissions', 'groups',
                   'is_admin', 'is_staff', 'is_superuser',)

        extra_kwargs = {"password": {"write_only": True}}
