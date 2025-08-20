from user_analysis.k_mer_length import *


class K_mer_Analysis:

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
                                       height=50, command=self.show_k_mer)
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
        self.k_mer_count = CTkLabel(self.frame_2, text="None, ", fg_color=bright_colors[2],
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
        """ Button For Next Window """
        self.k_mer_length = CTkButton(self.window, text="K-mer Length", font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2],
                                      command=self.next_window)
        self.k_mer_length.pack(side="bottom", fill='both', pady=10, expand=True, padx=10)
        self.window.mainloop()


    def next_window(self):

        """ Next Window """
        self.window.destroy()
        K_mer_Length(self.username, self.firstname, self.lastname, self.DNA_data, self.sequence_type, self.menu_window)


    def set_reversed(self):

        """ Manage Reverse Complement """
        # Setting Values To None
        self.k_mer_count.configure(text="None, ")
        # Clearing Frames
        for widget in self.frame_3.winfo_children():
            widget.destroy()
        if self.reverse_switch == 0:
            self.isReverse = "True"
            self.isReversed.configure(text="True")
            self.reverse_switch = 1
            return
        elif self.reverse_switch == 1:
            self.isReverse = "False"
            self.isReversed.configure(text="False")
            self.reverse_switch = 0
            return
        return


    def show_k_mer(self):

        """ Making And Showing K-mer """

        # Cleaning Frame
        for widget in self.frame_3.winfo_children():
            widget.destroy()
        if not str(self.read_index_entry.get()):
            # Setting Values To None
            self.k_mer_count.configure(text="None, ")
            # Error
            error_label_1 = CTkLabel(self.window, text="Empty Read Index", font=(window_font, window_font_size),
                                     fg_color=color_scheme, text_color=bright_colors[1])
            error_label_1.place(relx=0.4, rely=0.25)
            self.window.after(1000, error_label_1.destroy)
            return
        # List For Our Read Indexes
        result_k_mer_indexes = list()
        for key, value in self.DNA_data.items():
            # Bug Review Here
            if key == str(self.read_index_entry.get()):
                if self.isReverse == "True":
                    result_k_mer_indexes = k_mer_indexes(reverseComplement(str(value), self.sequence_type), self.sequence_type, str(self.k_mer_entry.get()).upper())
                elif self.isReverse == "False":
                    result_k_mer_indexes = k_mer_indexes(value, self.sequence_type, str(self.k_mer_entry.get()).upper())
                """ Checking For Errors """
                if result_k_mer_indexes == -2:
                    # Setting Values To None
                    self.k_mer_count.configure(text="None, ")
                    # Error
                    error_label_1 = CTkLabel(self.window, text="Empty K-mer", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_1.place(relx=0.4, rely=0.25)
                    self.window.after(1000, error_label_1.destroy)
                    return
                elif result_k_mer_indexes == -1:
                    # Setting Values To None
                    self.k_mer_count.configure(text="None, ")
                    # Error
                    error_label_2 = CTkLabel(self.window, text="Bad Seq Types", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_2.place(relx=0.4, rely=0.25)
                    self.window.after(1000, error_label_2.destroy)
                    return
                # If Input K-mer Is Greater Than The Sequence
                elif len(str(self.k_mer_entry.get())) > len(str(value)):
                    # Setting Values To None
                    self.k_mer_count.configure(text="None, ")
                    # Error
                    error_label_3 = CTkLabel(self.window, text="Longer K-mer", font=(window_font, window_font_size),
                                             fg_color=color_scheme, text_color=bright_colors[1])
                    error_label_3.place(relx=0.4, rely=0.25)
                    self.window.after(1000, error_label_3.destroy)
                    return
                """ No Errors Then Update Our K-mer Count And Frame """
                self.k_mer_count.configure(text=f"{len(result_k_mer_indexes)},")
                for i in result_k_mer_indexes:
                    CTkLabel(self.frame_3, text=f"{i+1}", font=(window_font, window_font_size), fg_color=color_scheme,
                             text_color=bright_colors[5], corner_radius=corner,
                             height=self.frame_3.winfo_height()).pack(side='left')
                return