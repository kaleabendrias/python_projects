from tkinter import *
from tkinter import messagebox


class Converter(object):
    """
     Displays a Tkinter user interface to convert between Fahrenheit and centigrade
     Call the display function to display the converter on the screen
     """

    def display(self):
        """
         Displays the converter window
         When the window is closed, this method completes
         """
        root = Tk()

        cent = Label(root, text='centigrade')
        cent.grid(row=0, column=0, stick=E, padx=5, pady=5)

        fah = Label(root, text='fahrenheit')
        fah.grid(row=2, column=0, padx=5, pady=5)

        cent_entry = Entry(root)
        cent_entry.grid(row=0, column=1, padx=5, pady=5)

        fah_entry = Entry(root)
        fah_entry.grid(row=2, column=1, padx=5, pady=5)

        def fah_to_cent():
            fah_string = fah_entry.get()
            try:
                fah_float = float(fah_string)
                result = (fah_float - 32) / 1.89
                cent_entry.delete(0, END)
                cent_entry.insert(0, str(result))
            except ValueError:
                cent_entry.delete(0, END)
                cent_entry.insert(0, 'Error')

        def cent_to_fah():
            cent_string = cent_entry.get()
            try:
                cent_float = float(cent_string)
                result = cent_float * 1.89 + 32
                fah_entry.delete(0, END)
                fah_entry.insert(0, result)
            except ValueError:
                fah_entry.delete(0, END)
                fah_entry.insert(0, 'Error')

        fah_to_cent = Button(root, text='Fah_to_cent', command=fah_to_cent)
        fah_to_cent.grid(row=1, column=0, stick=E, padx=0, pady=0)

        cent_to_fah = Button(root, text='cent_to-fah', command=cent_to_fah)
        cent_to_fah.grid(row=1, column=1, padx=5, pady=5)

        root.mainloop()


if __name__ == '__main__':
    app = Converter()
    app.display()
