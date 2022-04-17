import tkinter as tk
from typing import List

from utils.generators import generate_loop_numbers


class FrameSet:
    def __init__(self, canvas: tk.Canvas, frame_paths: List[str]):
        self.canvas = canvas
        self.__frame_paths = frame_paths
        self.__frames: List[tk.PhotoImage] = [None] * len(frame_paths)
        self.__frame_generator = generate_loop_numbers(len(frame_paths))

    def next_frame(self):
        index = next(self.__frame_generator)
        if self.__frames[index] is None:
            frame_path = self.__frame_paths[index]
            self.__frames[index] = tk.PhotoImage(file=frame_path)
        return self.__frames[index]
