from user_analysis.k_mer_length import *


class K_mer_Search:

    def __init__(self, username, firstname, lastname, DNA_data, sequence_type, menu_window, signing_window):

        # Useful Variables
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.DNA_data = DNA_data
        self.sequence_type = sequence_type
        self.menu_window = menu_window
        self.signing_window = signing_window
        # Helpful Variables
        self.isReverse = "False"
        self.reverse_switch = 0
        # Window
        self.window = Tk()
        self.window.title("K-mer Search")
        self.window.config(bg=color_scheme)
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.eval("tk::PlaceWindow . center")
        self.window.propagate(True)
        self.window.resizable(False, False)
        """ K_mer Analysis Header """
        k_mer_header = CTkLabel(self.window, text="K-mer Search", font=(window_font, window_font_size),
                                fg_color=color_scheme, text_color=text_color)
        k_mer_header.pack(fill="both", pady=5, side='top')
        """ Frame For Read Index and K_mer """
        self.frame_1 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_1.pack(fill='both', pady=50, expand=True)
        """ Putting Read Index Entry and K_mer Entry Into Frame """
        self.read_index_entry = CTkEntry(self.frame_1, placeholder_text="Enter Read Index", placeholder_text_color=bright_colors[0],
                                         text_color=bright_colors[5], border_color=bright_colors[2], border_width=border,
                                         height=50, width=350, font=(window_font, window_font_size), fg_color=color_scheme)
        self.read_index_entry.pack(side='left', padx=10, pady=10)
        self.k_mer_entry = CTkEntry(self.frame_1, placeholder_text="Enter k-mer", placeholder_text_color=bright_colors[0],
                                         text_color=bright_colors[5], border_color=bright_colors[2], border_width=border,
                                         height=50, width=350, font=(window_font, window_font_size), fg_color=color_scheme)
        self.k_mer_entry.pack(side='right', pady=10, padx=10)
        """ Frame For Buttons """
        self.middle_frame = CTkFrame(self.window, fg_color=color_scheme)
        self.middle_frame.pack(fill='both')
        """ Buttons """
        self.search_button = CTkButton(self.middle_frame, text="Search", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                       height=50, command=lambda: self.show_k_mer(True))
        self.search_button.pack(fill='both', side='left', padx=10, expand=True)
        self.reverse_button = CTkButton(self.middle_frame, text="Reverse", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                       height=50, command=self.set_reversed)
        self.reverse_button.pack(fill='both', side='right', padx=10, expand=True)
        """ Frane For K-mer Count And ReverseComplement """
        self.frame_2 = CTkFrame(self.window, fg_color=bright_colors[2], height=50)
        self.frame_2.pack(fill='both', padx=10, pady=10)
        """ Label For K-mer Count """
        self.k_mer_count_label = CTkLabel(self.frame_2, text="K-mer Count:", fg_color=bright_colors[2], text_color=bright_colors[4],
                                    font=(window_font, (window_font_size - 10), font_style))
        self.k_mer_count_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        """ K-mer Count """
        self.k_mer_count = CTkLabel(self.frame_2, text="None,", fg_color=bright_colors[2],
                                          text_color=bright_colors[4],
                                          font=(window_font, (window_font_size - 10)))
        self.k_mer_count.grid(row=0, column=1, sticky='w', pady=10)
        """ Label For isReversed """
        self.isReversed_label = CTkLabel(self.frame_2, text="Reverse Complement:", fg_color=bright_colors[2],
                                          text_color=bright_colors[4], font=(window_font, (window_font_size - 10), font_style))
        self.isReversed_label.grid(row=0, column=2, sticky='w', padx=10, pady=10)
        """ isReversed """
        self.isReversed = CTkLabel(self.frame_2, text=f"{self.isReverse}", fg_color=bright_colors[2],
                                    text_color=bright_colors[4], font=(window_font, (window_font_size - 10)))
        self.isReversed.grid(row=0, column=3, sticky='w', pady=10)
        """ Frame For K-mer """
        self.frame_3 = CTkScrollableFrame(self.window, scrollbar_fg_color=bright_colors[3], scrollbar_button_color=bright_colors[3],
                                          scrollbar_button_hover_color=bright_colors[3], fg_color=bright_colors[3], orientation=HORIZONTAL,
                                          height=100)
        self.frame_3.pack(fill='both', padx=10, pady=10, expand=True)
        """ Frame For Navigation """
        self.frame_4 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_4.pack(fill='both')
        # Navigation Buttons
        move_left = CTkButton(self.frame_4, text='<', font=(window_font, window_font_size), fg_color=color_scheme,
                              text_color=bright_colors[4], hover_color=color_scheme, command=lambda: self.move_pages("Left"))
        move_left.pack(side='left')
        self.tracker_label = CTkLabel(self.frame_4, text='', fg_color=color_scheme, text_color=bright_colors[5], font=(window_font, window_font_size))
        self.tracker_label.place(relx=0.45, rely=0.0)
        move_right = CTkButton(self.frame_4, text='>', font=(window_font, window_font_size), fg_color=color_scheme,
                               text_color=bright_colors[4], hover_color=color_scheme, command=lambda: self.move_pages("Right"))
        move_right.pack(side='right')
        """ Button For Next Window """
        self.k_mer_length = CTkButton(self.window, text="K-mer Length", font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2],
                                      command=self.next_window)
        self.k_mer_length.pack(side="bottom", fill='both', pady=10, expand=True, padx=10)
        self.window.mainloop()


    def move_pages(self, direction):

        """" Navigates Pages """

        if direction == "Left":
            if self.start >= (view_limit + 5):
                self.start -= (view_limit + 5)
                self.stop -= (view_limit + 5)
                try:
                    # Clean Frame
                    for widget_1 in self.frame_3.winfo_children():
                        widget_1.destroy()
                    # Redraw
                    self.show_k_mer(False)
                    self.tracker_label.configure(text_color=bright_colors[5])
                    self.tracker_label.configure(text=f"{(self.start // (view_limit + 5))+1}/{math.ceil(self.results_length/(view_limit + 5))}") if self.results_length >= 1 else 0
                except tkinter.TclError: return
        elif direction == "Right":
            if self.stop < self.results_length:
                self.start += (view_limit + 5)
                self.stop += (view_limit + 5)
                try:
                    # Clean Frame
                    for widget_2 in self.frame_3.winfo_children():
                        widget_2.destroy()
                    # Redraw
                    self.show_k_mer(False)
                    self.tracker_label.configure(text_color=bright_colors[5])
                    self.tracker_label.configure(text=f"{(self.start // (view_limit + 5))+1}/{math.ceil(self.results_length/(view_limit + 5))}") if self.results_length >= 1 else 0
                except tkinter.TclError: return


    def next_window(self):

        """ Next Window """

        try: self.window.destroy()
        except tkinter.TclError: return
        K_mer_Length(self.username, self.firstname, self.lastname, self.DNA_data, self.sequence_type, self.menu_window, self.signing_window)


    def set_reversed(self):

        """ Manage Reverse Complement """

        # Setting Values To None
        try:
            self.k_mer_count.configure(text="None,")
            # Clearing Frames
            for widget in self.frame_3.winfo_children():
                widget.destroy()
            # Reset Bounds And self.tracker_label
            self.start, self.stop = 0, (view_limit + 5)
            self.results_length = 0
            self.tracker_label.configure(text=f"")
        except tkinter.TclError:
            return
        if self.reverse_switch == 0:
            self.isReverse = "True"
            try: self.isReversed.configure(text="True")
            except tkinter.TclError: return
            self.reverse_switch = 1
            return
        elif self.reverse_switch == 1:
            self.isReverse = "False"
            try: self.isReversed.configure(text="False")
            except tkinter.TclError: return
            self.reverse_switch = 0
            return
        return


    def show_k_mer(self, isFrom_k_mer):

        """ Making And Showing K-mer """

        # Cleaning Frame
        try:
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        except tkinter.TclError:
            return
        if not str(self.read_index_entry.get()):
            # Setting Values To None
            try: self.k_mer_count.configure(text="None,")
            except tkinter.TclError: return
            # Error
            error_label_1 = CTkLabel(self.window, text="Empty Read Index", font=(window_font, window_font_size),
                                     fg_color=color_scheme, text_color=bright_colors[1])
            error_label_1.place(relx=0.4, rely=0.25)
            self.window.after(1000, error_label_1.destroy)
            return
        # List For Our Read Indexes
        result_k_mer_indexes = list()
        for key, value in self.DNA_data.items():
            if key == str(self.read_index_entry.get()):
                if self.isReverse == "True":
                    result_k_mer_indexes = k_mer_indexes(reverseComplement(str(value), self.sequence_type), self.sequence_type, str(self.k_mer_entry.get()).upper())
                elif self.isReverse == "False":
                    result_k_mer_indexes = k_mer_indexes(value, self.sequence_type, str(self.k_mer_entry.get()).upper())
                """ Checking For Errors """
                if result_k_mer_indexes == -2:
                    # Setting Values To None
                    try: self.k_mer_count.configure(text="None,")
                    except tkinter.TclError: return
                    # Error
                    error_label_1 = CTkLabel(self.window, text="Empty K-mer", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_1.place(relx=0.4, rely=0.25)
                    try: self.window.after(1000, error_label_1.destroy)
                    except tkinter.TclError: return
                    return
                elif result_k_mer_indexes == -1:
                    # Setting Values To None
                    try: self.k_mer_count.configure(text="None,")
                    except tkinter.TclError: return
                    # Error
                    error_label_2 = CTkLabel(self.window, text="Bad Seq Types", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_2.place(relx=0.4, rely=0.25)
                    try: self.window.after(1000, error_label_2.destroy)
                    except tkinter.TclError: return
                    return
                # If Input K-mer Is Greater Than The Sequence
                elif len(str(self.k_mer_entry.get())) > len(str(value)):
                    # Setting Values To None
                    try: self.k_mer_count.configure(text="None,")
                    except tkinter.TclError: return
                    # Error
                    error_label_3 = CTkLabel(self.window, text="Longer K-mer", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_3.place(relx=0.4, rely=0.25)
                    try: self.window.after(1000, error_label_3.destroy)
                    except tkinter.TclError: return
                    return
                # Set The self.result_length To result_k_mer_indexes
                self.results_length = len(result_k_mer_indexes)
                # Reset Bounds Whenever New Sequences Are Got
                if isFrom_k_mer:
                    self.start, self.stop = 0, (view_limit + 5)
                    self.tracker_label.configure(text=f"{(self.start // (view_limit + 5)) + 1}/{math.ceil(self.results_length / (view_limit + 5))}") if self.results_length >= 1 else 0
                """ No Errors Then Update Our K-mer Count And Frame """
                try: self.k_mer_count.configure(text=f"{len(result_k_mer_indexes)}," if len(result_k_mer_indexes) < number_threshold else f"{len(result_k_mer_indexes):,.2e},")
                except tkinter.TclError: return
                for i in result_k_mer_indexes[self.start:self.stop]:
                    CTkLabel(self.frame_3, text=f"{i+1}", font=(window_font, window_font_size), fg_color=color_scheme,
                             text_color=bright_colors[5], corner_radius=corner,
                             height=self.frame_3.winfo_height()).pack(side='left')
                return