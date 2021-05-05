import struct
from loguru import logger


class AngularVelocityType:
    """
    // [0]: packet start byte
    // [1]: packet type 3 byte (angular velocity)
    // [2]: packet number byte
    // [6-3]: time stamp (4 bytes)
    // [12-7]: add the scaled angular velocity vector to the output buffer
    // [13]: add the tail byte for the angular velocity packet type 3
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 3
        self._expected_data_size = 12
        self._data_raw = b''
        self._packet_type = 0
        self._packet_number = 0
        self._timestamp = 0
        self._omega_x = 0  # angular velocity x component
        self._omega_y = 0  # angular velocity x component
        self._omega_z = 0  # angular velocity x component
        self._is_valid = False
        self._parse_data(data)

    def _parse_data(self, data: bytes):
        """ """
        self._data_raw = data
        if len(data) != self._expected_data_size:
            logger.warning(
                f"AngularVelocityType: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
            return
        self._packet_type, self._packet_number, self._timestamp, \
        self._omega_x, self._omega_y, self._omega_z = struct.unpack("<BBLHHH", data)
        if self._expected_packet_type != self._packet_type:
            self._is_valid = False
            logger.warning(f"packet type {self._packet_type} does not match the expected type {self._expected_packet_type}")
        else:
            self._is_valid = True

    @property
    def is_valid(self):
        """ """
        return self._is_valid
