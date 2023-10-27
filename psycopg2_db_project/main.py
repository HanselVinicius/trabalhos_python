from controllers.db.FactoryDb import DbFactory
import tkinter as tk
from view.MainView import MainView
def main():
    DbFactory.create_alunos_tb()
    win = tk.Tk()
    mainView = MainView(win)
    win.title("Application")
    win.geometry("820x600+10+10")
    win.mainloop()
main()