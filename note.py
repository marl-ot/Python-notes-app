import json
from datetime import datetime


class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date


class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                self.notes = json.load(file, object_hook=self._note_decoder)
        except FileNotFoundError:
            self.notes = []

    def _note_decoder(self, note_dict):
        note_date = datetime.strptime(note_dict['date'], '%Y-%m-%d %H:%M:%S')
        return Note(note_dict['title'], note_dict['content'], note_date)

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, default=self._note_encoder)

    def _note_encoder(self, note):
        return {'title': note.title, 'content': note.content, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')}

    def create_note(self, title, content):
        current_date = datetime.now()
        note = Note(title, content, current_date)
        self.notes.append(note)
        self.save_notes()

    def list_notes(self, date_filter=None):
        for idx, note in enumerate(self.notes):
            if date_filter is None or note.date.date() == date_filter.date():
                print(f"\n{idx + 1}. {note.title} ({note.date.strftime('%Y-%m-%d %H:%M:%S')})")

    def read_note(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            print(f"\nЗаголовок: {note.title}\nСодержание: {note.content}")
        else:
            print("\nНедопустимый индекс заметки")

    def edit_note(self, index, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index].content = new_content
            self.save_notes()
            print("\nЗаметка обновлена")
        else:
            print("\nНедопустимый индекс заметки")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
            print("\nЗаметка удалена")
        else:
            print("\nНедопустимый индекс заметки")
