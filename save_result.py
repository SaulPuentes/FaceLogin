import logging

def save_result(response):
    # Create and configure logger
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = "/home/antoniogarcia/OpenCV/FaceLogin/fr.log",
                        level = logging.DEBUG,
                        format = LOG_FORMAT)
    logger = logging.getLogger()

    #Test messages
    logger.info(response)