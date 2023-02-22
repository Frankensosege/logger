import logging

class MyLogger():
    def get_logger(self, name=None):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")
        console = logging.StreamHandler()
        file_handler_debug = logging.FileHandler(filename="./log/log_debug.log")
        file_handler_info = logging.FileHandler(filename="./log/log_info.log")
        console.setLevel(logging.INFO)
        file_handler_debug.setLevel(logging.DEBUG)
        file_handler_info.setLevel(logging.INFO)

        #6 handler 출력을 format 지정방식으로 합니다.
        console.setFormatter(formatter)
        file_handler_debug.setFormatter(formatter)
        file_handler_info.setFormatter(formatter)

        #7 logger에 handler 추가합니다.
        logger.addHandler(console)
        logger.addHandler(file_handler_debug)
        logger.addHandler(file_handler_info)

        #8 설정된 log setting을 반환합니다.
        return logger
