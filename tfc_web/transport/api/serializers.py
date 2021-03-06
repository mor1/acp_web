from rest_framework import serializers
from transport.models import VehicleJourney, Line, Stop, Timetable, Operator


class VehicleJourneySerializer(serializers.ModelSerializer):
    timetable = serializers.SerializerMethodField()

    def get_timetable(self, obj):
        return TimetableSerializerForJourney(obj.get_timetable(), many=True).data

    class Meta:
        model = VehicleJourney
        fields = '__all__'
        depth = 4


class VehicleJourneySummarisedSerializer(serializers.ModelSerializer):
    timetable = serializers.SerializerMethodField()
    direction = serializers.CharField(source='journey_pattern.direction')
    route_description = serializers.CharField(source='journey_pattern.route.description')

    def get_timetable(self, obj):
        return TimetableSerializerForJourney(obj.get_timetable(), many=True).data

    class Meta:
        model = VehicleJourney
        fields = ['id', 'timetable', 'departure_time', 'days_of_week', 'direction', 'route_description']
        depth = 3


class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operator
        fields = ['id', 'code', 'short_name', 'trading_name']


class LineSerializer(serializers.ModelSerializer):
    operator = serializers.SerializerMethodField()

    def get_operator(self, obj):
        return OperatorSerializer(obj.operator).data

    class Meta:
        model = Line
        fields = ['id', 'line_name', 'description', 'standard_origin', 'standard_destination', 'operator']
        depth = 2


class StopSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='atco_code')
    stop_id = serializers.CharField(source='atco_code')
    lat = serializers.FloatField(source='latitude')
    lng = serializers.FloatField(source='longitude')

    class Meta:
        model = Stop
        fields = ['id', 'stop_id', 'atco_code', 'naptan_code', 'common_name', 'indicator',
                  'locality_name', 'latitude', 'longitude', 'lat', 'lng']


class TimetableSerializerForJourney(serializers.ModelSerializer):
    stop = serializers.SerializerMethodField()

    def get_stop(self, obj):
        return StopSerializer(obj.stop).data

    class Meta:
        model = Timetable
        fields = ['order', 'stop', 'time']
        depth = 2
