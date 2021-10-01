from tkinter import *


class GraphWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent

    def handle_closeGraph(self):
        self.destroy()

    def setEquation(self, equation):
        self.equation = equation


def main():
    pass


if __name__ == "__main__":
    main()
