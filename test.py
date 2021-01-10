from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")

# signals = {
# 	'COM_ACTIVE_FREQUENCY:1': {"getter": None, "val": None},
# 	'COM_ACTIVE_FREQUENCY:2': {"getter": None, "val": None},
# 	'NAV_ACTIVE_FREQUENCY:1': {"getter": None, "val": None},
# 	'NAV_ACTIVE_FREQUENCY:2': {"getter": None, "val": None},
# }


sm = SimConnect()
aq = AircraftRequests(sm)
COMFREQ = aq.get("VERTICAL_SPEED")
print(COMFREQ)
sm.exit()