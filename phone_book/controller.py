
import view
import model_add
import model_del
import model_finde
import model_show

def button_click():
    # data = init.set_data()
    user_choice = view.show_menu()
    while user_choice != '5':
        if user_choice == '1':
            model_add.add_contact()
        elif user_choice == '2':
            model_del.del_contact()
        elif user_choice == '3':
            model_finde.finde_contact()
        elif user_choice == '4':
            model_show.show_all()
        else:
            break
        user_choice = view.show_menu()