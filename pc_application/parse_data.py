import os
import pathlib
import serial
from loguru import logger

from fs_sensor_fusion.factory import create_object
from fs_sensor_fusion.shared import START_BYTE
from fs_sensor_fusion.main import MainType


def process_package(package_data: bytes):
    """ """
    if package_data:
        package = create_object(package_data)
        if package and package.is_valid:
            if isinstance(package, MainType):
                ACCEL_SCALE_1G = 8192  # [12-7]: integer accelerometer data words (scaled to 8192 counts per g for PC GUI)
                MAG_SCALE_uT = 10  # [18-13]: integer calibrated magnetometer data words (already scaled to 10 count per uT for PC GUI)
                GYRO_SCALE_DEG_PER_SEC = 20  # [24-19]: uncalibrated gyro data words (scaled to 20 counts per deg/s for PC GUI)
                logger.info(f"Accelerometer X: {package.accelerometer_x} => {package.accelerometer_x/ACCEL_SCALE_1G}g")
                logger.info(f"Accelerometer Y: {package.accelerometer_y} => {package.accelerometer_y/ACCEL_SCALE_1G}g")
                logger.info(f"Accelerometer Z: {package.accelerometer_z} => {package.accelerometer_z/ACCEL_SCALE_1G}g")
                logger.info(f"Magnetometer X: {package.magnetometer_x} => {package.magnetometer_x/MAG_SCALE_uT}uT")
                logger.info(f"Magnetometer Y: {package.magnetometer_y} => {package.magnetometer_y/MAG_SCALE_uT}uT")
                logger.info(f"Magnetometer Z: {package.magnetometer_z} => {package.magnetometer_z/MAG_SCALE_uT}uT")
                logger.info(f"Gyroscope X: {package.gyroscope_x} => {package.gyroscope_x/GYRO_SCALE_DEG_PER_SEC}deg/s")
                logger.info(f"Gyroscope Y: {package.gyroscope_y} => {package.gyroscope_y/GYRO_SCALE_DEG_PER_SEC}deg/s")
                logger.info(f"Gyroscope Z: {package.gyroscope_z} => {package.gyroscope_z/GYRO_SCALE_DEG_PER_SEC}deg/s")


def process_data(data: bytearray) -> bytearray:
    """ """
    package = b''
    while True:
        package, separator, data_rest = data.partition(START_BYTE)
        if not separator and not data_rest:
            break
        else:
            process_package(package)
            data = data_rest
    return package


if __name__ == "__main__":
    UART_SPEED = 115200
    # available_ports = serial.tools.list_ports
    port = '/dev/tty.usbmodem0000001234561'

    with serial.Serial(port, UART_SPEED, timeout=None) as serial_port:
        data = bytearray()
        while True:
            data.extend(serial_port.read(512))
            data = process_data(data)

    # binary_data = pathlib.Path("test_data.bin").read_bytes()
    # binary_data = pathlib.Path("test_data.bin").read_bytes()
    # binary_data = binary_data.split(sep=START_BYTE)
    # print(f"{len(binary_data)} packages in data")
    # for one_package in binary_data:
    #     process_package(one_package)
