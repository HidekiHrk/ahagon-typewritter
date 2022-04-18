from os import listdir

from components.Canvas import Canvas
from components.MainWindow import MainWindow
from events.Keyboard import Keyboard
from settings import *
from utils.files import get_frame_folder, get_icon


def main():
    window = MainWindow(WINDOW_NAME, FRAME_SIZE, icon=get_icon())

    frames_paths = [get_frame_folder(file_name)
                    for file_name in listdir(get_frame_folder())]

    canvas = Canvas(window, FRAME_SIZE, frames_paths, BACKGROUND_COLOR)
    canvas.render_next_image()

    kb = Keyboard()

    kb.on('keydown', lambda _: canvas.render_next_image())

    kb.start()

    window.show()


if __name__ == '__main__':
    main()
