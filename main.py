import keyboard
from PIL import ImageGrab
import os


class Save:
    def __init__(self, bangumi: str) -> None:
        self.count = 0
        self.bangumi = bangumi
        self.image_root = os.path.join('note', self.bangumi, 'image')
        if not os.path.exists(self.image_root):
            os.makedirs(self.image_root)

    def build_image_path(self):
        self.count += 1
        count = str(self.count).zfill(2)
        image_name = f'{self.bangumi}_{count}.jpg'
        self.image_path = os.path.join(self.image_root, image_name)
        print(self.image_path)

    def save(self):
        self.build_image_path()
        image = ImageGrab.grab()
        image.save(self.image_path)

    def on_key(self, event):
        if event.name == 'print screen':
            self.save()
        else:
            print(event.name)


if __name__ == '__main__':
    handler = Save('test')
    keyboard.on_press(handler.on_key)
    keyboard.wait()
