from tkinter import *


class Adder(object):
    """
    Implements an adding machine using a Tkinter GUI
    Call the method display to initiate the display
    """
    def display(self):
        """
        Display the user interface
        Returns when the interface is closed by the user
        """

        root = Tk()

        first_number_label = Label(root, text='First Number')
        first_number_label.grid(sticky=E, padx=5, pady=5, row=0, column=0)

        first_number_entry = Entry(root, width=10)
        first_number_entry.grid(padx=5, pady=5, row=0, column=1)

        second_number_label = Label(root, text='Second number')
        second_number_label.grid(sticky=E, padx=5, pady=5, row=1, column=0)

        second_number_entry = Entry(root, width=10)
        second_number_entry.grid(padx=5, pady=5, row=1, column=1)

        result_label = Label(root, text='Result')
        result_label.grid(sticky=E + W, padx=5, pady=5, row=3, column=0, columnspan=2)


        def do_add():
            first_number_text = first_number_entry.get()
            try:
                first_number = float(first_number_text)
            except ValueError:
                result_label.config(text='Invalid first number')
                return
            second_number_text = second_number_entry.get()
            try:
                second_number = float(second_number_text)
            except ValueError:
                result_label.config(text='Invalid second number')
                return
            
            result = first_number + second_number
            result_label.config(text=str(result))

        add_button = Button(root, text='Add numbers', command=do_add)
        add_button.grid(sticky=E + W, row=2, column=0, columnspan=2, padx=5, pady=5)

        root.mainloop()


if __name__ == '__main__':
    app = Adder()
    app.display()


