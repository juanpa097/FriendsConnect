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

    def validate(self, attrs):
        email = attrs.get('email')
        user = get_object_or_404(User, email=email)
        code = attrs.get('code')
        code = get_object_or_404(CodeValidate, code=code)
        if code.user.id != user.id :
            raise ValidationError({
                'ErrorCode': 'The code not correspond with this user.'
            })
        return attrs
