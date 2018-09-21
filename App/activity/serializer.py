from rest_framework import serializers

from App.activity.model import Activity


class ActivitySerializer(serializers.ModelSerializer):
    ###location = serializers.ReadOnlyField()

    class Meta:
        model = Activity
        fields = ('name', 'description', 'location', 'due_date', 'max_participants', 'visibility')
        ###fields = ('name', 'description', 'location', 'due_date', 'max_participants', 'visibility', 'User_Activity_id')




