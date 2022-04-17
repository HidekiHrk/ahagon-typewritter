from typing import List, Literal, Callable, Dict
from threading import Thread
import keyboard


EventName = Literal['keydown', 'keyup', 'keypressed', 'any']
EventPredicate = Callable[[keyboard.KeyboardEvent], None]


class Keyboard:
    def __init__(self, supress=False):
        self.supress = supress
        self.__listeners: Dict[EventName, List[EventPredicate]] = {}
        self.__thread: Thread = Thread(daemon=True, target=self.loop)
        self.__started = False

    def on(self, event_name: EventName, callback: EventPredicate):
        if not self.__listeners.get(event_name):
            self.__listeners[event_name] = []
        self.__listeners[event_name].append(callback)

    def listen(self, event_name: EventName):
        def decorator_wrapper(callback: EventPredicate):
            self.on(event_name, callback)
        return decorator_wrapper

    def loop(self):
        pressed = False
        while self.started == True:
            event: keyboard.KeyboardEvent = keyboard.read_event(self.supress)
            event_name = {
                keyboard.KEY_DOWN: 'any' if pressed else 'keydown',
                keyboard.KEY_UP: 'keyup'
            }.get(event.event_type, 'any')

            pressed = event.event_type == keyboard.KEY_DOWN

            for listener in self.__listeners.get('any', []):
                listener(event)
            if event_name != 'any':
                for listener in self.__listeners.get(event_name, []):
                    listener(event)

    def start(self):
        self.__started = True
        self.__thread.start()

    def stop(self):
        self.__started = False

    @property
    def started(self):
        return self.__started
