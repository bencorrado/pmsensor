import logging
import time
from pmsensor import serial_pm as pm


def main():
    logging.basicConfig(level=logging.INFO)
    sensors = []
#    sensors.append(pm.PMDataCollector("/dev/tty.wchusbserial144740",
#                                      pm.SUPPORTED_SENSORS["novafitness,sds011"]))
    sensors.append(pm.PMDataCollector("/dev/tty.SLAB_USBtoUART",
                                      pm.SUPPORTED_SENSORS["oneair,s3"]))
#    sensors.append(pm.PMDataCollector("/dev/tty.SLAB_USBtoUART4",
#                                      pm.SUPPORTED_SENSORS["plantower,pms7003"]))
#    sensors.append(pm.PMDataCollector("/dev/tty.SLAB_USBtoUART",
#                                      pm.SUPPORTED_SENSORS["winsen,zh03b"]))

    for s in sensors:
        print(s.supported_values())

    while True:
        for s in sensors:
            print(s.read_data())
        time.sleep(3)

if __name__ == '__main__':
    main()
