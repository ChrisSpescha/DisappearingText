from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time


class App:
    def __init__(self):
        Label(text="").grid(row=0, column=0)
        self.text = ScrolledText()
        self.text.grid(row=1, column=1)
        self.state = 'startup'
        self.start = 0

    def loop(self):
        if self.state == 'startup':
            Label(text="Start Typing").grid(row=0, column=1)
        elif self.state == 'running':
            Label(text="Don't Stop!").grid(row=0, column=1)
            root.after(5000, self.check_time)

    def check_time(self):
        current_time = time.time()
        elapsed = current_time - self.start
        if elapsed > 5:
            self.state = 'startup'
            Label(text="Start Typing").grid(row=0, column=1)
            self.text.delete(1.0, END)

    def key(self, event):
        if self.state == 'startup':
            self.state = 'running'
        self.start = time.time()
        self.loop()


root = Tk()
game_app = App()
root.bind('<Key>', game_app.key)
root.title('FreeFlow')
root.after(20, game_app.loop)
root.geometry("675x400")
root.mainloop()
