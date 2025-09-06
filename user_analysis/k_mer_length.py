import tkinter
import math
from customtkinter import *
from tkinter import *
from DNAtoolkit.DNAtools import *
from interface.GUI_attr import *


class K_mer_Length:

    def __init__(self, username, firstname, lastname, DNA_data, sequence_type, menu_window):

        # Useful Variables
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.DNA_data = DNA_data
        self.sequence_type = sequence_type
        self.menu_window = menu_window
        # Helpful Variables
        self.isReverse = "False"
        self.reverse_switch = 0
        self.start, self.stop = 0, view_limit
        # Update Once k_mer_dict length Is Got
        self.k_mer_dict_length = 0
        # Window
        self.window = Tk()
        self.window.title("K-mer Length")
        self.window.config(bg=color_scheme)
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.propagate(True)
        self.window.eval("tk::PlaceWindow . center")
        self.window.resizable(False, False)
        """ k-mer Length Heading """
        self.k_mer_heading = CTkLabel(self.window, text="K-mer Length", font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=text_color)
        self.k_mer_heading.pack(side='top', pady=5)
        """ Frame For Read Index And Length """
        self.frame_1 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_1.pack(fill='both', expand=True)
        """ Read Index And Length Entry """
        self.read_index_entry = CTkEntry(self.frame_1, placeholder_text="Enter Read Index", placeholder_text_color=bright_colors[0],
                                         text_color=bright_colors[5], fg_color=color_scheme, font=(window_font, window_font_size),
                                         border_color=bright_colors[2], border_width=border, height=50, width=350)
        self.read_index_entry.pack(side='left', padx=10, pady=10)
        self.length_entry = CTkEntry(self.frame_1, placeholder_text="Enter Length", placeholder_text_color=bright_colors[0],
                                     text_color=bright_colors[5], fg_color=color_scheme, font=(window_font, window_font_size),
                                     border_color=bright_colors[2], border_width=border, height=50, width=350)
        self.length_entry.pack(side='right', padx=10, pady=10)
        """ Frame For Buttons """
        self.middle_frame = CTkFrame(self.window, fg_color=color_scheme)
        self.middle_frame.pack(fill='both')
        """ Buttons """
        self.search_length = CTkButton(self.middle_frame, text="Search", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner, height=50,
                                       command=self.get_k_mer)
        self.search_length.pack(fill='both', side="left", padx=10, pady=10, expand=True)
        self.isReversed = CTkButton(self.middle_frame, text="Reverse", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner, height=50,
                                       command=self.set_reversed)
        self.isReversed.pack(fill='both', side="right", padx=10, pady=10, expand=True)
        """ Frane For Information """
        self.frame_2 = CTkFrame(self.window, fg_color=bright_colors[2], height=50)
        self.frame_2.pack(fill='both', padx=10, pady=10)
        """ Label For K-mer Count """
        self.appearance_label = CTkLabel(self.frame_2, text="Appearance(s):", fg_color=bright_colors[2],
                                          text_color=bright_colors[4], font=(window_font, (window_font_size - 10), font_style))
        self.appearance_label.grid(row=0, column=0, sticky='w',padx=10, pady=10)
        """ K-mer Count """
        self.appearance = CTkLabel(self.frame_2, text="None,", fg_color=bright_colors[2],
                                    text_color=bright_colors[4], font=(window_font, (window_font_size - 10)))
        self.appearance.grid(row=0, column=1, sticky='w', pady=10)
        """ Label For Length """
        self.length_label = CTkLabel(self.frame_2, text="Length:", fg_color=bright_colors[2],
                                         text_color=bright_colors[4], font=(window_font, (window_font_size - 10), font_style))
        self.length_label.grid(row=0, column=2, sticky='w', pady=10, padx=10)
        """ Length """
        self.length = CTkLabel(self.frame_2, text="None,", fg_color=bright_colors[2],
                                   text_color=bright_colors[4], font=(window_font, (window_font_size - 10)))
        self.length.grid(row=0, column=3, sticky='w', pady=10)
        """ Label For Reverse Complement """
        self.reverse_label = CTkLabel(self.frame_2, text="ReverseComplement:", fg_color=bright_colors[2],
                                     text_color=bright_colors[4], font=(window_font, (window_font_size - 10), font_style))
        self.reverse_label.grid(row=0, column=4, sticky='w', pady=10, padx=10)
        """ Reverse """
        self.reverse = CTkLabel(self.frame_2, text=f"{self.isReverse}", fg_color=bright_colors[2],
                               text_color=bright_colors[4], font=(window_font, (window_font_size - 10)))
        self.reverse.grid(row=0, column=5, sticky='w', pady=10)
        """ Frame For Analysis """
        self.frame_3 = CTkScrollableFrame(self.window, fg_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                          scrollbar_button_color=bright_colors[3], scrollbar_button_hover_color=bright_colors[3],
                                          height=300, orientation=HORIZONTAL)
        self.frame_3.pack(fill='both')
        """ Frame For Navigation Buttons """
        self.frame_4 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_4.pack(fill='both')
        # Navigation Buttons
        move_left = CTkButton(self.frame_4, text='<', fg_color=color_scheme, hover_color=color_scheme, text_color=bright_colors[4],
                              font=(window_font, window_font_size), command=lambda: self.move_pages("Left"))
        move_left.pack(side='left')
        self.tracker_label = CTkLabel(self.frame_4, text='', font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=bright_colors[5])
        self.tracker_label.place(relx=0.45, rely=0.0)
        move_right = CTkButton(self.frame_4, text='>', fg_color=color_scheme, hover_color=color_scheme, text_color=bright_colors[4],
                               font=(window_font, window_font_size), command=lambda: self.move_pages("Right"))
        move_right.pack(side='right')
        self.menu = CTkButton(self.window, text="Menu", text_color=bright_colors[4], fg_color=color_scheme,
                                       hover_color=bright_colors[2], font=(window_font, window_font_size),
                                       corner_radius=corner, command=self.call_menu)
        self.menu.pack(fill='both', padx=10, pady=10)
        self.window.mainloop()


    def move_pages(self, direction):

        """ Navigates Pages """
        if direction == "Left":
            if self.start >= view_limit:
                self.start -= view_limit
                self.stop -= view_limit
                self.get_k_mer()
                try:
                    self.tracker_label.configure(text=f"{(self.start // view_limit) + 1}/{math.ceil(self.k_mer_dict_length / view_limit)}") if self.k_mer_dict_length >= 1 else 0
                except tkinter.TclError:
                    return
        elif direction == "Right":
            if self.stop < self.k_mer_dict_length:
                self.start += view_limit
                self.stop += view_limit
                self.get_k_mer()
                try:
                    self.tracker_label.configure(text=f"{(self.start // view_limit) + 1}/{math.ceil(self.k_mer_dict_length / view_limit)}") if self.k_mer_dict_length >= 1 else 0
                except tkinter.TclError:
                    return


    def call_menu(self):

        """ Calling Menu """
        try: self.window.destroy()
        except tkinter.TclError: return
        self.menu_window(self.username, self.firstname, self.lastname)


    def set_reversed(self):

        """ Managing Reverse Complement """
        try:
            # Setting Values To None
            self.appearance.configure(text="None,")
            self.length.configure(text="None,")
            # Cleaning Frame
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        except tkinter.TclError:
            return
        if self.reverse_switch == 0:
            self.isReverse = "True"
            try: self.reverse.configure(text='True')
            except tkinter.TclError: return
            self.reverse_switch = 1
            return
        elif self.reverse_switch == 1:
            self.isReverse = "False"
            try: self.reverse.configure(text="False")
            except tkinter.TclError: return
            self.reverse_switch = 0
            return
        return


    def get_k_mer(self):

        """ Making and Showing K-mer """
        try:
            # Cleaning Frame
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        except tkinter.TclError:
            return
        if not str(self.read_index_entry.get()):
            try:
                # Setting Values To None
                self.appearance.configure(text="None,")
                self.length.configure(text="None,")
            except tkinter.TclError:
                return
            # Error
            error_label_1 = CTkLabel(self.window, text="Empty Read Index", font=(window_font, window_font_size),
                                     fg_color=color_scheme, text_color=bright_colors[1])
            error_label_1.place(relx=0.4, rely=0.4)
            try: self.window.after(1000, error_label_1.destroy)
            except tkinter.TclError: return
            return
        # Our Dictionary For Highest K-mer By Length
        k_mer_dict = dict()
        for key, value in self.DNA_data.items():
            if key == str(self.read_index_entry.get()):
                if self.isReverse == "True":
                    k_mer_dict = highest_k_mer_len(reverseComplement(value, self.sequence_type), self.length_entry.get())
                elif self.isReverse == "False":
                    k_mer_dict = highest_k_mer_len(value, self.length_entry.get())
                if k_mer_dict == -1:
                    try:
                        # Setting Values To None
                        self.appearance.configure(text="None,")
                        self.length.configure(text="None,")
                    except tkinter.TclError:
                        return
                    # Error
                    error_label_1 = CTkLabel(self.window, text="Empty Seq", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_1.place(relx=0.4, rely=0.4)
                    try: self.window.after(1000, error_label_1.destroy)
                    except tkinter.TclError: return
                    return
                elif k_mer_dict == -2 or k_mer_dict == -3:
                    try:
                        # Setting Values To None
                        self.appearance.configure(text="None,")
                        self.length.configure(text="None,")
                    except tkinter.TclError:
                        return
                    # Error
                    error_label_2 = CTkLabel(self.window, text="Bad Length", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_2.place(relx=0.4, rely=0.4)
                    try: self.window.after(1000, error_label_2.destroy)
                    except tkinter.TclError: return
                    return
                # If No Errors
                self.k_mer_dict_length = len(k_mer_dict.keys())
                for i, (x, y) in enumerate(list(k_mer_dict.items())[self.start: self.stop]):
                    CTkLabel(self.frame_3, text=str(x), text_color=color_scheme, fg_color=bright_colors[3],
                             font=(window_font, window_font_size - 10)).grid(row=i, column=0, sticky='w', padx=1, pady=1)
                    p = CTkProgressBar(self.frame_3, fg_color=bright_colors[3], corner_radius=corner)
                    p.set(y / max(list(k_mer_dict.values())))
                    p.grid(row=i, column=1, sticky='w', padx=1, pady=1)
                    CTkLabel(self.frame_3, text=str(y), text_color=color_scheme, fg_color=bright_colors[3],
                             font=(window_font, window_font_size - 10)).grid(row=i, column=2, sticky='w', padx=1, pady=1)
                try:
                    self.appearance.configure(text=f"{sum(list(k_mer_dict.values()))},")
                    self.length.configure(text=f"{len(value)},")
                except tkinter.TclError:
                    return
                return