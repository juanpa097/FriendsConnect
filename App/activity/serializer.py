import base64
import datetime

import pytz
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from App.activity.model import Activity, ActivityUser
from App.image.serializer import ImageSerializer


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(required=False)
    max_participants = serializers.IntegerField(min_value=0)
    begin_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    image = serializers.SerializerMethodField(required=False)
    date_created = serializers.DateTimeField(required=False)
    author = serializers.CharField(required=False)
    participants = serializers.IntegerField(required=False)
    comments = serializers.IntegerField(required=False)
    is_current_user_subscribed = serializers.BooleanField(required=False)

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'location', 'begin_date',
                  'end_date', 'max_participants', 'visibility', 'image',
                  'date_created', 'author', 'participants', 'comments',
                  'is_current_user_subscribed')

    def create(self, valid_date):
        user_id = valid_date['user']
        valid_date.pop('user')
        activity = Activity.objects.create(**valid_date)
        user = get_object_or_404(User, id=user_id)
        # TODO Change rol to constant
        ActivityUser.objects.create(
            user=user,
            activity=activity,
            rol=0
        )
        return activity

    def validate(self, data):

        now = pytz.UTC.localize(datetime.datetime.now())
        if data['begin_date'] < now:
            raise \
                serializers.ValidationError("Date invalid it must be > to now")
        if data['end_date'] <= data['begin_date']:
            raise serializers.ValidationError("Date end is < to begin")
        return data

    def get_image(self, obj):
        if not obj.image:
            return None
        complete_path = obj.image.file.path
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
