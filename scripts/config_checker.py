import json
import os
from flet import *

class ConfigChecker():
    def __init__(self):
        self.path_folder = "config"
        self.full_path_folder = os.path.join(self.path_folder, "config.json")

        self.data = {
            "path_to_folder": None,
        }

    def create_json_file(self):
        if os.path.isfile(self.full_path_folder):
            print(f'Файл существует в папке {self.path_folder}')
        else:
            with open(self.full_path_folder, "w") as f:
                json.dump(self.data, f, indent=5)
                print("Файл создан")

    def save_path_to_folder(self,e: FilePickerResultEvent):
        self.data = {
                "path_to_folder": e.path
            }

        with open(self.full_path_folder, "w", encoding="utf-8") as f:
            json.dump(
                self.data, f, indent=5,ensure_ascii=False
            )
            print(e.path)

    def get_folder_path(self):
        with open(self.full_path_folder, "r", encoding="utf-8") as f:
            data = json.load(f)
            value = data["path_to_folder"]

            return str(value)