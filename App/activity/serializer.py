import datetime

import pytz
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from App.activity.model import Activity, ActivityUser


class ActivitySerializer(serializers.ModelSerializer):
    # location = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField(required=False)
    max_participants = serializers.IntegerField(min_value=0)
    due_date = serializers.DateTimeField()

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'location', 'due_date',
                  'max_participants', 'visibility')

    def create(self, valid_date):
        user_id = valid_date['user']
        valid_date.pop('user')
        activity = Activity.objects.create(**valid_date)
        user = get_object_or_404(User, id=user_id)
        ActivityUser.objects.create(
            user=user,
            activity=activity,
            rol=1
        )
        return activity

    def validate(self, data):

        now = pytz.UTC.localize(datetime.datetime.now())
        if data['due_date'] < now:
            raise \
                serializers.ValidationError("Date invalid it must be > to now")
        return data


class ActivityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'name', 'due_date', 'max_participants')
