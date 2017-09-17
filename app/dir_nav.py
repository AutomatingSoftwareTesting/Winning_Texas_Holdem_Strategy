import os
import sys


class DirNav(object):
    def __init__(self, file_name=None, file_path=None):
        self.file_path = file_path
        self.name = file_name

    def get_path(self, folder):
        current_dir = sys.path[0]
        if folder == "tables":
            self.file_path = os.path.join(current_dir, "../images/tables/")
        elif folder == "cards":
            self.file_path = os.path.join(current_dir, "../images/cards/")
        elif folder == "hand_ranges":
            self.file_path = os.path.join(current_dir, "../hand_ranges/")
        elif folder == "reports":
            self.file_path = os.path.join(current_dir, "../reports/")
        else:
            return "Sorry, unknown folder."
        return self.file_path

    def get_name(self):
        return self.name

    def __str__(self):
        return str(self.file_path) + str(self.name)
