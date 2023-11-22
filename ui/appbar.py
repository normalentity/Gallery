from flet import *
from ui.file_picker import File_Picker

class AppBarUI(UserControl):
    def __init__(self, page:Page):
        super().__init__()

        self.filepicker = File_Picker(page)

        self.open_folder = TextButton(
            icon=icons.FOLDER,text="Open Folder",
            on_click=lambda _: self.filepicker.get_directory_dialog.get_directory_path(),
        )

        self.open_pick = TextButton(
            icon=icons.FILE_OPEN, text="Open Files",
            on_click=lambda _: self.filepicker.pick_files_dialog.pick_files(
                allow_multiple=True,
                allowed_extensions=["png", "svg", "jpg"]
            ),
        )

        self.appbar_container = AppBar(
            bgcolor=colors.SURFACE_VARIANT,
            title=PopupMenuButton(
                items=[
                    self.open_folder,
                    self.open_pick
                ]
            )
        )

    def build(self):
        self.appbar_container