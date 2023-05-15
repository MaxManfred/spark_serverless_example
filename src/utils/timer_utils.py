# Import Python libraries.
import logging
from typing import Dict

# Import third party libraries.
from humanfriendly import format_timespan

# create logger
logger = logging.getLogger('serverless-spark-example')


def timer_args(name) -> Dict:
    """
    :param name: Name of Timer
    :return:  Dict
    """
    return {
        'name': name,
        'text': lambda secs: f'{name}: {format_timespan(secs)}',
        'logger': logger.info,
    }
