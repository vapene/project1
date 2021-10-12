import logging
#handler
handler= logging.StreamHandler()
#formatter
formatter= logging.Formatter('%(asctime)s -%(name)s - %(levelname)-8s - %(message)s')
# formatter on handler
handler.setFormatter(formatter)

# add logger
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# log message

logger.debug("이 메세지는")
logger.info("생각대로 동작")
logger.warning('곧 문제 생김')
logger.error('기능이 동작 안함')
logger.critical('시스템 다운!')

