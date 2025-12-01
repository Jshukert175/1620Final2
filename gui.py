from tkinter import *
import csv

class Gui:
    """
    Class to create the GUI
    """
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text="Student name:")
        self.input_name = Entry(self.frame_name)

        self.label_name.pack(side='left')
        self.input_name.pack(padx=5)
        self.frame_name.pack(anchor='w', padx=10, pady=10)

        self.frame_two = Frame(self.window)
        self.label_attempts = Label(self.frame_two, text="No of attempts:")
        self.input_attempts = Entry(self.frame_two)

        self.label_attempts.pack(side='left')
        self.input_attempts.pack(padx=5)
        self.frame_two.pack(anchor='w', padx=10, pady=10)

        self.frame_three = Frame(self.window)
        self.button_submit = Button(self.frame_three, text="Submit", command=self.submit)
        self.label_message = Label(self.frame_three, text="")

        self.label_message.pack(side='bottom')
        self.button_submit.pack(side='bottom')
        self.frame_three.pack()

    def submit(self):
        """
        Method to submit name and attempts
        :return:
        """

        try:
            attempts = self.input_attempts.get()
            if int(attempts) > 4:
                raise ValueError
        except ValueError:
            self.label_message.config(text="Invalid input")
            return