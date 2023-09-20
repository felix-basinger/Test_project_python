from datetime import datetime

import text


def menu() -> int:
    print(text.menu[0])
    for i in range(1, len(text.menu)):
        print(f"\t{i}. {text.menu[i]}")
    while True:
        selected = input(text.select_menu)
        if 0 < int(selected) <= len(text.menu):
            return int(selected)
        print(text.invalid_selection)


def show_nodes(note: dict, message):
    if note:
        # sorted(note.items(), key=lambda x: x["title"], reverse=True)
        for index, note in note.items():
            print(f'{index:<3}. {note.get("title"):<50}\n{note.get("body"):<250}\n{note.get("date"):<20}')
    else:
        print_message(message)


def print_message(message):
    print(message)


def add_note():
    new_note = {}
    for key, value in text.new_note.items():
        new_note[key] = input(value)
    new_note['date'] = datetime.now().isoformat(sep=',', timespec='minutes')
    return new_note


def view_input(text: str):
    return input(text)
