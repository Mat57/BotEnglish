import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
TOKEN = config["telegram"]["token"]
