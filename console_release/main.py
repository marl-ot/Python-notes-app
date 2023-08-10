import argparse
from datetime import datetime
from note import NoteManager


def main():
    parser = argparse.ArgumentParser(description="Управление заметками")

    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    add_parser = subparsers.add_parser("add", help="Добавить новую заметку")
    add_parser.add_argument("--title", required=True, help="Заголовок заметки")
    add_parser.add_argument("--content", required=True, help="Содержание заметки")

    list_parser = subparsers.add_parser("list", help="Вывести список заметок")
    list_parser.add_argument("--date", help="Фильтр по дате (в формате 'гггг-мм-дд')")

    read_parser = subparsers.add_parser("read", help="Прочитать заметку по индексу")
    read_parser.add_argument("index", type=int, help="Индекс заметки")

    edit_parser = subparsers.add_parser("edit", help="Редактировать заметку по индексу")
    edit_parser.add_argument("index", type=int, help="Индекс заметки")
    edit_parser.add_argument("--content", required=True, help="Новое содержание заметки")

    delete_parser = subparsers.add_parser("delete", help="Удалить заметку по индексу")
    delete_parser.add_argument("index", type=int, help="Индекс заметки")

    args = parser.parse_args()

    note_manager = NoteManager("notes.json")
    note_manager.load_notes()

    if args.command == "add":
        note_manager.create_note(args.title, args.content)
    elif args.command == "list":
        date_filter = None
        if args.date:
            date_filter = datetime.strptime(args.date, '%Y-%m-%d').date()
        note_manager.list_notes(date_filter)
    elif args.command == "read":
        note_manager.read_note(args.index - 1)
    elif args.command == "edit":
        note_manager.edit_note(args.index - 1, args.content)
    elif args.command == "delete":
        note_manager.delete_note(args.index - 1)
    else:
        print("\nНедопустимая команда. Пожалуйста, используйте 'add', 'list', 'read', 'edit' или 'delete'")


if __name__ == "__main__":
    main()
