import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger=logging.getLogger(__name__)


logger.debug("yes i can")


logger.info("난 할 수 있다")

logger.warning('곧 문제 생김')
logger.warning('곧 문제 생김')


logger.error('기능이 동작 안함')
logger.critical('시스템 다운!')


