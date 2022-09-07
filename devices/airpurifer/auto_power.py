from time import sleep
from config import MAX_RETRY
from device import Device
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

device = Device()


def action(retry=0):
    if retry > MAX_RETRY:
        logging.warning(f"Exceeding max retry {MAX_RETRY}, abort.")
        return
    result = device.status()

    if result.aqi is None:
        # retry
        sleep(1)
        return action(retry=retry+1)
    elif result.is_on is True and (result.aqi <= 10):
        logging.info(f"AQI {result.aqi} is low. Turning off")
        device.off()
    elif result.is_on is False and (result.aqi > 10):
        logging.info(f"AQI {result.aqi} is high. Turning on")
        device.on()


action()
