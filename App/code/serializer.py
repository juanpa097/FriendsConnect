from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from App.code.model import CodeValidate
from django.contrib.auth.models import User


class ForgotPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField()

    class Meta:
        model = CodeValidate
        fields = ('code', 'password', 'email')

    def create(self, validated_data):
        email = validated_data.get('email')
        user = get_object_or_404(User, email=email)
        user.set_password(validated_data['password'])
        user.save()
        code = validated_data['code']
        code = get_object_or_404(CodeValidate, code=code, user=user)
        return {
            'code': code.code,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }

    def validate(self, attrs):
        email = attrs.get('email')
        user = get_object_or_404(User, email=email)
        code = attrs.get('code')
        code = get_object_or_404(CodeValidate, code=code, user=user)
        return attrs
