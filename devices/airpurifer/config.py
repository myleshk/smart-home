import configparser


configParser = configparser.ConfigParser()
configParser.read('config.ini')
config = configParser['DEFAULT']
IP = config.get('ip')
TOKEN = config.get('token')
MAX_RETRY = config.getint('maxRetry', 3)
