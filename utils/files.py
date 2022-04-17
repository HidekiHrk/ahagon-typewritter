from os import path
from settings import *


def get_folder(root: str, *paths: str):
    return path.join(path.abspath(root), *paths)


def get_icon():
    return get_folder('.', ASSETS_FOLDER, ICON_FILE)


def get_frame_folder(file_name: str = None):
    paths = [ASSETS_FOLDER, FRAMES_FOLDER]
    if file_name:
        paths.append(file_name)

    return get_folder('.', *paths)
