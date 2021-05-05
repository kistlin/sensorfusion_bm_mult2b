import struct
from loguru import logger


class PrecisionAccelerometer:
    """
    // [0]: packet start byte (need a iIndex++ here since not using sBufAppendItem)
    // [1]: packet type 8 byte (iIndex is automatically updated in sBufAppendItem)
    // [2]: packet number byte
    // [3]: AccelCalPacketOn in range 0-11 denotes stored location and MAXORIENTATIONS denotes transmit
    // precision accelerometer calibration on power on before any measurements have been obtained.
    // [9-4]: stored accelerometer measurement fGs (scaled to 8192 counts per g)
    // [15-10]: precision accelerometer offset vector fV (g scaled by 32768.0)
    // [21-16]: precision accelerometer inverse gain matrix diagonal finvW - 1.0 (scaled by 10000.0)
    // [27-22]: precision accelerometer inverse gain matrix off-diagonal finvW (scaled by 10000)
    // [33-28]: precision accelerometer rotation matrix diagonal fR0 (scaled by 10000)
    // [45-34]: precision accelerometer inverse rotation matrix off-diagonal fR0 (scaled by 10000)
    // [46]: add the tail byte for the packet type 8
    """
    def __init__(self, data: bytes):
        """ """
        self._expected_packet_type = 8
        self._expected_data_size = 45
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
                f"PrecisionAccelerometer: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
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
