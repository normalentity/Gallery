from flet import *
from ui.gallery_ui import GalleryUI
from scripts.config_checker import ConfigChecker


class File_Picker(UserControl):
    def __init__(self,page:Page):
        super().__init__()

        self.gallery = GalleryUI(page=page)
        self.config = ConfigChecker()
        self.selected_files = self.gallery.folder_name

        self.get_directory_dialog = FilePicker(on_result=self.config.save_path_to_folder)

        self.pick_files_dialog = FilePicker(on_result=self.config.save_path_to_folder,)

        page.overlay.extend([self.get_directory_dialog, self.pick_files_dialog])
