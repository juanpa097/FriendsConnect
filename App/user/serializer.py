import base64

from rest_framework import serializers
from App.user.model import Profile
from django.contrib.auth.models import User
from App.code.mixins import CodeGenMixin


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.Field(write_only=True, required=False)
    image = serializers.SerializerMethodField(
        required=False,
        read_only=True
    )

    class Meta:
        model = Profile
        fields = ('rol', 'about_me', 'image', 'user',)

    def create(self, validated_data, user):
        return Profile.objects.create(user=user, **validated_data)

    def get_image(self, obj):
        if type(obj) != type(Profile):
            return None
        if not obj.image:
            return None
        complete_path = obj.image.file.path
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str


class UserSerializer(
    serializers.ModelSerializer,
    CodeGenMixin
):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'profile')

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
