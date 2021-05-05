import struct
from loguru import logger

from .shared import MessageType, BaseType


class MainType(BaseType):
    """
    Main type 1:
    // [0]: packet start byte (need a iIndex++ here since not using sBufAppendItem)
    // [1]: packet type 1 byte (iIndex is automatically updated in sBufAppendItem)
    // [2]: packet number byte
    // [6-3]: 1MHz time stamp (4 bytes)
    // [12-7]: integer accelerometer data words (scaled to 8192 counts per g for PC GUI)
    // send non-zero data only if the accelerometer sensor is enabled and used by the selected quaternion
    // [18-13]: integer calibrated magnetometer data words (already scaled to 10 count per uT for PC GUI)
    // send non-zero data only if the magnetometer sensor is enabled and used by the selected quaternion
    // [24-19]: uncalibrated gyro data words (scaled to 20 counts per deg/s for PC GUI)
    // send non-zero data only if the gyro sensor is enabled and used by the selected quaternion
    // [32-25]: scale the quaternion (30K = 1.0F) and add to the buffer
    // [33]: add the flags byte to the buffer
    // flags byte 33: quaternion type in least significant nibble
    // Q3:   coordinate nibble, 1
    // Q3M:	 coordinate nibble, 6
    // Q3G:	 coordinate nibble, 3
    // Q6MA: coordinate nibble, 2
    // Q6AG: coordinate nibble, 4
    // Q9:   coordinate nibble, 8
    // flags byte 33: coordinate in most significant nibble
    // Aerospace/NED:	0, quaternion nibble
    // Android:	  		1, quaternion nibble
    // Windows 8: 		2, quaternion nibble
    // set the quaternion, flags, angular velocity and Euler angles
    // [34]: add the shield (bits 7-5) and Kinetis (bits 4-0) byte
    //     tmpuint8_t = ((THIS_SHIELD & 0x07) << 5) | (THIS_BOARD & 0x1F);
    //     #define THIS_BOARD                 5          ///< FRDM_K64F
    //     #define SHIELD_MULTIB 0
    //     #define SHIELD_NONE   1
    //     #define SHIELD_AGM01  2
    //     #define SHIELD_AGM02  3
    //     #define SHIELD_AGMP03 4
    //     #define SHIELD_AGM04  5
    //     #define THIS_SHIELD   SHIELD_MULTIB
    // [35]: add the tail byte for the standard packet type 1
    """

    def __init__(self, data: bytes):
        """
        `data` needs to have exactly 34 bytes, not counting start and end byte. Packet type has to be 1.

        Parameters
        ----------
        data: bytes
            Raw bytes sent by the FRDM-K64F / FRDM-FXS-MULT2-B
        """
        super().__init__()
        self._expected_packet_type = MessageType.MAIN
        self._expected_data_size = 34
        self._data_raw = b''
        self._packet_type = MessageType.UNDEFINED
        self._packet_number = 0
        self.time_stamp_1MHz = 0
        self.accelerometer_x = 0
        self.accelerometer_y = 0
        self.accelerometer_z = 0
        self.magnetometer_x = 0
        self.magnetometer_y = 0
        self.magnetometer_z = 0
        self.gyroscope_x = 0
        self.gyroscope_y = 0
        self.gyroscope_z = 0
        self.quaternion_q0 = 0
        self.quaternion_q1 = 0
        self.quaternion_q2 = 0
        self.quaternion_q3 = 0
        self.flags = 0
        self.shield_and_kinetis_byte = 0
        self._is_valid = False
        self._parse_data(data)

    def _parse_data(self, data: bytes):
        """ """
        self._data_raw = data
        if len(data) != self._expected_data_size:
            logger.warning(
                f"MainType: not the right amount of data bytes ({len(data)}), expected {self._expected_data_size}")
            return
        packet_type, self._packet_number, self._time_stamp_1MHz, \
        self.accelerometer_x, self.accelerometer_y, self.accelerometer_z, \
        self.magnetometer_x, self.magnetometer_y, self.magnetometer_z, \
        self.gyroscope_x, self.gyroscope_y, self.gyroscope_z, \
        self.quaternion_q0, self.quaternion_q1, self.quaternion_q2, self.quaternion_q3, \
        self.flags, self.shield_and_kinetis_byte = struct.unpack(
            "<BBLhhhhhhhhhhhhhBB", data)
        if self._expected_packet_type.value != packet_type:
            self._is_valid = False
            logger.warning(f"packet type {packet_type} does not match the expected type {self._expected_packet_type}")
        else:
            self._packet_type = self._expected_packet_type
            self._is_valid = True
