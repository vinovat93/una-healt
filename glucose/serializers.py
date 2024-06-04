from rest_framework import serializers

from .models import Glucose


class LevelsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    device = serializers.CharField(max_length=255)
    serial_number = serializers.CharField(max_length=100)
    device_timestamp = serializers.DateTimeField()
    record_type = serializers.IntegerField(default=0)
    glucose_history = serializers.DecimalField(max_digits=5, decimal_places=2)
    glucose_scan = serializers.DecimalField(max_digits=5, decimal_places=2)
    non_numeric_rapid_acting_insulin = serializers.CharField(max_length=500)
    rapid_acting_insulin = serializers.IntegerField(default=0)
    non_numeric = serializers.CharField(max_length=500)
    food_data = serializers.CharField(max_length=500)
    carbohydrates_grams = serializers.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates_servings = serializers.DecimalField(max_digits=5, decimal_places=2)
    non_numeric_depot_insulin = serializers.CharField(max_length=500)
    depot_insulin = serializers.IntegerField(default=0)
    notes = serializers.CharField()
    glucose_test_strip = serializers.DecimalField(max_digits=5, decimal_places=2)
    ketone = serializers.DecimalField(max_digits=5, decimal_places=2)
    mealtime_insulin = serializers.IntegerField(default=0)
    correction_insulin = serializers.IntegerField(default=0)
    user_insulin_change = serializers.IntegerField(default=0)

    class Meta:
        model = Glucose
        fields = '__all__'

    def create(self, validated_data):
        return Glucose.objects.create(**validated_data)
