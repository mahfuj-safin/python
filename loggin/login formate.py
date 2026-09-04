import logging
logging.basicConfig(
  filename = "myFile.log",
  format = '%(asctime)s - %(levelname)s - %(message)s',
  filemode = "a"
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
logger.debug("Harmless debug message")
logger.info("Program started successfully")
logger.warning("Low disk space warning")
logger.error("some error in program")
logger.critical("Critical issue! system might be down")