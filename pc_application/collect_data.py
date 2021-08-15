import os
import serial


if __name__ == "__main__":
    """ """
    UART_SPEED = 115200
    # available_ports = serial.tools.list_ports
    port = '/dev/ttyACM0'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_file_name = os.path.abspath(os.path.join(current_dir, 'test_data.bin'))

    with serial.Serial(port, UART_SPEED, timeout=None) as serial_port:
        data = bytearray()
        while True:
            data.extend(serial_port.read(8192))
            with open(test_data_file_name, 'ab') as file:
                file.write(data)
                data.clear()
