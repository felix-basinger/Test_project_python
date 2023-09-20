import json
from datetime import datetime
from typing import Optional


class NotesApp:
    def __init__(self, path: str = 'notes.json'):
        self.notes: dict = {}
        self.path = path

    def get(self, index: Optional[int] = None):
        if index:
            return self.notes.get(index)
        return self.notes

    def open(self):
        try:
            with open(self.path, 'r', encoding="UTF-8") as f:
                self.notes = json.load(f)
            return True
        except:
            return False

    def save(self):
        try:
            with open(self.path, 'w', encoding="UTF-8") as f:
                json.dump(self.notes, f, indent=4, ensure_ascii=False)
            return True
        except:
            return False

    def find(self, word: str) -> dict[int:dict[str, str, datetime]]:
        result = {}
        for index, note in self.notes.items():
            if word.lower() in ' '.join(note.values()).lower():
                result[index] = note
        return result

    def check_id(self):
        if self.notes:
            return max(list(map(int, self.notes))) + 1
        return 1

    def add(self, new_note: dict[str, str, datetime]):
        notes = {str(self.check_id()): new_note}
        self.notes.update(notes)

    def remove(self, index):
        title = self.notes.pop(str(index))
        return title.get('title')

    def update(self, index: str, new_note: dict[str, str, datetime]):
        self.notes[index] = new_note
