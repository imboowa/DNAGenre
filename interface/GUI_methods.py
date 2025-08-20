from customtkinter import *
from tkinter import *

def animate_words(window, text, label, count=0):

    """ Animates Text In The Window """
    if count < len(text):
        label.configure(text=text[:count + 1])
        label.after(300, animate_words, window, text, label, count + 1)

def time_calculator(counter=0):

    """ Returns Elapsed Time """
    seconds = int(counter) % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600) % 24
    days = int(counter / 86400) % 7
    weeks = int(counter / 604800)
    return weeks, days, hours, minutes, seconds

def custom_progressbar_tips(the_window: Tk, frame: CTkFrame, label_fg_color: str, label: CTkLabel, step: int=0, total_steps: int=5) -> None:

    """ Needs A Frame To Put Labels Hence Animate It As A Progressbar """
    if step < total_steps:
        CTkLabel(frame, text='', fg_color=label_fg_color, corner_radius=5, width=50, height=50).pack(side='left', padx=5, pady=5)
        the_window.after(1000, lambda: custom_progressbar_tips(the_window, frame, label_fg_color, label, step+1, total_steps))
    else:
        if label.winfo_exists():
            label.destroy()
        if frame.winfo_exists():
            frame.destroy()
    return None