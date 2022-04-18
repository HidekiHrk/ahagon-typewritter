import configparser

config = configparser.ConfigParser()
config.read('./config.ini')


WINDOW_NAME = config.get('general', 'window_name')
BACKGROUND_COLOR = config.get('general', 'background_color')
ASSETS_FOLDER = config.get('paths', 'ASSETS_FOLDER')
FRAMES_FOLDER = config.get('paths', 'FRAMES_FOLDER')
ICON_FILE = config.get('paths', 'icon_name')
FRAME_SIZE = (config.get('frames', 'frame_width'),
              config.get('frames', 'frame_height'))
