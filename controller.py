import text_fields as tf
import view
import model


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(tf.open_successful)
            case 2:
                model.safe_file()
                view.print_message(tf.safe_successful)
            case 3:
                pb = model.phone_book
                view.show_contact(pb, tf.no_phone_book)
            case 4:
                new_contact = view.input_contact(tf.new_contact)
                model.add_contact(new_contact)
                view.print_message(tf.add_successful)
            case 5:
                word = view.enter_keyword()
                result = model.find_contact(word)
                view.show_contact(result, tf.not_found(word))
            case 6:
                pb = model.get_phone_book()
                view.show_contact(pb, tf.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view.edit_contact(pb, tf.input_index)
                    model.edit_contact(edited_contact)
                    view.print_message(tf.successful_edited(edited_contact[1].get('name')))
            case 7:
                pb = model.get_phone_book()
                view.show_contact(pb, tf.empty_list_or_not_open_file)
                if pb:
                    index = view.input_index(pb, tf.input_delete_index)
                if view.confirm(tf.confirm_delete(pb[index - 1].get('name'))):
                    view.print_message(tf.delete_contact(model.delete_contact(index)))
            case 8:
                if model.original_book != model.phone_book:
                    if view.confirm(tf.no_saved_book):
                        model.safe_file()
                view.print_message(tf.bye)
                break
