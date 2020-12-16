import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

port = config.getint('app', 'port')
is_debug = config.getboolean('app', 'isDebug')
