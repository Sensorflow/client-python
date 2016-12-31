from protobuf_stream import ProtocolBuffersStream
import sensorflow.model as command_sf


class SensorflowSerialMessenger(object):
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.messenger = ProtocolBuffersStream(port, baudrate)

    def ping(self, test_value=101):
        ping_command = command_sf.Command()
        ping_command.command = command_sf.Command.CommandType.PING
        self.messenger.send(ping_command)

        ping_command = command_sf.Ping()
        ping_command.value = test_value
        self.messenger.send(ping_command)

        ping_response = command_sf.Ping()
        self.messenger.receive(ping_response)

        return test_value + 1 == ping_response.value

    def notification(self):
        notification_command = command_sf.Command()
        notification_command.command = command_sf.Command.CommandType.NOTIFICATION
        self.messenger.send(notification_command)

        notification_response = command_sf.Notification()
        self.messenger.receive(notification_response)
        return notification_response

    def read_all(self):
        read_response = command_sf.SensorReadList()
        read_command = command_sf.Command()
        read_command.command = command_sf.Command.CommandType.READ_ALL
        self.messenger.send(read_command)
        self.messenger.receive(read_response)
        return read_response.reads

    def read(self, sensor_name):
        read_response = command_sf.SensorRead()
        read_command = command_sf.Command()
        read_command.command = command_sf.Command.CommandType.READ
        self.messenger.send(read_command)
        sensor_name_command = command_sf.SensorName()
        sensor_name_command.name = sensor_name
        self.messenger.send(sensor_name_command)
        self.messenger.receive(read_response)
        return read_response