""""
Read data from CO2 sensor
"""

import time
import logging

import serial

MHZ19_SIZE = 9
MZH19_READ = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]

def read_mh_z19(serial_device):
    """ Read the CO2 PPM concenration from a MH-Z19 sensor"""

    logger = logging.getLogger(__name__)

    ser = serial.Serial(port=serial_device,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)

    sbuf = bytearray()
    starttime = time.time()
    finished = False
    timeout = 2
    res = -1
    ser.write(MZH19_READ)
    while not finished:
        mytime = time.time()
        if mytime - starttime > timeout:
            logger.error("read timeout after %s seconds, read %s bytes",
                         timeout, len(sbuf))
            return {}

        if ser.inWaiting() > 0:
            sbuf += ser.read(1)

            if len(sbuf) == MHZ19_SIZE:
                # TODO: check checksum

                res = sbuf[2]*256 + sbuf[3]
                logger.debug("Finished reading data %s", sbuf)
                finished = True

        else:
            time.sleep(.1)
            logger.debug("Serial waiting for data, buffer length=%s",
                         len(sbuf))

    return res
