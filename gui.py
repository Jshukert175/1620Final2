from tkinter import *
import csv

class Gui:
    """
    Class to create the GUI
    """
    def __init__(self, window) -> None:
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
        self.frame_three.pack(anchor='w', padx=10, pady=10)

        self.frame_four = Frame(self.window)
        self.button_submit = Button(self.frame_four, text="Submit", command=self.submit)
        self.label_message = Label(self.frame_four, text="")

        self.label_message.pack(side='bottom')
        self.button_submit.pack(side='bottom')
        self.frame_four.pack()


    def attempt_nums(self):
        pass
        #self.frame_four.pack(anchor='w', padx=10, pady=10)

    def submit(self):
        """
        Method to submit name and attempts
        :return:
        """
        #Name
        name = self.input_name.get().strip()
        if len(name) == 0:
            self.label_message.config(text="Please enter a name")
        #Attempt num
        try:
            attempts = int(self.input_attempts.get())
            if attempts > 4 or attempts < 1:
                raise ValueError
        except ValueError:
            self.label_message.config(text="Invalid input", fg="red")
            return
        scores = []
        for a in range(1, attempts + 1):
            self.score_label = Label(self.frame_three, text=f"Score {a}:")
            self.score_label.grid(row=a, column=0)
            self.score_list = Entry(self.frame_three)
            self.score_list.grid(row=a, column=1)


        for s in range(4):
            if s < 0:
                s = 0
                scores.append(s)
            else:
                scores.append(s)
        with open('data.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Final"])
            content.writerow([name, scores[0], scores[1], scores[2], scores[3], max(scores)])

        self.input_name.delete(0, END)
        self.input_attempts.delete(0, END)
        self.label_message.config(text="Submitted", fg="red")
        self.input_name.focus()