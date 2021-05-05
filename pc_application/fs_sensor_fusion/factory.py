from loguru import logger
from .main import MainType
from .debug import DebugType
from .angular_velocity import AngularVelocityType
from .euler_angles import EulerAnglesType
from .magnetic import MagneticType
from .kalman import Kalman
from .precision_accelerometer import PrecisionAccelerometer


def create_object(data: bytes):
    """ """
    type_byte = data[0]
    if type_byte == 1:
        logger.debug(f"creating package of type MainType with package of length {len(data)}")
        return MainType(data)
    elif type_byte == 2:
        logger.debug(f"creating package of type DebugType with package of length {len(data)}")
        return DebugType(data)
    elif type_byte == 3:
        logger.debug(f"creating package of type AngularVelocityType with package of length {len(data)}")
        return AngularVelocityType(data)
    elif type_byte == 4:
        logger.debug(f"creating package of type EulerAnglesType with package of length {len(data)}")
        return EulerAnglesType(data)
    elif type_byte == 5:
        logger.warning(f"package type {type_byte} is not implemented")
        return None
    elif type_byte == 6:
        logger.debug(f"creating package of type MagneticType with package of length {len(data)}")
        return MagneticType(data)
    elif type_byte == 7:
        logger.debug(f"creating package of type Kalman with package of length {len(data)}")
        return Kalman(data)
    elif type_byte == 8:
        logger.debug(f"creating package of type PrecisionAccelerometer with package of length {len(data)}")
        return PrecisionAccelerometer(data)
    else:
        logger.warning(f"package type {type_byte} is not implemented")
        return None
