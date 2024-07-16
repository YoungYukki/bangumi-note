from PIL import ImageGrab
import re
import os


class Screenshot:
    def __init__(self, bangumi: str) -> None:
        self.image_root = os.path.join('note', 'image')
        if not os.path.exists(self.image_root):
            os.makedirs(self.image_root)
        self.bangumi = bangumi
        self.get_count()

    def get_count(self):
        images = os.listdir(os.path.join('note', 'image'))
        pattern = re.compile(f'{self.bangumi}.+')
        self.count = 0
        for image in images:
            if pattern.match(image):
                self.count += 1

    def build_image_path(self):
        self.count += 1
        count = str(self.count).zfill(3)
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
