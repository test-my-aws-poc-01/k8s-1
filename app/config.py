import os
import uuid


ROOT = os.path.abspath(os.path.dirname(__file__))
_STARTUP_IDENTIFIER = uuid.uuid4()


class Config(object):
    SERVICE_NAME = 'DEMO KUBERNETES PROJECT 1'
    STARTUP_IDENTIFIER = _STARTUP_IDENTIFIER
