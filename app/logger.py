import os
import logging
from logging.handlers import RotatingFileHandler

from app.env_validator import get_settings

settings = get_settings()
log_format = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s " "(%(filename)s:%(lineno)d)"
)


def service_logger(name):
    logger = logging.getLogger(name)

    env = settings.APP_ENV.lower()

    if env == "development" or env == "testing":
        logger.setLevel(logging.INFO)

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f"{name}.log"),
            maxBytes=1024 * 1024 * 5,
            backupCount=5,
        )
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 핸들러 추가
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    elif env == "production":
        logger.setLevel(logging.ERROR)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    else:
        raise ValueError(f"Unknown environment: {env}")

    return logger
