from user_analysis.k_mer_search import *


class Hamming:

    def __init__(self, username, firstname, lastname, DNA_data, sequence_type, menu_window):

        # Useful Information
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.menu_window = menu_window
        self.DNA_data = DNA_data
        self.sequence_type = sequence_type
        # Helpful Variables
        self.reverse_switch = 0
        self.isReverse = "False"
        # Window
        self.window = Tk()
        self.window.config(bg=color_scheme)
        self.window.title("Hamming Distance")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.eval("tk::PlaceWindow . center")
        self.window.propagate(True)
        self.window.resizable(False, False)
        """ Showing Header """
        self.hamming_header = CTkLabel(self.window, text="Hamming Distance", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=text_color)
        self.hamming_header.pack(fill='both', side='top', pady=5, expand=True)
        """ Frame For seq_1 And seq_2 """
        self.frame_1 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_1.pack(fill='both', pady=100)
        """ Putting Stuff Inside Frame """
        self.seq_1_entry = CTkEntry(self.frame_1, placeholder_text="Seq 1 Read Index", placeholder_text_color=bright_colors[0],
                                    fg_color=color_scheme, text_color=bright_colors[5], border_width=border, border_color=bright_colors[2],
                                    height=50, width=350, font=(window_font, window_font_size))
        self.seq_1_entry.pack(side='left', padx=10, pady=10)
        self.seq_2_entry = CTkEntry(self.frame_1, placeholder_text="Seq 2 Read Index", placeholder_text_color=bright_colors[0],
                                    fg_color=color_scheme, text_color=bright_colors[5], border_width=border, border_color=bright_colors[2],
                                    height=50, width=350, font=(window_font, window_font_size))
        self.seq_2_entry.pack(side="right", padx=10, pady=10)
        """ Frame For Buttons """
        self.middle_frame = CTkFrame(self.window, fg_color=color_scheme)
        self.middle_frame.pack(fill='both')
        """ Button For Hamming Distance Call """
        self.ham_it = CTkButton(self.middle_frame, text="Ham It", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                corner_radius=corner, hover_color=bright_colors[2], height=50, command=lambda: self.show_hamming(DNA_data))
        self.ham_it.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        """ Button For Reverse Complement """
        self.reverse = CTkButton(self.middle_frame, text="Reverse", font=(window_font, window_font_size), fg_color=color_scheme,
                                text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2], height=50,
                                command= self.set_reverse)
        self.reverse.pack(side="right", fill='both', expand=True, padx=10, pady=10)
        """ Frame For Some Analysis """
        self.frame_2 = CTkFrame(self.window, fg_color=color_scheme, height=200)
        self.frame_2.pack(fill='both')
        """ Analysis Frame """
        self.frame_3 = CTkFrame(self.frame_2, fg_color=bright_colors[2], height=50)
        self.frame_3.pack(fill='both')
        """ Hamming Distance Label """
        self.hamming_distance_label = CTkLabel(self.frame_3, text="Hamming", font=(window_font, (window_font_size - 10)), fg_color=bright_colors[2],
                                         text_color=bright_colors[4], corner_radius=corner)
        self.hamming_distance_label.grid(row=0, column=0, sticky='w', padx=5, pady=10)
        """ Hamming Distance """
        self.hamming_distance = CTkLabel(self.frame_3, text="", font=(window_font, (window_font_size - 10)), fg_color=bright_colors[5],
                                         text_color=bright_colors[4], corner_radius=corner)
        self.hamming_distance.grid(row=0, column=1, padx=5, pady=10)
        """ Length Of Each Label """
        self.length_each_label = CTkLabel(self.frame_3, text="LengthOfEach", font=(window_font, (window_font_size - 10)), fg_color=bright_colors[2],
                                               text_color=bright_colors[4], corner_radius=corner)
        self.length_each_label.grid(row=0, column=2, padx=5, pady=10)
        """ Length Of Each """
        self.length_each = CTkLabel(self.frame_3, text="", font=(window_font, (window_font_size - 10)), fg_color=bright_colors[5], text_color=bright_colors[4],
                                    corner_radius=corner)
        self.length_each.grid(row=0, column=3, padx=5, pady=10)
        """ Intersection Label """
        self.intersection_label = CTkLabel(self.frame_3, text="Intersection", font=(window_font, (window_font_size - 10)),
                                               fg_color=bright_colors[2], text_color=bright_colors[4], corner_radius=corner)
        self.intersection_label.grid(row=0, column=4, padx=5, pady=10)
        """ Intersection """
        self.intersection = CTkLabel(self.frame_3, text="", font=(window_font, (window_font_size - 10)), fg_color=bright_colors[5], text_color=bright_colors[4],
                                     corner_radius=corner)
        self.intersection.grid(row=0, column=5, sticky='w', padx=5, pady=10)
        """ isReversed Label """
        self.isReversed_label = CTkLabel(self.frame_3, text="ReverseComplement",
                                           font=(window_font, (window_font_size - 10)),
                                           fg_color=bright_colors[2], text_color=bright_colors[4], corner_radius=corner)
        self.isReversed_label.grid(row=0, column=6, padx=5, pady=10)
        """ isReversed """
        self.isReversed = CTkLabel(self.frame_3, text=f"{self.isReverse}", font=(window_font, (window_font_size - 10)),
                                     fg_color=bright_colors[5], text_color=bright_colors[4],
                                     corner_radius=5)
        self.isReversed.grid(row=0, column=7, sticky='w', padx=5, pady=10)
        """ Frame For Visual Frames """
        self.frame_4 = CTkFrame(self.frame_2, fg_color=color_scheme)
        self.frame_4.pack(fill='both')
        """ Visualizing Hamming Distance """
        # Frame For seq_1 Visualization
        self.frame_5 = CTkScrollableFrame(self.frame_4, fg_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                          orientation=HORIZONTAL, scrollbar_button_color=bright_colors[3],
                                          scrollbar_button_hover_color=bright_colors[3])
        self.frame_5.pack(side="left", fill='both', expand=True, padx=1, pady=1)
        # Frame For seq_2 Visualization
        self.frame_6 = CTkScrollableFrame(self.frame_4, fg_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                          orientation=HORIZONTAL, scrollbar_button_color=bright_colors[3],
                                          scrollbar_button_hover_color=bright_colors[3])
        self.frame_6.pack(side='right', fill='both', expand=True, padx=1, pady=1)
        """ Bottom Buttons For Back To Codon Analysis And K_mer Analysis """
        self.back_to_codon = CTkButton(self.window, text="Menu", font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2], height=50,
                                       command=self.back_to_menu)
        self.back_to_codon.pack(fill="both", side="left", pady=50, padx=10)
        self.k_mer_analysis = CTkButton(self.window, text="K-mer Analysis", font=(window_font, window_font_size), fg_color=color_scheme,
                                        text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2], height=50,
                                        command=self.next_window)
        self.k_mer_analysis.pack(fill="both", side="right", pady=50, padx=10)
        self.window.mainloop()


    def next_window(self):

        """ Go To Next Window """
        self.window.destroy()
        K_mer_Analysis(self.username, self.firstname, self.lastname, self.DNA_data, self.sequence_type, self.menu_window)


    def back_to_menu(self):

        """ Back To The Menu """
        self.window.destroy()
        self.menu_window(self.username, self.firstname, self.lastname)


    def set_reverse(self):

        """ Managing Reverse Complement """
        # Setting Values To None
        self.hamming_distance.configure(text="None")
        self.intersection.configure(text="None")
        self.length_each.configure(text="None")
        # Clearing Frames
        for widget_1 in self.frame_5.winfo_children():
            widget_1.destroy()
        for widget_2 in self.frame_6.winfo_children():
            widget_2.destroy()
        # Checking Conditions
        if self.reverse_switch == 0:
            self.isReverse = "True"
            self.isReversed.configure(text='True')
            self.reverse_switch = 1
            return
        elif self.reverse_switch == 1:
            self.isReverse = "False"
            self.isReversed.configure(text='False')
            self.reverse_switch = 0
            return
        return


    def show_hamming(self, DNA_data):

        """ Showing Hamming Distance """
        # Cleaning The Screen
        for widget in self.frame_5.winfo_children():
            widget.destroy()
        for widget in self.frame_6.winfo_children():
            widget.destroy()
        # Temporary string Variables
        temp_seq_1 = str()
        temp_seq_2 = str()
        # Getting Sequences From Data
        for key, value in DNA_data.items():
            if key == str(self.seq_1_entry.get()):
                # After Getting The Data At Key
                # Is Our User Requesting For Reverse Complement
                if self.isReverse == "True":
                    temp_seq_1 += reverseComplement(str(value), self.sequence_type)
                elif self.isReverse == "False":
                    temp_seq_1 += str(value)
            elif key == str(self.seq_2_entry.get()):
                # After Getting The Data At Key
                # Is Our User Requesting For Reverse Complement
                if self.isReverse == "True":
                    temp_seq_2 += reverseComplement(str(value), self.sequence_type)
                elif self.isReverse == "False":
                    temp_seq_2 += str(value)
        # result Has The Hamming Distance
        result = n_distance(temp_seq_1, temp_seq_2)
        if result == -1 or result == -2:
            # Setting Values To None
            self.hamming_distance.configure(text="None")
            self.intersection.configure(text="None")
            self.length_each.configure(text="None")
            # Error
            self.error = CTkLabel(self.window, text="Sequence(s) Error", font=(window_font, window_font_size),
                                  fg_color=color_scheme, text_color="red")
            self.error.place(relx=0.4, rely=0.37)
            self.window.after(1000, self.error.destroy)
            return
        else:
            # Useful Variable For Updates
            hamming_count, intersection_count = 0, 0
            """ Showing The Strands For Visual Comparison"""
            for i in result:
                if i[1] != i[2]:
                    hamming_count += 1
                    CTkLabel(self.frame_5, text=f"{i[1]}\n{i[0]+1}", fg_color="white", text_color="black", height=self.frame_5.winfo_height(),
                             width=50, corner_radius=5, font=(window_font, window_font_size)).grid(row=0, column=i[0],
                                                                                              sticky='s', pady=1)
                    CTkLabel(self.frame_6, text=f"{i[2]}\n{i[0]+1}", fg_color="white", text_color="black", height=self.frame_6.winfo_height(),
                             width=50, corner_radius=5, font=(window_font, window_font_size)).grid(row=0, column=i[0],
                                                                                              sticky='s', pady=1)
                elif i[1] == i[2]:
                    intersection_count += 1
                    CTkLabel(self.frame_5, text=f"{i[1]}\n{i[0]+1}", fg_color="black", text_color="white", height=self.frame_5.winfo_height(),
                             width=50, corner_radius=5, font=(window_font, window_font_size)).grid(row=0, column=i[0],
                                                                                              sticky='s', pady=1)
                    CTkLabel(self.frame_6, text=f"{i[2]}\n{i[0]+1}", fg_color="black", text_color="white", height=self.frame_6.winfo_height(),
                             width=50, corner_radius=5, font=(window_font, window_font_size)).grid(row=0, column=i[0],
                                                                                              sticky='s', pady=1)
            # Updating Dormant Labels; Hamming Distance, Length Of Each, Intersection
            self.hamming_distance.configure(text=f"{hamming_count}|{round(((hamming_count/len(result)) * 100),1)}%")
            self.intersection.configure(text=f"{intersection_count}|{round(((intersection_count/len(result)) * 100),1)}%")
            # Since The Length Of Result Is The Length Of Each Strand
            self.length_each.configure(text=f"{len(result)}")