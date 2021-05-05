import struct
from loguru import logger


class MagneticType:
    """
    // [0]: packet start byte
    // [1]: packet type 6 byte
    // [2]: packet number byte
    // [4-3]: number of active measurements in the magnetic buffer
    // [6-5]: fit error (%) with resolution 0.01%
    // [8-7]: geomagnetic field strength with resolution 0.1uT
    // [10-9]: int16_t: ID of magnetic variable to be transmitted
    // ID 0 to 4 inclusive are magnetic calibration coefficients
    // ID 5 to 9 inclusive are for future expansion
    // ID 10 to (MAGBUFFSIZEX=12) * (MAGBUFFSIZEY=24)-1 or 10 to 10+288-1 are magnetic buffer elements
    // where the convention is used that a negative value indicates empty buffer element (index=-1)
    // [12-11]: int16_t: variable 1 to be transmitted this iteration
    // [14-13]: int16_t: variable 2 to be transmitted this iteration
    // [16-15]: int16_t: variable 3 to be transmitted this iteration
    // [17]: add the tail byte for the magnetic packet type 6
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 6
        self._expected_data_size = 16
        self._data_raw = b''
        self._packet_type = 0
        self._packet_number = 0
        self._is_valid = False
        self._parse_data(data)

    def _parse_data(self, data: bytes):
        """ """
        self._data_raw = data
        if len(data) != self._expected_data_size:
            logger.warning(
                f"MagneticType: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
            return
        # self._packet_type, self._packet_number = struct.unpack("<BB", data)
        if self._expected_packet_type != self._packet_type:
            self._is_valid = False
            logger.warning(f"packet type {self._packet_type} does not match the expected type {self._expected_packet_type}")
        else:
            self._is_valid = True

    @property
    def is_valid(self):
        """ """
        return self._is_valid
