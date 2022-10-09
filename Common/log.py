import logging

class Logger:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def get_log(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        streamHandle = logging.StreamHandler()
        fileHandle = logging.FileHandler(filename=self.path)

        formatter = logging.Formatter(f"%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s")
        streamHandle.setFormatter(formatter)
        fileHandle.setFormatter(formatter)

        streamHandle.setLevel(logging.INFO)
        fileHandle.setLevel(logging.INFO)

        self.logger.addHandler(streamHandle)
        self.logger.addHandler(fileHandle)

        return self.logger

logger = Logger('CAMETEST', r'D:\CameraTest\log.log')
logger = logger.get_log()
