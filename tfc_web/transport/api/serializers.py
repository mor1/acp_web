from rest_framework import serializers
from transport.models import VehicleJourney, Line, Stop, SpecialDaysOperation


class VehicleJourneySerializer(serializers.ModelSerializer):
    timetable = serializers.SerializerMethodField()
    special_days_operation = serializers.SerializerMethodField()

    def get_timetable(self, obj):
        return obj.get_timetable().values('order', 'stop_id', 'time')

    def get_special_days_operation(self, obj):
        return SpecialDaysOperation.objects.filter(vehicle_journey=obj)\
            .values('days__lower', 'days__upper', 'operates')

    class Meta:
        model = VehicleJourney
        fields = '__all__'
        depth = 4


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stop
        fields = '__all__'
