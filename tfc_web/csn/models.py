import logging
import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


LOGGER = logging.getLogger('CSN')


class Sensor(models.Model):
    """This is the model is used to store a json version of any type of
    sensor object."""
    id = models.AutoField(primary_key=True)
    info = JSONField()

    @classmethod
    def get_lorawan(cls, sensor_id, user_id):
        sensor = Sensor.objects.filter(info__sensor_id=sensor_id, info__sensor_type="lorawan", info__user_id=user_id)
        if sensor:
            return sensor[0]
        else:
            return None

    @classmethod
    def get_all_lorawan(cls, user_id):
        return Sensor.objects.filter(info__sensor_type="lorawan", info__user_id=user_id, info__sensor_id__isnull=False)

    @classmethod
    def insert_lorawan(cls, info):
        return Sensor.objects.create(info=info)

    @classmethod
    def delete_lorawan(cls, sensor_id, user_id):
        sensor = Sensor.objects.filter(info__sensor_id=sensor_id, info__sensor_type="lorawan", info__user_id=user_id)
        num_deleted, deleted = sensor.delete()
        return num_deleted

    class Meta:
        managed = False


class ConnectionQuerySet(models.QuerySet):

    def owned_by_user(self, user):
        return self.filter(user=user)

    def lwhttp_objects(self):
        return self.filter(info__connection_type='everynet_lw_http')


class ConnectionManager(models.Manager):

    def get_queryset(self):
        return ConnectionQuerySet(self.model, using=self._db)

    def create_lwhttp_object(self, **kwargs):
        kwargs['info']['connection_type'] = 'everynet_lw_http'
        obj = self.create(**kwargs)
        return obj


class Connection(models.Model):

    objects = ConnectionManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    info = JSONField()


