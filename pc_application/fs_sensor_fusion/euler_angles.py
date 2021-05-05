import struct
from loguru import logger


class EulerAnglesType:
    """
    // [0]: packet start byte
    // [1]: packet type 4 byte (Euler angles)
    // [2]: packet number byte
    // [6-3]: time stamp (4 bytes)
    // [12-7]: add the angles (resolution 0.1 deg per count) to the transmit buffer
    // [13]: add the tail byte for the roll, pitch, compass angle packet type 4
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 4
        self._expected_data_size = 12
        self._data_raw = b''
        self._packet_type = 0
        self._packet_number = 0
        self._phi_roll = 0
        self._theta_pitch = 0
        self._rho_yaw = 0
        self._is_valid = False
        self._parse_data(data)

    def _parse_data(self, data: bytes):
        """ """
        self._data_raw = data
        if len(data) != self._expected_data_size:
            logger.warning(
                f"EulerAnglesType: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
            return
        self._packet_type, self._packet_number, self._timestamp, \
        self._phi_roll, self._theta_pitch, self._rho_yaw = struct.unpack("<BBLhhh", data)
        if self._expected_packet_type != self._packet_type:
            self._is_valid = False
            logger.warning(f"packet type {self._packet_type} does not match the expected type {self._expected_packet_type}")
        else:
            self._is_valid = True

    @property
    def is_valid(self):
        """ """
        return self._is_valid
