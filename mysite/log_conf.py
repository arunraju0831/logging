import logging.config
import datetime

def log ():    
    LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'filters': {
                'request_id': {
                    '()': 'log_request_id.filters.RequestIDFilter'
                    # "()": "request_id.logging.RequestIdFilter"
                }
            },
            'formatters': {
                'standard': {
                    'format': '%(levelname)s [%(asctime)s] request-id=[%(request_id)s] : %(message)s'
                }
            },
            'handlers': {
                'file': {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'filters': ['request_id'],
                    'formatter': 'standard',
                    'filename': 'LOGFILES\\log_' + str(datetime.datetime.now().time()).replace(':', '-') + '.log',
                    'mode': 'w'
                }
            },
            'loggers': {
                'arun': {
                    'handlers': ['file'],
                    'level': 'DEBUG',
                    'propagate': False,
                }
            }
        }
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger('arun')
    logger.info("A Request is identified")
    logger.setLevel(logging.DEBUG)