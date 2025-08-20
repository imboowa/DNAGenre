from interface.GUI_attr import *
import threading
from DNAtoolkit.DNAtools import *
from interface.GUI_methods import *
import time
from user_app.hamming import Hamming
# Is Done

class Protein:

    def __init__(self, username, firstname, lastname, prev_window, DNA_data, seq_type, menu_window):

        # Information on User
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        # Useful
        self.menu_window = menu_window
        # Destroy prev_window
        prev_window.destroy()
        # Making A Dictionary To Store The Read Index: Frame, Proteins
        self.sane_DNA_data = dict()
        # Saving DNA_data For Future Use
        self.DNA_data = DNA_data
        # Saving seq_type
        self.sequence_type = str(seq_type)
        # Switch To Toggle Between Reverse Complement And Normal Complement
        self.reverse_normal_switch = 0
        # Start Of Window
        self.window = Tk()
        self.window.config(bg=color_scheme)
        self.window.title("Protein Analysis")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.eval('tk::PlaceWindow . center')
        self.window.propagate(True)
        self.window.resizable(False, False)
        # Calling Threads After Rendering The Window
        self.window.after(100, lambda: self.start_threads(DNA_data, seq_type))
        """ Making Variables For The Presentable Data """
        self.current_read_index = "None"
        self.isReverseComplement = "False"
        """ Showing Proteins Heading """
        self.proteins_heading = CTkLabel(self.window, text="Proteins", font=(window_font, window_font_size), fg_color=color_scheme, text_color=text_color)
        self.proteins_heading.pack(fill='both', expand=True, side='top')
        """ Frame For Top Information """
        self.frame_1 = CTkFrame(self.window, height=50, fg_color=bright_colors[2])
        self.frame_1.pack(fill='both', padx=10, pady=10)
        """ Top Information: Seq Type, Reverse Complement, Read Index, Time Execution """
        """ Seq Type """
        self.seq_type_label = CTkLabel(self.frame_1, text="SeqType:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2],
                                       text_color=bright_colors[4])
        self.seq_type_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.seq_type = CTkLabel(self.frame_1, text=f"{seq_type},", font=(window_font, (window_font_size - 15)), fg_color=bright_colors[2],
                                 text_color=bright_colors[4])
        self.seq_type.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        """ Reverse Complement """
        self.reverse_complement_label = CTkLabel(self.frame_1, text="ReverseComplement:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2],
                                                 text_color=bright_colors[4])
        self.reverse_complement_label.grid(row=0, column=2, sticky="w", padx=3, pady=5)
        self.reverse_complement = CTkLabel(self.frame_1, text=f"{self.isReverseComplement},", font=(window_font, (window_font_size - 15)), fg_color=bright_colors[2],
                                           text_color=bright_colors[4])
        self.reverse_complement.grid(row=0, column=3, sticky='w', padx=3, pady=5)
        """ Read Index """
        self.read_index_label = CTkLabel(self.frame_1, text="ReadIndex:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2],
                                         text_color=bright_colors[4])
        self.read_index_label.grid(row=0, column=4, sticky="w", padx=3, pady=5)
        self.read_index = CTkLabel(self.frame_1, text=f"{self.current_read_index},", font=(window_font, (window_font_size - 15)), fg_color=bright_colors[2],
                                   text_color=bright_colors[4])
        self.read_index.grid(row=0, column=5, sticky='w', padx=3, pady=5)
        """ Time Execution """
        self.time_execution_label = CTkLabel(self.frame_1, text="TimeOnProteinsynthesis:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2],
                                             text_color=bright_colors[4])
        self.time_execution_label.grid(row=0, column=6, sticky="w", padx=3, pady=5)
        self.time_execution = CTkLabel(self.frame_1, text=f"", font=(window_font, (window_font_size - 15)), fg_color=bright_colors[2],
                                       text_color=bright_colors[4])
        self.time_execution.grid(row=0, column=7, sticky='w', padx=3, pady=5)
        """ Frame For Protein Showcase """
        self.frame_2 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_2.pack(fill="both")
        """ Information: Frame And Proteins """
        """ Open Reading Frame 1 Label """
        self.reading_frame_1_label = CTkLabel(self.frame_2, text="Frame 1+", fg_color=color_scheme, text_color=bright_colors[5],
                                              font=(window_font, window_font_size))
        self.reading_frame_1_label.grid(row=0, column=0, sticky='w', padx=10, pady=50)
        """ Open Reading's Frame (1)"""
        self.reading_frame_1 = CTkScrollableFrame(self.frame_2, fg_color=bright_colors[3], width=self.window.winfo_width() - 200,
                                                  scrollbar_button_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                                  scrollbar_button_hover_color=bright_colors[3])
        self.reading_frame_1.grid(row=0, column=1, sticky='w', padx=1, pady=5)
        """ Open Reading Frame 2 """
        self.reading_frame_2_label = CTkLabel(self.frame_2, text="Frame 2+", fg_color=color_scheme, text_color=bright_colors[5],
                                              font=(window_font, window_font_size))
        self.reading_frame_2_label.grid(row=1, column=0, sticky='w', padx=10, pady=50)
        """ Open Reading's Frame (2)"""
        self.reading_frame_2 = CTkScrollableFrame(self.frame_2, fg_color=bright_colors[3], width=self.window.winfo_width() - 200,
                                                  scrollbar_button_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                                  scrollbar_button_hover_color=bright_colors[3])
        self.reading_frame_2.grid(row=1, column=1, sticky='w', padx=1, pady=5)
        """ Open Reading Frame 3 """
        self.reading_frame_3_label = CTkLabel(self.frame_2, text="Frame 3+", fg_color=color_scheme, text_color=bright_colors[5],
                                              font=(window_font, window_font_size))
        self.reading_frame_3_label.grid(row=2, column=0, sticky='w', padx=10, pady=50)
        """ Open Reading's Frame (3)"""
        self.reading_frame_3 = CTkScrollableFrame(self.frame_2, fg_color=bright_colors[3], width=self.window.winfo_width() - 200,
                                                  scrollbar_button_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                                  scrollbar_button_hover_color=bright_colors[3])
        self.reading_frame_3.grid(row=2, column=1, sticky='w', padx=1, pady=5)
        """ Entry For Read Index, Search, Reversing The Protein (Analyzing The Reverse Complement) """
        """ Frame For Bottom Stuff """
        self.frame_3 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_3.pack(fill='both', expand=True)
        """ Read Index Entry """
        self.read_index_entry = CTkEntry(self.frame_3, placeholder_text="Enter Read Index/\"hamming\"", placeholder_text_color=bright_colors[0],
                                         border_width=border, border_color=bright_colors[3], font=(window_font, window_font_size), text_color=bright_colors[5],
                                         fg_color=color_scheme, width=600)
        self.read_index_entry.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        """ Search Button """
        self.search_button = CTkButton(self.frame_3, text="Search", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                       corner_radius=corner, hover_color=bright_colors[2], command=lambda: self.draw_proteins(self.sane_DNA_data))
        self.search_button.grid(row=0, column=1, sticky='w', padx=50, pady=10)
        """ Reverse Button """
        self.reverse_button = CTkButton(self.frame_3, text="Reverse", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                        corner_radius=5, hover_color=bright_colors[2], command=self.set_isReverseComplement)
        self.reverse_button.grid(row=0, column=2, sticky='w', padx=0, pady=10)
        self.window.mainloop()


    def start_threads(self, DNA_data, seq_type):

        # Calling proteinsynthesis And timer In Parallel
        self.time_counter = 0
        self.isRunning = True
        # daemon - Die Once The Main Thread (tkinter GUI) Dies (closes)
        time_threader = threading.Thread(target=self.time_thread, daemon=True)
        time_threader.start()
        protein_threader = threading.Thread(target=self.proteinsynthesis_thread, args=(DNA_data, seq_type), daemon=True)
        protein_threader.start()


    def time_thread(self):

        """ Calculates Time Taken For Proteinsynthesis """
        while self.isRunning:
            weeks, days, hours, minutes, seconds = time_calculator(self.time_counter)
            self.time_counter += 1
            elapsed_time = f"{weeks}W:{days}D:{hours:02}H:{minutes:02}M:{seconds:02}S"
            if self.window.winfo_exists():
                self.window.after(0, lambda t=elapsed_time: self.time_execution.configure(text=t))
                time.sleep(1)


    def proteinsynthesis_thread(self, DNA_data, seq_type):

        """ Storing Read Index: Codons (Both Normal And Reverse Complement) """
        key_value_codons = dict()
        for key, value in DNA_data.items():
            temp_open_reading_frames = gen_openReading_frames(value, seq_type)
            if temp_open_reading_frames != -1 and temp_open_reading_frames != -2:
                key_value_codons[key] = temp_open_reading_frames
        """ Read Index: List Of Tuples (Index, Proteins) """
        read_index_proteins_dict = dict()
        for key, value in key_value_codons.items():
            read_index_proteins_dict[key] = list()
            for index, (i) in enumerate(value):
                temp_proteins = proteins_from_reference(i)
                if temp_proteins != -1:
                    index_and_proteins = f"{index}|{str(temp_proteins)}"
                    read_index_proteins_dict[key].append(index_and_proteins)
        self.isRunning = False
        self.sane_DNA_data = read_index_proteins_dict


    def set_isReverseComplement(self):

        """ Toggles Between 0 And 1 For self.isReverseComplement """
        if self.reverse_normal_switch == 0:
            self.isReverseComplement = "True"
            self.reading_frame_1_label.configure(text='Frame 1-', text_color='green')
            self.reading_frame_2_label.configure(text='Frame 2-', text_color='green')
            self.reading_frame_3_label.configure(text='Frame 3-', text_color='green')
            self.reverse_complement.configure(text='True,')
            for widget_4 in self.reading_frame_1.winfo_children():
                widget_4.destroy()
            for widget_5 in self.reading_frame_2.winfo_children():
                widget_5.destroy()
            for widget_6 in self.reading_frame_3.winfo_children():
                widget_6.destroy()
            self.reverse_normal_switch = 1
            return
        elif self.reverse_normal_switch == 1:
            self.isReverseComplement = "False"
            self.reading_frame_1_label.configure(text='Frame 1+', text_color='lightgreen')
            self.reading_frame_2_label.configure(text='Frame 2+', text_color='lightgreen')
            self.reading_frame_3_label.configure(text='Frame 3+', text_color='lightgreen')
            self.reverse_complement.configure(text="False,")
            for widget_1 in self.reading_frame_1.winfo_children():
                widget_1.destroy()
            for widget_2 in self.reading_frame_2.winfo_children():
                widget_2.destroy()
            for widget_3 in self.reading_frame_3.winfo_children():
                widget_3.destroy()
            self.reverse_normal_switch = 0
            return
        return


    def draw_proteins(self, sane_DNA_data):

        """ Draw Proteins Or No-Protein Sequence On Screen """
        if str(self.read_index_entry.get()).lower() == "hamming":
            # Destroy Window
            self.window.destroy()
            # Calling Hamming Distance Window
            Hamming(self.username, self.firstname, self.lastname, self.DNA_data, self.sequence_type, self.menu_window)
            return
        for key, value in sane_DNA_data.items():
            if key == str(self.read_index_entry.get()):
                self.read_index.configure(text=str(key)+"," if len(str(key)) < 5 else f"{str(key)[:2]}...,")
                # Used For Reverse Complement
                temp_reversed_complement = reverseComplement(self.DNA_data[key], self.sequence_type)
                if temp_reversed_complement != -1:
                    self.desired_reverse_seq = temp_reversed_complement
                for i in value:
                    # Separating Frame From Protein(s)
                    frame, proteins = i.split("|")
                    if int(frame) == 0 and self.isReverseComplement == "False":
                        for widget_1 in self.reading_frame_1.winfo_children():
                            widget_1.destroy()
                        if proteins == '[]':
                            self.label_1 = CTkLabel(self.reading_frame_1, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                     fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_1.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_2 = CTkLabel(self.reading_frame_1, text=f"{self.DNA_data[key][0:10]}...{self.DNA_data[key][-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.DNA_data[key]}",
                                     font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=corner)
                            self.label_2.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_1 = 3
                            color_1 = colors_1[color_counter_1]
                            row_counter_1, col_counter_1 = 0, 0
                            i_1 = 0
                            for letter_1 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_1 == "M" and proteins[i_1 - 1] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_1 = colors_1[color_counter_1]
                                    if color_counter_1 == 0:
                                        color_counter_1 = 3
                                    color_counter_1 -= 1
                                    row_counter_1 += 1
                                    col_counter_1 = 0
                                if letter_1 in DNA_Codons.values():
                                    letter_label_1 = CTkLabel(self.reading_frame_1, text=str(letter_1), font=(window_font, (window_font_size + 20)),
                                                            fg_color=color_1, text_color="white", corner_radius=corner)
                                    letter_label_1.grid(row=row_counter_1, column=col_counter_1, sticky='w', padx=5, pady=5)
                                    col_counter_1 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_1.winfo_width() * col_counter_1) + (10 * col_counter_1)) + 20) >= self.reading_frame_1.winfo_width():
                                        row_counter_1 += 1
                                        col_counter_1 = 0
                                i_1 += 1
                    elif int(frame) == 1 and self.isReverseComplement == "False":
                        for widget_2 in self.reading_frame_2.winfo_children():
                            widget_2.destroy()
                        if proteins == '[]':
                            self.label_3 = CTkLabel(self.reading_frame_2, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                     fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_3.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_4 = CTkLabel(self.reading_frame_2, text=f"{self.DNA_data[key][0:10]}...{self.DNA_data[key][-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.DNA_data[key]}",
                                     font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=corner)
                            self.label_4.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_2 = 3
                            color_2 = colors_2[color_counter_2]
                            row_counter_2, col_counter_2 = 0, 0
                            i_2 = 0
                            for letter_2 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_2 == "M" and proteins[i_2] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_2 = colors_2[color_counter_2]
                                    if color_counter_2 == 0:
                                        color_counter_2 = 3
                                    color_counter_2 -= 1
                                    row_counter_2 += 1
                                    col_counter_2 = 0
                                if letter_2 in DNA_Codons.values():
                                    letter_label_2 = CTkLabel(self.reading_frame_2, text=str(letter_2), font=(window_font, (window_font_size + 20)),
                                                            fg_color=color_2, text_color="white", corner_radius=corner)
                                    letter_label_2.grid(row=row_counter_2, column=col_counter_2, sticky='w', padx=5, pady=5)
                                    col_counter_2 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_2.winfo_width() * col_counter_2) + (10 * col_counter_2)) + 20) >= self.reading_frame_2.winfo_width():
                                        row_counter_2 += 1
                                        col_counter_2 = 0
                                i_2 += 1
                    elif int(frame) == 2 and self.isReverseComplement == "False":
                        for widget_3 in self.reading_frame_3.winfo_children():
                            widget_3.destroy()
                        if proteins == '[]':
                            self.label_5 = CTkLabel(self.reading_frame_3, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                     fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_5.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_6 = CTkLabel(self.reading_frame_3, text=f"{self.DNA_data[key][0:10]}...{self.DNA_data[key][-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.DNA_data[key]}",
                                     font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=5)
                            self.label_6.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_3 = 3
                            color_3 = colors_3[color_counter_3]
                            row_counter_3, col_counter_3 = 0, 0
                            i_3 = 0
                            for letter_3 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_3 == "M" and proteins[i_3 - 1] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_3 = colors_3[color_counter_3]
                                    if color_counter_3 == 0:
                                        color_counter_3 = 3
                                    color_counter_3 -= 1
                                    row_counter_3 += 1
                                    col_counter_3 = 0
                                if letter_3 in DNA_Codons.values():
                                    letter_label_3 = CTkLabel(self.reading_frame_3, text=str(letter_3), font=(window_font, (window_font_size + 20)),
                                                            fg_color=color_3, text_color="white", corner_radius=corner)
                                    letter_label_3.grid(row=row_counter_3, column=col_counter_3, sticky='w', padx=5, pady=5)
                                    col_counter_3 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_3.winfo_width() * col_counter_3) + (10 * col_counter_3)) + 20) >= self.reading_frame_3.winfo_width():
                                        row_counter_3 += 1
                                        col_counter_3 = 0
                                i_3 += 1
                    elif int(frame) == 3 and self.isReverseComplement == "True":
                        # Clear The Frame For New Stuff
                        for widget_4 in self.reading_frame_1.winfo_children():
                            widget_4.destroy()
                        if proteins == '[]':
                            self.label_7 = CTkLabel(self.reading_frame_1, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                                    fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_7.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_8 = CTkLabel(self.reading_frame_1,
                                                    text=f"{self.desired_reverse_seq[0:10]}"
                                                         f"...{self.desired_reverse_seq[-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.desired_reverse_seq}",
                                                    font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=corner)
                            self.label_8.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_4 = 3
                            color_1 = colors_1[color_counter_4]
                            row_counter_4, col_counter_4 = 0, 0
                            i_4 = 0
                            for letter_4 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_4 == "M" and proteins[i_4 - 1] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_1 = colors_1[color_counter_4]
                                    if color_counter_4 == 0:
                                        color_counter_4 = 3
                                    color_counter_4 -= 1
                                    row_counter_4 += 1
                                    col_counter_4 = 0
                                if letter_4 in DNA_Codons.values():
                                    letter_label_4 = CTkLabel(self.reading_frame_1, text=str(letter_4),
                                                              font=(window_font, (window_font_size + 20)),
                                                              fg_color=color_1, text_color="white", corner_radius=corner)
                                    letter_label_4.grid(row=row_counter_4, column=col_counter_4, sticky='w', padx=5,
                                                        pady=5)
                                    col_counter_4 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_4.winfo_width() * col_counter_4) + (
                                            10 * col_counter_4)) + 20) >= self.reading_frame_1.winfo_width():
                                        row_counter_4 += 1
                                        col_counter_4 = 0
                                i_4 += 1
                    elif int(frame) == 4 and self.isReverseComplement == "True":
                        # Clear The Frame For New Stuff
                        for widget_5 in self.reading_frame_2.winfo_children():
                            widget_5.destroy()
                        if proteins == '[]':
                            self.label_9 = CTkLabel(self.reading_frame_2, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                                    fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_9.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_10= CTkLabel(self.reading_frame_2,
                                                    text=f"{self.desired_reverse_seq[0:10]}"
                                                         f"...{self.desired_reverse_seq[-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.desired_reverse_seq}",
                                                    font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=corner)
                            self.label_10.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_5 = 3
                            color_2 = colors_2[color_counter_5]
                            row_counter_5, col_counter_5 = 0, 0
                            i_5 = 0
                            for letter_5 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_5 == "M" and proteins[i_5 - 1] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_2 = colors_2[color_counter_5]
                                    if color_counter_5 == 0:
                                        color_counter_5 = 3
                                    color_counter_5 -= 1
                                    row_counter_5 += 1
                                    col_counter_5 = 0
                                if letter_5 in DNA_Codons.values():
                                    letter_label_5 = CTkLabel(self.reading_frame_2, text=str(letter_5),
                                                              font=(window_font, (window_font_size + 20)),
                                                              fg_color=color_2, text_color="white", corner_radius=corner)
                                    letter_label_5.grid(row=row_counter_5, column=col_counter_5, sticky='w', padx=5,
                                                        pady=5)
                                    col_counter_5 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_5.winfo_width() * col_counter_5) + (
                                            10 * col_counter_5)) + 20) >= self.reading_frame_3.winfo_width():
                                        row_counter_5 += 1
                                        col_counter_5 = 0
                                i_5 += 1
                    elif int(frame) == 5 and self.isReverseComplement == "True":
                        # Clear The Frame For New Stuff
                        for widget_6 in self.reading_frame_3.winfo_children():
                            widget_6.destroy()
                        if proteins == '[]':
                            self.label_11 = CTkLabel(self.reading_frame_3, text="No Protein(s)", font=(window_font, (window_font_size + 20)),
                                                    fg_color=bright_colors[3], text_color=color_scheme)
                            self.label_11.grid(row=0, column=0, sticky='w', padx=5, pady=5)
                            self.label_12 = CTkLabel(self.reading_frame_3,
                                                    text=f"{self.desired_reverse_seq[0:10]}"
                                                         f"...{self.desired_reverse_seq[-1]}"
                                                    if len(self.DNA_data[key]) > 10 else f"{self.desired_reverse_seq}",
                                                    font=(window_font, (window_font_size + 20)), fg_color=bright_colors[2], text_color=color_scheme,
                                                     corner_radius=corner)
                            self.label_12.grid(row=1, column=0, sticky='w', padx=5, pady=5)
                        else:
                            # Helpful Variables
                            color_counter_6 = 3
                            color_3 = colors_3[color_counter_6]
                            row_counter_6, col_counter_6 = 0, 0
                            i_6 = 0
                            for letter_6 in proteins:
                                # We Want Proteins That Are From 'M' Codon To '_' Stop Codon (No Duplicates In Showcase)
                                if letter_6 == "M" and proteins[i_6 - 1] == '\'':
                                    # No Using random Module Because It Can Generate The Same Color
                                    color_3 = colors_3[color_counter_6]
                                    if color_counter_6 == 0:
                                        color_counter_6 = 3
                                    color_counter_6 -= 1
                                    row_counter_6 += 1
                                    col_counter_6 = 0
                                if letter_6 in DNA_Codons.values():
                                    letter_label_6 = CTkLabel(self.reading_frame_3, text=str(letter_6),
                                                              font=(window_font, (window_font_size + 20)),
                                                              fg_color=color_3, text_color="white", corner_radius=corner)
                                    letter_label_6.grid(row=row_counter_6, column=col_counter_6, sticky='w', padx=5,
                                                        pady=5)
                                    col_counter_6 += 1
                                    self.window.update_idletasks()
                                    # Putting Codon Labels To New Line When At Edge Of Frame
                                    if (((letter_label_6.winfo_width() * col_counter_6) + (
                                            10 * col_counter_6)) + 20) >= self.reading_frame_3.winfo_width():
                                        row_counter_6 += 1
                                        col_counter_6 = 0
                                i_6 += 1
                return