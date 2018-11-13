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

    def update(self, instance, validated_data):
        instance.about_me = validated_data.get('about_me', instance.about_me)
        instance.save()
        return instance

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

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name',
            instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name',
            instance.last_name
        )
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        profile = validated_data.get('profile', None)
        if profile:
            profile_serializer = \
                ProfileSerializer(instance.profile, data=profile)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save()
        return instance
