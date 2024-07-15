from .screen import Screenshot
from .manager import Manager
import keyboard


def screenshot(bangumi: str):
    handler = Screenshot(bangumi)
    keyboard.on_press(handler.on_key)
    keyboard.wait()


def manager() -> str:
    handler = Manager()
    return handler.bangumi
