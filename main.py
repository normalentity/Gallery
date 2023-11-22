from flet import *
from scripts.config_checker import ConfigChecker
from ui.appbar import AppBarUI
from ui.gallery_ui import GalleryUI
from scripts.logic_ui import LogicUI



def main(page:Page):
    # window settings
    page.window_width = 900
    page.window_height = 600
    page.window_center()
    page.window_resizable = False
    page.title = "Gallery Photo"

    page.appbar = AppBarUI(page).appbar_container

    app = GalleryUI(page=page)
    page.add(app)

    page.update()


if __name__ == "__main__":
    config = ConfigChecker()
    l = LogicUI(page=Page)

    config.create_json_file()
    l.draw_images()

    app(target=main)