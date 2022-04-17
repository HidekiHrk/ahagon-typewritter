import configparser

config = configparser.ConfigParser()
config.read('./config.ini')


ASSETS_FOLDER = config.get('paths', 'ASSETS_FOLDER')
FRAMES_FOLDER = config.get('paths', 'FRAMES_FOLDER')
ICON_FILE = config.get('paths', 'icon_name')
WINDOW_NAME = config.get('general', 'window_name')
FRAME_SIZE = (config.get('frames', 'frame_width'),
              config.get('frames', 'frame_height'))
