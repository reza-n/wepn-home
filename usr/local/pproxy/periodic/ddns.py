
import sys
import os
import logging.config
up_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(up_dir)
from ipw import IPW
from device import Device

# commenting out these lines, since ddns runs as user pi
# and user pi cannot write to the error.log file
# DO NOT RE-ENABLE THESE LOGS
# LOG_CONFIG = "/etc/pproxy/logging.ini"
# logging.config.fileConfig(LOG_CONFIG, disable_existing_loggers=False)
logger = logging.getLogger("ddns")
device = Device(logger)
ipw = IPW()
ip_address = ipw.myip()

device.update_dns(ip_address)
