from rest_framework import serializers

from App.activity.model import Activity


class ActivitySerializer(serializers.ModelSerializer):
    location = serializers.ReadOnlyField()

    class Meta:
        model = Activity
        fields = '__all__'
        # fields = ('name', 'description')

    ##def create(self, validate_data):
      ##  return Activity.objects.create(**validate_data)


