import os
from scripts.config_checker import ConfigChecker
from flet import *


class LogicUI(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page=page
        self.config_checker = ConfigChecker()
        from ui.gallery_ui import GalleryUI

        self.gallery_ui = GalleryUI(page=Page)

        self.page = page

        self.folder_path = self.config_checker.get_folder_path()
        self.files = os.listdir(self.folder_path)

        # Filter only images (for example, with the extension .jpg or .png)
        self.images_filter = [f for f in self.files if f.endswith((".png", ".svg", ".jpg"))]

    def load_images(self):
        # Load and process each image

        for self.image_file in self.images_filter:
            self.images_path = os.path.join(self.folder_path, self.image_file)
            
            return self.images_path
        
    def draw_images(self):
        self.gallery_ui.images_row.controls.append(
            Image(
                src=self.load_images(),
                width=200,
                height=200,
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            )
        )
        self.page.update()