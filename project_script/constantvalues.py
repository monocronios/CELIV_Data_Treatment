ELECTRON_CHARGE = 1.6 * 10 ** (-19)

DEVICE_AREA = 1.4 * 10 ** (-5)

DEVICE_THICKNESS = 478 * 10 ** (-9)

INTEGRAL_CORRECTION_FACTOR = 1 * 10 ** (-9)

CURRENT_CORRECTION_FACTOR = pow(10, -3)

CHARGE_DENSITY_CORRECTION_FACTOR = 1 * 10 ** (-6)

CTTS_PRODUCT = INTEGRAL_CORRECTION_FACTOR * CHARGE_DENSITY_CORRECTION_FACTOR \
               / ELECTRON_CHARGE

SQR_METER_SQR_CENTIMETER_CONVERSION = pow(10, 4)

SQUARED_TIME_CORRECTION_FACTOR = pow(10, -12)

INTENSITIES = [(n*7.2) for n in list(range(1, 11))]
