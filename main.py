from gui import *

def main():
    """
    Main function
    """
    window = Tk()
    window.title("Final 2")
    window.geometry("300x300")
    window.resizable(False, False)
    Gui(window)

    window.mainloop()

if __name__ == "__main__":
    main()