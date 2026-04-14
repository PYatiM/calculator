import os

class HistoryManager:
    FILE_PATH = "history.txt"

    def save_entry(self, entry):
        with open(self.FILE_PATH, "a") as f:
            f.write(entry + "\n")

    def load_history(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, "r") as f:
            return f.readlines()