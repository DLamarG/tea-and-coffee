from rest_framework import serializers
from .models import Tea


class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = ['name', 'description', 'picture', 'caffeine', 'rating']

    def create(self, validated_data):
        # Custom validation logic goes here
        # For example, you can add additional checks on the data

        # Call the default create method to actually create the object
        tea = Tea.objects.create(**validated_data)

        return tea