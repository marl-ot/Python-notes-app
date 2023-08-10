from note import NoteManager


def main():
    note_manager = NoteManager("notes.json")
    note_manager.load_notes()

    while True:
        print("\nМеню:")
        print("\t1. Создать заметку")
        print("\t2. Список заметок")
        print("\t3. Прочитать заметку")
        print("\t4. Редактировать заметку")
        print("\t5. Удалить заметку")
        print("\t6. Сохранить и выйти")

        choice = input("Введите ваш выбор: ")
        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            note_manager.create_note(title, content)
        elif choice == '2':
            note_manager.list_notes()
        elif choice == '3':
            index = int(input("Введите индекс заметки: ")) - 1
            note_manager.read_note(index)
        elif choice == '4':
            index = int(input("Введите индекс заметки: ")) - 1
            new_content = input("Введите новое содержание заметки: ")
            note_manager.edit_note(index, new_content)
        elif choice == '5':
            index = int(input("Введите индекс заметки: ")) - 1
            note_manager.delete_note(index)
        elif choice == '6':
            break
        else:
            print("Недопустимый выбор. Пожалуйста, выберите корректный вариант")


if __name__ == "__main__":
    main()
