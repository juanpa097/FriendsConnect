from rest_framework import serializers
from App.user.model import Profile
from django.contrib.auth.models import User
from App.code.mixins import CodeGenMixin


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.Field(write_only=True, required=False)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data, user):
        return Profile.objects.create(user=user, **validated_data)


class UserSerializer(
    serializers.ModelSerializer,
    CodeGenMixin
):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user_model = ProfileSerializer(data=profile_data)
        if user_model.is_valid():
            user_model.create(profile_data, user)
        self.generate_user_validate_code(user)
        return user
