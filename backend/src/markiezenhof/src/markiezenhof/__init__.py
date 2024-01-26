"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "markiezenhof"

_ = MessageFactory("markiezenhof")

logger = logging.getLogger("markiezenhof")
