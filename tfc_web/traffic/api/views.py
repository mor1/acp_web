from datetime import timedelta
import logging

from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import (
    ZoneListSerializer, ZoneConfigSerializer, ZoneHistorySerializer)
from api import util, auth


logger = logging.getLogger(__name__)


def get_zone_config(zone_id=None):
    if zone_id is None:
        return util.get_config('zone')
    else:
        try:
            return util.get_config('zone', zone_id,
                                   'zone_list', 'zone.id')
        except (util.TFCValidationError) as e:
            raise NotFound("Zone not found: {0}".format(e))


def swap_dot_and_underscore(data):
    ''' serializer can't cope with '.' in keys - switch to '_' '''
    return {key.replace('.', '_'): value for (key, value) in data.items()}


class ZoneList(auth.AuthenticateddAPIView):
    '''
    List metadata for all known zones, including each zone's
    zone_id
    '''
    def get(self, request):
        data = get_zone_config()
        # serializer can't cope with '.' in keys - switch to '_'
        fixed_zones = []
        for zone in data['zone_list']:
            fixed_zone = swap_dot_and_underscore(zone)
            fixed_zones.append(fixed_zone)
        serializer = ZoneListSerializer({"zone_list": fixed_zones})
        return Response(serializer.data)


class ZoneConfig(auth.AuthenticateddAPIView):
    '''
    Return the metadata for a single zone identified by zone_id
    '''
    def get(self, request, zone_id):
        data = get_zone_config(zone_id)
        serializer = ZoneConfigSerializer(swap_dot_and_underscore(data))
        return Response(serializer.data)


class ZoneHistory(auth.AuthenticateddAPIView):
    '''
    Return historic zone data for the single zone identified by zone_id.
    Data is returned in 24-hour chunks from start_date to end_date
    inclusive. A most 31 day's data can be retrieved in a single request.
    '''
    schema = util.list_args_schema

    def get(self, request, zone_id):

        args = util.ListArgsSerializer(data=request.query_params)
        args.is_valid(raise_exception=True)

        # Note that this validates zone_id!
        get_zone_config(zone_id)

        start_date = args.validated_data.get('start_date')
        end_date = args.validated_data.get('end_date')
        if end_date is None:
            end_date = start_date
        day_count = (end_date - start_date).days + 1

        results = []
        for date in (start_date + timedelta(n) for n in range(day_count)):
            try:
                filename = (
                    'cloudamber/sirivm/data_zone/'
                    '{1:%Y}/{1:%m}/{1:%d}/{0}_{1:%Y-%m-%d}.txt'
                    .format(zone_id, date)
                    )
                results = results + util.read_json_fragments(filename)
            except (FileNotFoundError):
                pass
        serializer = ZoneHistorySerializer({'request_data': results})
        return Response(serializer.data)