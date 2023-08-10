import json
from datetime import datetime


class Note:
    def __init__(self, id, title, content, creation_date, last_modified=None):
        self.id = id
        self.title = title
        self.content = content
        self.creation_date = creation_date
        self.last_modified = last_modified

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
        note_date = datetime.strptime(note_dict['creation_date'], '%Y-%m-%d %H:%M:%S')
        last_modified = datetime.strptime(note_dict['last_modified'], '%Y-%m-%d %H:%M:%S') if note_dict['last_modified'] else None
        return Note(note_dict['id'], note_dict['title'], note_dict['content'], note_date, last_modified)

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, default=self._note_encoder)

    def _note_encoder(self, note):
        return {'id': note.id, 'title': note.title, 'content': note.content, 'creation_date': note.creation_date.strftime('%Y-%m-%d %H:%M:%S'), 'last_modified': note.last_modified.strftime('%Y-%m-%d %H:%M:%S') if note.last_modified else None}

    def create_note(self, title, content):
        current_date = datetime.now()
        new_id = len(self.notes) + 1
        note = Note(new_id, title, content, current_date)
        self.notes.append(note)
        self.save_notes()

    def list_notes(self, date_filter=None):
        if not self.notes:
            print("\nНет заметок")
            return

        for idx, note in enumerate(self.notes):
            if date_filter is None or note.creation_date.date() == date_filter:
                last_modified_str = note.last_modified.strftime('%Y-%m-%d %H:%M:%S') if note.last_modified else "Нет данных"
                print(f"\n{idx + 1}. {note.title} (Создано: {note.creation_date.strftime('%Y-%m-%d %H:%M:%S')}, Последнее изменение: {last_modified_str})")

    def read_note(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            print(f"\nЗаголовок: {note.title}\nСодержание: {note.content}")
        else:
            print("\nНедопустимый индекс заметки")

    def edit_note(self, index, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index].content = new_content
            self.notes[index].last_modified = datetime.now()
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
