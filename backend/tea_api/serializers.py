from rest_framework import serializers
from .models import Tea
from tea_reviews.serializers import ReviewSerializer

class TeaSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Tea
        fields = ['name', 'description', 'picture', 'caffeine', 'rating', 'reviews']

    def create(self, validated_data):
        # Custom validation logic goes here
        # For example, you can add additional checks on the data

        # Call the default create method to actually create the object
        coffee = Tea.objects.create(**validated_data)

        return coffee