from protobuf3.fields import EnumField, Int32Field, MessageField, FloatField, StringField
from enum import Enum
from protobuf3.message import Message


class Command(Message):
    pass


class SensorRead(Message):
    pass


class SensorName(Message):
    pass


class Ping(Message):
    pass


class SensorReadList(Message):
    pass


class Notification(Message):
    pass


Command.add_field('command', StringField(field_number=1, optional=True))
SensorRead.add_field('name', StringField(field_number=1, optional=True))
SensorRead.add_field('values', FloatField(field_number=2, repeated=True))
SensorName.add_field('name', StringField(field_number=1, optional=True))
Ping.add_field('value', Int32Field(field_number=1, optional=True))
SensorReadList.add_field('reads', MessageField(field_number=1, repeated=True, message_cls=SensorRead))
Notification.add_field('what', StringField(field_number=1, optional=True))
