import configparser


class ConfigReader:
    config = configparser.ConfigParser()
    config.read('config.ini')

    @staticmethod
    def get(section, key):
        return ConfigReader.config.get(section, key)

    @staticmethod
    def getint(section, key):
        return ConfigReader.config.getint(section, key)
