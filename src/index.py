from tkinter import Tk
from ui.ui import UI, initRoot
import database

def main():
    connection = database.connect()

    root = Tk()
    initRoot(root)

    view = UI(root, connection)
    view.start()

    root.mainloop()


if __name__ == "__main__":
    main()
