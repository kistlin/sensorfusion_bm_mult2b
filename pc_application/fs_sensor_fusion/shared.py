from enum import IntEnum


START_BYTE = b"\x7e"  # ~


class MessageType(IntEnum):
    """ """
    UNDEFINED = -1
    MAIN = 1
    DEBUG = 2
    ANGULAR_VELOCITY = 3
    EULER_ANGLES = 4
    ALTITUDE_TEMP = 5
    MAGNETIC = 6
    KALMAN = 7
    PRECISION_ACCELEROMETER = 8


class BaseType:
    """ """
    def __init__(self):
        """ """
        self._expected_packet_type = MessageType.UNDEFINED
        self._expected_data_size = 0
        self._data_raw = b''
        self._packet_type = MessageType.UNDEFINED
        self._packet_number = 0
        self._is_valid = False

    @property
    def type_expected(self) -> MessageType:
        """ """
        return self._expected_packet_type

    @property
    def type(self) -> MessageType:
        return self._packet_type

    @property
    def is_valid(self):
        """ """
        return self._is_valid
