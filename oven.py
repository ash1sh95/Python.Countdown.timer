import threading
import tkinter as tk
from tkinter import messagebox
import time


class countdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("460x220")
        self.root.title("Microwave oven")
        self.start_button = tk.Button(self.root, font=("Helvetica", 30), text="Start", command=self.start_thread)
        self.start_button.place(x=30, y=120)

        self.start_button = tk.Button(self.root, font=("Helvetica", 30), text="Stop", command=self.stop)
        self.start_button.place(x=150, y=120)
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()

        self.popcorn_button = tk.Button(self.root, font=("Helvetica", 30), text="Popcorn", command=self.popcorn)
        self.popcorn_button.place(x=250, y=120)

        # defaults to 0
        self.minutes.set("00")
        self.seconds.set("00")
        self.minuteEntry = tk.Entry(self.root, width=3, font=("Helvetica", 30),
                                    textvariable=self.minutes)
        self.minuteEntry.place(x=85, y=20)

        self.secondEntry = tk.Entry(self.root, width=3, font=("Helvetica", 30),
                                    textvariable=self.seconds)
        self.secondEntry.place(x=130, y=20)

        self.stop_loop = False
        self.popcorn = False

        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def popcorn(self):
        self.popcorn = True
        self.start_thread()

    def start(self):
        self.stop_loop = False
        if (self.popcorn == True):
            full_seconds = 120
            tk.messagebox.showinfo("popcorn selected, popcorn coming up in 2 minutes")
        else:
            full_seconds = int(self.minutes.get()) * 60 + int(self.seconds.get())

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            if minutes > 60:
                minutes = divmod(minutes, 60)

            self.minutes.set("{0:2d}".format(minutes))
            self.seconds.set("{0:2d}".format(seconds))
            self.root.update()
            time.sleep(1)
        if not self.stop_loop:
            tk.messagebox.showinfo("Time Countdown", "Time's up ")

    def stop(self):
        self.stop_loop = True


countdownTimer()
