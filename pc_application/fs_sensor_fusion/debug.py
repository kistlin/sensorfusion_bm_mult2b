import struct
from loguru import logger


class DebugType:
    """
    // [0]: packet start byte
    // [1]: packet type 2 byte
    // [2]: packet number byte
    // [4-3] software version number
    // [6-5] systick count / 20
    // [7 in practice but can be variable]: add the tail byte for the debug packet type 2
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 2
        self._expected_data_size = 6
        self._data_raw = b''
        self._packet_type = 0
        self._packet_number = 0
        self._sw_version_number = 0
        self._sys_tick_count = 0
        self._is_valid = False
        self._parse_data(data)

    def _parse_data(self, data: bytes):
        """ """
        self._data_raw = data
        if len(data) != self._expected_data_size:
            logger.warning(
                f"DebugType: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
            return
        self._packet_type, self._packet_number, self._sw_version_number, self._sys_tick_count = struct.unpack("<BBhH", data)
        if self._expected_packet_type != self._packet_type:
            self._is_valid = False
            logger.warning(f"packet type {self._packet_type} does not match the expected type {self._expected_packet_type}")
        else:
            self._is_valid = True

    @property
    def is_valid(self):
        """ """
        return self._is_valid
