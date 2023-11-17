import logging


def setup_logger(name: str) -> logging.Logger:
    """
    Configurar el logger.
    """

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # StreamHandler para output en consola
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    return logger


# Inicializar el logger
log = setup_logger("logger")
