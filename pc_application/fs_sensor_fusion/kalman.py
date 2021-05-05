import struct
from loguru import logger


class Kalman:
    """
    // [0]: packet start byte
    // [1]: packet type 7 byte
    // [2]: packet number byte
    // [4-3]: fzgErr[CHX] resolution scaled by 30000
    // [6-5]: fzgErr[CHY] resolution scaled by 30000
    // [8-7]: fzgErr[CHZ] resolution scaled by 30000
    // [10-9]: fgErrPl[CHX] resolution scaled by 30000
    // [12-11]: fgErrPl[CHY] resolution scaled by 30000
    // [14-13]: fgErrPl[CHZ] resolution scaled by 30000
    // [16-15]: fzmErr[CHX] resolution scaled by 30000
    // [18-17]: fzmErr[CHY] resolution scaled by 30000
    // [20-19]: fzmErr[CHZ] resolution scaled by 30000
    // [22-21]: fmErrPl[CHX] resolution scaled by 30000
    // [24-23]: fmErrPl[CHY] resolution scaled by 30000
    // [26-25]: fmErrPl[CHZ] resolution scaled by 30000
    // [28-27]: fbPl[CHX] resolution 0.001 deg/sec
    // [30-29]: fbPl[CHY] resolution 0.001 deg/sec
    // [32-31]: fbPl[CHZ] resolution 0.001 deg/sec
    // [34-33]: fDeltaPl resolution 0.01deg
    // [36-35]: fAccGl[CHX] resolution 1/8192 g
    // [38-37]: fAccGl[CHY] resolution 1/8192 g
    // [40-39]: fAccGl[CHZ] resolution 1/8192 g
    // [42-41]: fDisGl[CHX] resolution 0.01m
    // [44-43]: fDisGl[CHY] resolution 0.01m
    // [46-45]: fDisGl[CHZ] resolution 0.01m
    // [47]: add the tail byte for the Kalman packet type 7
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 7
        self._expected_data_size = 46
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
                f"Kalman: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
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
