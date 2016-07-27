import logging
import time
from pmsensor import serial_data_collector as pm


def main():
    logging.basicConfig(level=logging.INFO)
    dc1 = pm.PMDataCollector("/dev/tty.wchusbserial144740",
                             pm.SUPPORTED_SENSORS["novafitness,sds021"])
    dc2 = pm.PMDataCollector("/dev/tty.SLAB_USBtoUART",
                             pm.SUPPORTED_SENSORS["oneair,s3"],
                             power_control=pm.DTR_OFF)

    print(dc1.supported_values())
    print(dc2.supported_values())

    while True:
        print(dc1.read_data())
        print(dc2.read_data())
        print("------")
        time.sleep(300)

if __name__ == '__main__':
    main()
