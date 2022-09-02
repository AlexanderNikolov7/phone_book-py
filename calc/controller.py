import init
import view
import model_sum
import model_mult
import model_sub
import model_div

def button_click():
    view.new_string()
    data = init.set_data()
    if data[2] == '+':
        view.show_data(model_sum.sum(data[0], data[1]))
    elif data[2] == '*':
        view.show_data(model_mult.mult(data[0], data[1]))
    elif data[2] == '-':
        view.show_data(model_sub.sub(data[0], data[1]))
    elif data[2] == '/':
        view.show_data(model_div.div(data[0], data[1]))


