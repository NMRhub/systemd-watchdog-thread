
import logging
wdt_logger = logging.getLogger('systemd-watchdog-thread')

__version__ = 1.0
from .watchdogthread import WatchdogThread

