import logging
from miio import AirPurifierMiot
from datetime import datetime
from time import sleep
from config import IP, TOKEN


class Device:
    def __init__(self):
        self.device = AirPurifierMiot(IP, TOKEN)

    def status(self):
        status = self.device.status()
        logging.info({
            # "anion": status.anion,
            "aqi": status.aqi,
            # "average_aqi": status.average_aqi,
            # "fan_level": status.fan_level,
            "humidity": status.humidity,
            "is_on": status.is_on,
            # "power": status.power,
            "temperature": status.temperature,
        })

        return status
