from .serializers import (
    AQListSerializer, AQConfigSerializer,
    AQDataSerializer)
from api import util, auth
import coreapi
import coreschema
from datetime import datetime
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
import logging
from rest_framework.exceptions import NotFound


logger = logging.getLogger(__name__)

station_id_fields = [
    coreapi.Field(
        "station_id",
        required=True,
        location="path",
        schema=coreschema.String(
            description="Air quality sensor station id (e.g. 'S-1134')"),
        description="Air quality sensor station id (e.g. 'S-1134')",
        example="S-1134",
    ),
]

aq_history_fields = [
    coreapi.Field(
        "station_id",
        required=True,
        location="path",
        schema=coreschema.String(
            description="Air quality station id (e.g. 'S-1134')"),
        description="Air quality station id (e.g. 'S-1134')",
        example="S-1134",
    ),
    coreapi.Field(
        "sensor_type",
        required=True,
        location="path",
        schema=coreschema.String(
            description="Air quality sensor id (e.g. 'NO2')"),
        description="Air quality sensor id (e.g. 'NO2')",
        example="NO2",
    ),
    coreapi.Field(
        "month",
        required=True,
        location="path",
        schema=coreschema.String(
            description="The month for which to return data. YYYY-MM "
                        "(e.g. '2016-06')"),
        description="The month for which to return data. YYYY-MM "
                    "(e.g. '2016-06')",
        example="2016-06",
    ),
]


def get_aq_config(station_id=None):
    if station_id is None:
        return util.get_config('cam_aq')
    else:
        try:
            return util.get_config('cam_aq', station_id,
                                   'aq_list', 'StationID')
        except util.TFCValidationError as e:
            raise NotFound("Station not found: {0}".format(e))


class AQList(auth.AuthenticateddAPIView):
    ''' Return metadata for all stations, including each station's _station_id_.'''
    def get(self, request):
        data = get_aq_config()
        serializer = AQListSerializer(data)
        return Response(serializer.data)


class AQConfig(auth.AuthenticateddAPIView):
    ''' Return metadata for a single station identified by _station_id_.'''
    schema = AutoSchema(manual_fields=station_id_fields)

    def get(self, request, station_id):
        data = get_aq_config(station_id)
        serializer = AQConfigSerializer(data)
        return Response(serializer.data)


class AQHistory(auth.AuthenticateddAPIView):
    ''' Return historic data for a single sensor identified by _sensor_type_
    on a station identified by _station_id_ for a particular _month_.'''
    schema = AutoSchema(manual_fields=aq_history_fields)

    def get(self, request, station_id, sensor_type, month):
        # Note that this validates station_id!
        config = get_aq_config(station_id)

        if sensor_type not in config['SensorTypes']:
            raise NotFound("No sensor '{0}' on station '{1}'"
                           .format(sensor_type, station_id))

        try:
            month = datetime.strptime(month, '%Y-%m')
        except ValueError:
            raise util.TFCValidationError(
                "Month '{0}' has the wrong format. Use YYYY-MM".format(month))

        try:
            filename = (
                'cam_aq/data_bin/{1:%Y}/{1:%m}/{0}/{0}_{2}_{1:%Y-%m}.json'
                .format(station_id, month, sensor_type)
                )
            results = util.read_json(filename)
        except FileNotFoundError:
            raise NotFound("No data found for station '{0}', sensor '{1}', "
                           "month '{2:%Y-%m}'"
                           .format(station_id, sensor_type, month))

        serializer = AQDataSerializer(results)
        return Response(serializer.data)
