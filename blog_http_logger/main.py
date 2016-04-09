import logging
import logging.handlers

logger = logging.getLogger(__name__)

_TARGET = '127.0.0.1:5000'
_PATH = '/'
_VERB = 'GET'

sh = logging.handlers.HTTPHandler(_TARGET, _PATH, method=_VERB)

logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

logger.debug("Test message.")
