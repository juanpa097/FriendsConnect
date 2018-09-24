from rest_framework import serializers
from App.user.model import UserModel
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    user = serializers.Field(write_only=True, required=False)

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data, user):
        return UserModel.objects.create(user=user, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    usermodel = UserModelSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'usermodel')

    def create(self, validated_data):
        profile_data = validated_data.pop('usermodel')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user_model = UserModelSerializer(data=profile_data)
        if user_model.is_valid():
            user_model.create(profile_data, user)
        return user
