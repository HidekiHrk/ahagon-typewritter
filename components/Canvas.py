import tkinter
from typing import Any, List, Tuple

from components.FrameSet import FrameSet


LAYERS = ['first_layer', 'second_layer']


class Canvas(tkinter.Canvas):
    def __init__(self, root: Any, sizes: Tuple[int, int], frames_paths: List[str], background_color: str):
        super().__init__(root, width=sizes[0],
                         height=sizes[1], highlightthickness=0, bg=background_color)
        self.pack(expand=True)
        self.__frameSet: FrameSet = FrameSet(self, frames_paths)
        self.__current_layer = 0

    def render_next_image(self):
        aux_layer = self.__current_layer
        self.__current_layer = 1 if self.__current_layer == 0 else 0
        self.create_image(
            0, 0, image=self.__frameSet.next_frame(), anchor='nw', tags=LAYERS[self.__current_layer])
        self.delete(LAYERS[aux_layer])
