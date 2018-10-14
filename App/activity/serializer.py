import datetime

import pytz
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from App.activity.model import Activity


class ActivitySerializer(serializers.ModelSerializer):
    # location = serializers.ReadOnlyField()
    max_participants = serializers.IntegerField(min_value=0)
    due_date = serializers.DateTimeField()

    class Meta:
        model = Activity
        fields = ('name', 'description', 'location', 'due_date',
                  'max_participants', 'visibility', 'user_activity_id')

    def create(self, valid_date):
        user_id = valid_date['user_activity_id']
        valid_date['user_activity_id'] = get_object_or_404(User, id=user_id)
        return Activity.objects.create(**valid_date)

    def validate(self, data):

        now = pytz.UTC.localize(datetime.datetime.now())
        if data['due_date'] < now:
            raise \
                serializers.ValidationError("Date invalid it must be > to now")
        return data
