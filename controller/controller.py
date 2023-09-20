import text
from model import model
from view import view


def start():
    na = model.NotesApp()
    while True:
        select = view.menu()
        match select:
            case 1:
                if na.open():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if na.save():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_nodes(na.get(), text.empty_note)
            case 4:
                new = view.add_note()
                na.add(new)
                view.print_message(text.add_successful(new.get('title')))
            case 5:
                word = view.view_input(text.search_word)
                result = na.find(word)
                view.show_nodes(result, text.empty_search(word))
            case 6:
                index = view.view_input(text.index_update)
                new_note = view.add_note()
                na.update(index, new_note)
            case 7:
                word = view.view_input(text.search_word)
                result = na.find(word)
                view.show_nodes(result, text.empty_search(word))
                index = view.view_input(text.index_update)
                name = na.remove(index)
                view.print_message(text.remove_contact(name))

            case 8:
                view.print_message(text.goodbay)
                break