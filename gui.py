from tkinter import *
import csv

class Gui:
    """
    Class to create the GUI
    """
    def __init__(self, window) -> None:
        """
        Method to build widgets
        :param window: Gui window
        """
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
        self.attempt_save = Button(self.frame_three, text="Save", command=self.save)

        self.frame_three.pack()
        self.attempt_save.pack(side='bottom', padx=10, pady=10)

        self.score_label1 = Label(self.frame_three, text=f"Score 1:")
        self.score_list1 = Entry(self.frame_three)

        self.score_label2 = Label(self.frame_three, text=f"Score 2:")
        self.score_list2 = Entry(self.frame_three)

        self.score_label3 = Label(self.frame_three, text=f"Score 3:")
        self.score_list3 = Entry(self.frame_three)

        self.score_label4 = Label(self.frame_three, text=f"Score 4:")
        self.score_list4 = Entry(self.frame_three)

        self.frame_four = Frame(self.window)
        self.button_submit = Button(self.frame_four, text="Submit", command=self.submit)
        self.label_message = Label(self.frame_four, text="")

        self.label_message.pack(side='bottom')
        self.button_submit.pack(side='bottom')
        self.frame_four.pack()


    def save(self) -> None:
        """
        Method to submit number of attempts so scores can be input
        """
        # Name
        name = self.input_name.get().strip()
        if len(name) == 0:
            self.label_message.config(text="Please enter a name")
            return
        # Attempt num
        try:
            attempts = int(self.input_attempts.get())
            if attempts > 4 or attempts < 1:
                raise ValueError
        except ValueError:
            self.label_message.config(text="Enter 1 to 4", fg="red")
            return
        if attempts == 1:
            self.score_label1.pack()
            self.score_list1.pack()

            self.score_label2.pack_forget()
            self.score_list2.pack_forget()
            self.score_label3.pack_forget()
            self.score_list3.pack_forget()
            self.score_label4.pack_forget()
            self.score_list4.pack_forget()
        elif attempts == 2:
            self.score_label1.pack()
            self.score_list1.pack()
            self.score_label2.pack()
            self.score_list2.pack()

            self.score_label3.pack_forget()
            self.score_list3.pack_forget()
            self.score_label4.pack_forget()
            self.score_list4.pack_forget()
        elif attempts == 3:
            self.score_label1.pack()
            self.score_list1.pack()
            self.score_label2.pack()
            self.score_list2.pack()
            self.score_label3.pack()
            self.score_list3.pack()

            self.score_label4.pack_forget()
            self.score_list4.pack_forget()
        elif attempts == 4:
            self.score_label1.pack()
            self.score_list1.pack()
            self.score_label2.pack()
            self.score_list2.pack()
            self.score_label3.pack()
            self.score_list3.pack()
            self.score_label4.pack()
            self.score_list4.pack()

    def submit(self) -> None:
        """
        Method to submit name and scores
        """

        #Get all 4 scores
        name = self.input_name.get().strip()
        scores = []
        try:
            if len(self.score_list1.get()) == 0:
                self.label_message.config(text="Please enter a number 0-100", fg="red")
            else:
                scores.append(int(self.score_list1.get()))
            if len(self.score_list2.get()) != 0:
                scores.append(int(self.score_list2.get()))
            else:
                scores.append(0)
            if len(self.score_list3.get()) != 0:
                scores.append(int(self.score_list3.get()))
            else:
                scores.append(0)
            if len(self.score_list4.get()) != 0:
                scores.append(int(self.score_list4.get()))
            else:
                scores.append(0)
            # Check score ranges (less than 0 or greater than 100)
            for s in scores:
                if s < 0 or s > 100:
                    raise ValueError
        except ValueError:
            self.label_message.config(text="Enter a score between 0 and 100", fg="red")
            return






        with open('data.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Final"])
            content.writerow([name, scores[0], scores[1], scores[2], scores[3], max(scores)])

        self.input_name.delete(0, END)
        self.input_attempts.delete(0, END)
        self.label_message.config(text="Submitted", fg="green")
        self.input_name.focus()