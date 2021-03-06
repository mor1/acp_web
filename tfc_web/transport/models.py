import datetime
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.postgres.fields import JSONField, DateRangeField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


class Stop(models.Model):
    atco_code = models.CharField(max_length=12, unique=True, primary_key=True, db_index=True)
    naptan_code = models.CharField(max_length=12)
    # plate_code = models.CharField(max_length=12, null=True, blank=True)
    # cleardown_code = models.CharField(max_length=10, null=True, blank=True)
    common_name = models.CharField(max_length=48)
    # common_name_lang = models.CharField(max_length=2, null=True, blank=True)
    # short_common_name = models.CharField(max_length=48, null=True, blank=True)
    # short_common_name_lang = models.CharField(max_length=2, null=True, blank=True)
    # landmark = models.CharField(max_length=48, null=True, blank=True)
    # landmark_lang = models.CharField(max_length=2, null=True, blank=True)
    # street = models.CharField(max_length=48, null=True, blank=True)
    # street_lang = models.CharField(max_length=2, null=True, blank=True)
    # crossing = models.CharField(max_length=48, null=True, blank=True)
    # crossing_lang = models.CharField(max_length=2, null=True, blank=True)
    indicator = models.CharField(max_length=48, null=True, blank=True)
    # indicator_lang = models.CharField(max_length=2, null=True, blank=True)
    # bearing = models.CharField(max_length=2)
    # nptg_locality_code = models.CharField(max_length=8)
    locality_name = models.CharField(max_length=48)
    # parent_locality_name = models.CharField(max_length=48)
    # grand_parent_locality_name = models.CharField(max_length=48)
    # town = models.CharField(max_length=48, null=True, blank=True)
    # town_lang = models.CharField(max_length=2, null=True, blank=True)
    # suburb = models.CharField(max_length=48, null=True, blank=True)
    # suburb_lang = models.CharField(max_length=2, null=True, blank=True)
    # locality_centre = models.BooleanField()
    # grid_type = models.CharField(max_length=1, null=True, blank=True)
    # easting = models.IntegerField()
    # northing = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    # stop_type = models.CharField(max_length=3)
    # bus_stop_type = models.CharField(max_length=3, null=True, blank=True)
    # timing_status = models.CharField(max_length=3, null=True, blank=True)
    # default_wait_time = models.IntegerField(null=True, blank=True)
    # notes = models.TextField(null=True, blank=True)
    # notes_lang = models.CharField(max_length=2, null=True, blank=True)
    # administrative_area_code = models.IntegerField()
    # creation_datetime = models.DateTimeField()
    # modification_datetime = models.DateTimeField(null=True, blank=True)
    # revision_number = models.IntegerField(null=True, blank=True)
    # modification = models.CharField(max_length=3, null=True, blank=True)
    # status = models.CharField(max_length=3, null=True, blank=True)
    gis_location = models.PointField(null=True)
    data = JSONField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def get_coordinates(self):
        return [self.latitude, self.longitude]

    def get_absolute_url(self):
        return reverse('bus-stop', args=(self.atco_code,))

    def get_qualified_name(self):
        return str(self)

    @property
    def locality(self):
        return None

    @python_2_unicode_compatible
    def __str__(self):
        if self.indicator:
            if self.indicator in ('opp', 'adj', 'at', 'o/s', 'nr', 'before', 'after', 'by', 'on', 'in', 'near'):
                return '%s, %s %s' % (self.locality_name, self.indicator, self.common_name) \
                    if self.locality_name else '%s %s' % (self.indicator, self.common_name)
            else:
                return '%s, %s (%s)' % (self.locality_name, self.common_name, self.indicator) \
                    if self.locality_name else '%s (%s)' % (self.common_name, self.indicator)
        else:
            return '%s, %s' % (self.locality_name, self.common_name) if self.locality_name else '%s' % self.common_name


@receiver(pre_save, sender=Stop)
def update_gis_fields(sender, instance, **kwargs):
    instance.gis_location = Point(float(instance.longitude), float(instance.latitude))


class Operator(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    code = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    trading_name = models.CharField(max_length=255)
    last_modified = models.DateTimeField(auto_now=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.trading_name


class Line(models.Model):
    line_id = models.CharField(max_length=255, db_index=True)
    line_name = models.CharField(max_length=255)
    area = models.CharField(max_length=10)  # This is the TNDS zone
    filename = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    operator = models.ForeignKey(Operator, related_name="lines", on_delete=models.CASCADE)
    standard_origin = models.CharField(max_length=255)
    standard_destination = models.CharField(max_length=255)
    regular_days_of_week = models.CharField(max_length=255, null=True)
    bank_holiday_operation = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    stop_list = JSONField(null=True, blank=True)
    timetable = JSONField(null=True, blank=True)
    slug = models.SlugField(max_length=50)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify('-'.join([self.line_name, self.description]))[:49]
        super(Line, self).save(*args, **kwargs)

    def get_stop_list(self):
        stop_list = {}
        for bound in ['inbound', 'outbound']:
            for dayperiod in ['MondayToFriday', 'Saturday', 'Sunday', 'HolidaysOnly']:
                for stop in self.stop_list[bound][dayperiod]:
                    stop_list[stop] = Stop.objects.get(atco_code=stop)
        return stop_list

    def get_all_vehicle_journeys(self):
        return VehicleJourney.objects.filter(journey_pattern__route__line=self).order_by('departure_time')

    def generate_stop_list(self):
        stop_list = {
            'inbound': {
                'MondayToFriday': [],
                'Saturday': [],
                'Sunday': [],
                'HolidaysOnly': []
            },
            'outbound': {
                'MondayToFriday': [],
                'Saturday': [],
                'Sunday': [],
                'HolidaysOnly': []
            }
        }

        for bound in ['inbound', 'outbound']:
            for dayperiod in ['MondayToFriday', 'Saturday', 'Sunday', 'HolidaysOnly']:
                stop_list[bound][dayperiod] = list(Stop.objects.filter(
                    departure_journeys__journey_pattern_section__journey_patterns__route__in=
                    Route.objects.filter(line=self, journey_patterns__direction=bound,
                                         journey_patterns__journeys__days_of_week=dayperiod)).distinct()\
                    .order_by('departure_journeys__stop_from_sequence_number').values_list('atco_code', flat=True))
                last_stop = Stop.objects.filter(
                    arrival_journeys__journey_pattern_section__journey_patterns__route__in=
                    Route.objects.filter(line=self, journey_patterns__direction=bound,
                                         journey_patterns__journeys__days_of_week=dayperiod))\
                    .order_by('departure_journeys__stop_to_sequence_number').last()
                if last_stop:
                    stop_list[bound][dayperiod].append(last_stop.atco_code)
        self.stop_list = stop_list
        self.save()

    def generate_timetable(self):
        # Create list of stops per line number
        self.generate_stop_list()

        line_timetable = {
            'inbound': {
                'MondayToFriday': {},
                'Saturday': {},
                'Sunday': {},
                'HolidaysOnly': {}
            },
            'outbound': {
                'MondayToFriday': {},
                'Saturday': {},
                'Sunday': {},
                'HolidaysOnly': {}
            }
        }

        for bound in ['inbound', 'outbound']:
            for dayperiod in ['MondayToFriday', 'Saturday', 'Sunday', 'HolidaysOnly']:
                journeys = VehicleJourney.objects.filter(journey_pattern__route__line=self,
                                                         journey_pattern__direction=bound,
                                                         days_of_week=dayperiod).distinct().order_by('departure_time')
                timetable = line_timetable[bound][dayperiod]
                for stop in self.stop_list[bound][dayperiod]:
                    timetable[stop] = []
                i = 0
                for journey in journeys:
                    journey.generate_timetable()
                    for stop in self.stop_list[bound][dayperiod]:
                        timetable[stop].append(None)
                    for journey_timetable_entry in journey.timetable:
                        try:
                            timetable[journey_timetable_entry['stop_id']][i] = journey_timetable_entry['time']
                        except:
                            print(bound, dayperiod, journey.id, journey.journey_pattern.id, journey.journey_pattern.route.id, journey_timetable_entry)
                    i += 1

        self.timetable = line_timetable
        self.save()


    @python_2_unicode_compatible
    def __str__(self):
        return "%s (%s)" % (self.line_name, self.description)


class Route(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    description = models.CharField(max_length=255)
    line = models.ForeignKey(Line, related_name='routes', on_delete=models.CASCADE)
    stops_list = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    def get_all_vehicle_journeys(self):
        return VehicleJourney.objects.filter(journey_pattern__route=self).order_by('departure_time')

    def get_stops_list(self):
        bus_stops = []
        for stop in self.stops_list.split(','):
            bus_stops.append(Stop.objects.get(atco_code=stop))
        return bus_stops

    def get_route_coordinates(self):
        bus_stops = []
        for stop in self.stops_list.split(','):
            bus_stops.append(Stop.objects.get(atco_code=stop).get_coordinates())
        return bus_stops

    @python_2_unicode_compatible
    def __str__(self):
        return "%s - %s" % (self.line, self.description)


class JourneyPatternSection(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    last_modified = models.DateTimeField(auto_now=True)

    @python_2_unicode_compatible
    def __str__(self):
        return "%s" % (self.id)


class JourneyPatternTimingLink(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    stop_from = models.ForeignKey(Stop, related_name='departure_journeys', on_delete=models.CASCADE)
    stop_from_timing_status = models.CharField(max_length=3)
    stop_from_sequence_number = models.IntegerField()
    stop_to = models.ForeignKey(Stop, related_name='arrival_journeys', on_delete=models.CASCADE)
    stop_to_timing_status = models.CharField(max_length=3)
    stop_to_sequence_number = models.IntegerField()
    run_time = models.DurationField()
    wait_time = models.DurationField(null=True, blank=True)
    journey_pattern_section = models.ForeignKey(JourneyPatternSection, related_name='timing_links',
                                                on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)

    @python_2_unicode_compatible
    def __str__(self):
        return "%s - %s (%s)" % (self.stop_from, self.stop_to, self.run_time)


class JourneyPattern(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    route = models.ForeignKey(Route, related_name='journey_patterns', on_delete=models.CASCADE)
    direction = models.CharField(max_length=100)
    section = models.ForeignKey(JourneyPatternSection, related_name='journey_patterns', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.id


class VehicleJourney(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    journey_pattern = models.ForeignKey(JourneyPattern, related_name='journeys', on_delete=models.CASCADE)
    departure_time = models.TimeField()
    days_of_week = models.CharField(max_length=100, null=True, blank=True)
    nonoperation_bank_holidays = models.CharField(max_length=200, null=True, blank=True)
    operation_bank_holidays = models.CharField(max_length=200, null=True, blank=True)
    order = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)

    def generate_timetable(self):
        departure_time = datetime.datetime.combine(datetime.date(1, 1, 1), self.departure_time)
        timing_links = self.journey_pattern.section.timing_links.order_by('stop_from_sequence_number')\
            .select_related("stop_from")
        order = 1
        timetable_objects = []
        if timing_links:
            for timing_link in timing_links:
                timetable_objects.append(Timetable(
                    vehicle_journey=self, stop_id=timing_link.stop_from.atco_code, time=departure_time.time(), order=order))
                departure_time += timing_link.run_time
                if timing_link.wait_time:
                    departure_time += timing_link.wait_time
                order += 1
            timetable_objects.append(Timetable(vehicle_journey=self, stop_id=timing_links.last().stop_to.atco_code,
                                               time=departure_time.time(), order=order, last_stop=True))
        return timetable_objects

    def get_timetable(self):
        return Timetable.objects.filter(vehicle_journey=self).order_by('order')

    @property
    def timetable(self):
        timetable = []
        for time in Timetable.objects.filter(vehicle_journey=self).order_by('order'):
            timetable.append({'stop': time.stop.atco_code, 'time': time.time, 'order': time.order})
        return timetable

    def get_timetable_prefetch(self):
        return self.get_timetable().select_related('stop')

    def get_stops_list(self):
        return Timetable.objects.filter(vehicle_journey=self).order_by('order').values('stop')

    @python_2_unicode_compatible
    def __str__(self):
        return self.id


class SpecialDaysOperation(models.Model):
    vehicle_journey = models.ForeignKey(VehicleJourney, related_name='special_days_operation', on_delete=models.CASCADE)
    days = DateRangeField()
    operates = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields=['vehicle_journey', 'days', 'operates']),
        ]

class Timetable(models.Model):
    vehicle_journey = models.ForeignKey(VehicleJourney, related_name='journey_times', on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, related_name='journey_times', on_delete=models.CASCADE)
    time = models.TimeField()
    order = models.IntegerField()  # Order of the stop in the vehicle journey (first stop, order = 1)
    last_stop = models.BooleanField(default=False)  # Last stop of a vehicle journey

    class Meta:
        indexes = [
            models.Index(fields=['vehicle_journey', 'stop', 'time', 'order', 'last_stop']),
        ]
