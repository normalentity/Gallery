from flet import *
from scripts.config_checker import ConfigChecker

class GalleryUI(UserControl):
    def __init__(self, page:Page):
        super().__init__()
        self.scripts = ConfigChecker()

        self.folder_name = Text(
            value="Test"
        )

        self.images_row = Row(
            expand=1,wrap=False,scroll="always",
        )

        self.galleryui = Container(
            width=900,height=490,
            alignment=alignment.top_center,
            content=self.images_row
        )  

    def error_path(self):
        return Text(
            value=f"File {self.scripts.get_folder_path()} does not exist"
        )

    def build(self):
        return self.galleryui