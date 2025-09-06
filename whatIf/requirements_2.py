import threading
import interface
from user_app.hamming import *


class Requirements_2:

    def __init__(self, username, firstname, lastname, DNA_data, filename, seq_type, menu_window):

        # Useful Variables
        self.DNA_data = DNA_data
        # Stores Read Index: [Frame, Protein(s)]
        self.key_and_proteins = dict()
        self.sequence_type = seq_type
        self.isReverseComplement = False
        self.current_frame = -1
        self.draw_proteins = False
        # Windows
        self.window = Tk()
        self.window.config(bg=color_scheme)
        self.window.title("Proteinsynthesis")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.eval("tk::PlaceWindow . center")
        self.window.propagate(True)
        self.window.resizable(False, False)
        # Calling Proteinsynthesis In Separate Thread
        self.window.after(100, self.start_thread)
        """ Heading """
        CTkLabel(self.window, text="Proteinsynthesis", font=(window_font, window_font_size), fg_color=color_scheme, text_color=text_color).pack(fill='both',pady=10)
        """ Frame For Read Index Entry, Search, Reverse """
        self.frame_1 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_1.pack(fill='both')
        """ Read Index Entry, Search, Reverse """
        self.read_index_entry = CTkEntry(self.frame_1, placeholder_text="Enter Read Index", placeholder_text_color=bright_colors[0],
                                         fg_color=color_scheme, text_color=bright_colors[5], border_width=border, border_color=bright_colors[2],
                                         height=50, width=400, font=(window_font, window_font_size))
        self.read_index_entry.grid(row=0, column=0, sticky='news', padx=15, pady=5)
        self.protein_search = CTkButton(self.frame_1, text="Search", fg_color=color_scheme, text_color=bright_colors[4],
                                        font=(window_font, window_font_size), hover_color=bright_colors[2], corner_radius=corner,
                                        height=50, width=300, command=self.show_proteins)
        self.protein_search.grid(row=0, column=1, sticky='news', pady=5)
        self.reverse = CTkButton(self.frame_1, text="Reverse", font=(window_font, window_font_size), fg_color=color_scheme,
                                 text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner, height=50, width=330,
                                 command=self.reverse_toggler)
        self.reverse.grid(row=0, column=2, sticky='news', padx=5, pady=5)
        """ Frame For Useful Information """
        self.frame_2 = CTkFrame(self.window, fg_color=bright_colors[2], height=50)
        self.frame_2.pack(fill='both', padx=15, pady=10)
        """ Top Information: Seq Type, Reverse Complement, Read Index, Frame, Filename """
        CTkLabel(self.frame_2, text="SeqType:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2], text_color=bright_colors[4]).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.seq_type_label = CTkLabel(self.frame_2, text=f"{seq_type},", fg_color=bright_colors[2], text_color=bright_colors[4],
                                       font=(window_font, (window_font_size - 15)))
        self.seq_type_label.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        CTkLabel(self.frame_2, text="ReverseComplement:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2], text_color=bright_colors[4]).grid(row=0, column=2, sticky='w', padx=5, pady=5)
        self.isReverse_label = CTkLabel(self.frame_2, text=f"{str(self.isReverseComplement)},", fg_color=bright_colors[2],
                                  text_color=bright_colors[4], font=(window_font, (window_font_size - 15)))
        self.isReverse_label.grid(row=0, column=3, sticky='w', padx=5, pady=5)
        CTkLabel(self.frame_2, text="ReadIndex:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2], text_color=bright_colors[4]).grid(row=0, column=4, sticky='w', padx=5, pady=5)
        self.read_index_label = CTkLabel(self.frame_2, text=f"None,", fg_color=bright_colors[2], text_color=bright_colors[4],
                                         font=(window_font, (window_font_size - 15)))
        self.read_index_label.grid(row=0, column=5, sticky='w', padx=5, pady=5)
        CTkLabel(self.frame_2, text="Frame:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2], text_color=bright_colors[4]).grid(row=0, column=6, sticky='w', padx=5, pady=5)
        self.open_reading_frame_label = CTkLabel(self.frame_2, text=f"None,", fg_color=bright_colors[2], text_color=bright_colors[4],
                                                 font=(window_font, (window_font_size - 15)))
        self.open_reading_frame_label.grid(row=0, column=7, sticky='w', padx=5, pady=5)
        CTkLabel(self.frame_2, text="Filename:", font=(window_font, (window_font_size - 15), font_style), fg_color=bright_colors[2], text_color=bright_colors[4]).grid(row=0, column=8, sticky='w', padx=5, pady=5)
        new_filename = filename[str(filename).rfind('/')+1:]
        self.filename_label = CTkLabel(self.frame_2, text=f"{str(new_filename)}" if len(str(new_filename)) <= string_threshold else f"{str(new_filename)[:10]}...",
                                       fg_color=bright_colors[2], text_color=bright_colors[4], font=(window_font, (window_font_size - 15)))
        self.filename_label.grid(row=0, column=9, sticky='w', padx=5, pady=5)
        """ Scrollable Frame For Protein Showcase """
        self.scroll_frame = CTkScrollableFrame(self.window, fg_color=bright_colors[3], scrollbar_fg_color=bright_colors[3],
                                               scrollbar_button_color=bright_colors[3], scrollbar_button_hover_color=bright_colors[3])
        self.scroll_frame.pack(fill='both', expand=True, padx=15)
        # A Tip Off On The Frame
        self.tip_off = CTkLabel(self.window, text_color=text_color, text="Tip: " + str(tips[4]),
                           fg_color=color_scheme, font=(window_font, (window_font_size - 10)))
        """ Button For Hamming Distance """
        self.hamming_distance = CTkButton(self.window, text="Hamming", font=(window_font, window_font_size), fg_color=color_scheme,
                                          text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner, height=50,
                                          command=lambda: self.ham_window(username, firstname, lastname, DNA_data, seq_type, menu_window))
        self.hamming_distance.pack(side='bottom', fill='both', padx=15, pady=10)
        self.window.mainloop()


    def ham_window(self, username, firstname, lastname, DNA_data, seq_type, menu_window):

        """ Calls Hamming Window """
        try: self.window.destroy()
        except tkinter.TclError: return
        Hamming(username, firstname, lastname, DNA_data, seq_type, menu_window)


    def reverse_toggler(self):

        """ Manages Reverse Button Requests """
        # A Tip On App Usage
        if interface.GUI_attr.tip_switch == 2:
            self.tip_off.pack(side='bottom', fill='both', padx=15, pady=10)
            self.window.after(5000, self.tip_off.destroy)
            interface.GUI_attr.tip_switch = 3
            return
        self.draw_proteins = True
        self.current_frame = (self.current_frame + 1) % 6
        if self.current_frame >= 3:
            self.isReverseComplement = True
            frame_num = self.current_frame - 3
            suffix = '-'
            try:
                self.isReverse_label.configure(text=f"{str(self.isReverseComplement)}")
                self.open_reading_frame_label.configure(text=f"{frame_num + 1}{suffix}")
            except tkinter.TclError: return
        else:
            self.isReverseComplement = False
            frame_num = self.current_frame
            suffix = '+'
            try:
                self.isReverse_label.configure(text=f"{str(self.isReverseComplement)}")
                self.open_reading_frame_label.configure(text=f"{frame_num + 1}{suffix}")
            except tkinter.TclError: return


    def start_thread(self):

        """ Start Proteinsynthesis Thread """
        protein_thread = threading.Thread(target=self.proteinsynthesis_thread, daemon=True)
        protein_thread.start()


    def proteinsynthesis_thread(self):

        """ Makes The Proteins And Updates The self.key_and_proteins With The Read Index: [Frame, Protein(s)] """
        # Getting The 6 Possible Reading Frames
        key_and_ORF = dict()
        for key, value in self.DNA_data.items():
            temp_ORF = gen_openReading_frames(str(value), self.sequence_type)
            if temp_ORF != -1 and temp_ORF != -2:
                key_and_ORF[key] = temp_ORF
        # Getting Major Proteins From The Generated 6 Possible Frames
        read_index_proteins = dict()
        for key, value in key_and_ORF.items():
            read_index_proteins[key] = list()
            for index, i in enumerate(value):
                temp_proteins = proteins_from_reference(i)
                if temp_proteins != -1:
                    index_and_proteins = f"{index}|{str(temp_proteins)}"
                    read_index_proteins[key].append(index_and_proteins)
        self.key_and_proteins = read_index_proteins


    def show_proteins(self):

        """ Draws Proteins On Screen """

        # If User Draws Without Frame Selected
        if not self.draw_proteins:
            return

        for key, value in self.key_and_proteins.items():
            if key == str(self.read_index_entry.get()):
                # Updating Label To Show User The Current Read Index
                try: self.read_index_label.configure(text=f"{str(key)[:2]}...," if len(str(key)) > string_threshold else f"{key},")
                except tkinter.TclError: return
                # Choose Open Reading Frame Choice From User
                target_frame = self.current_frame
                # Is Our Target Frame In Range
                if target_frame < 0 or target_frame > 5:
                    return
                # Clean The Frame
                if len(self.scroll_frame.winfo_children()) != 0:
                    try:
                        for widget in self.scroll_frame.winfo_children():
                            widget.destroy()
                    except tkinter.TclError: return
                # Finding Target Frame
                for i in value:
                    frame, proteins = str(i).split("|")
                    frame_num = int(frame)
                    if frame_num == target_frame:
                        if proteins == '[]' and not self.isReverseComplement:
                            CTkLabel(self.scroll_frame, text="No Protein(s)", font=(window_font, (window_font_size + 30), font_style), fg_color=bright_colors[3],
                                     text_color=color_scheme).pack(fill='both', padx=10, pady=10)
                            CTkLabel(self.scroll_frame, text=f"{self.DNA_data[key]}" if len(str(self.DNA_data[key])) < string_threshold else f"{self.DNA_data[key][0:10]}...{self.DNA_data[key][-1]}",
                                     fg_color=bright_colors[2], text_color=color_scheme, font=(window_font, (window_font_size + 30), font_style), corner_radius=corner).pack(fill='both', padx=10, pady=10)
                        elif proteins == '[]' and self.isReverseComplement:
                            temp_reversed_seq = reverseComplement(self.DNA_data[key], self.sequence_type)
                            if temp_reversed_seq != -1:
                                reversed_seq = temp_reversed_seq
                                CTkLabel(self.scroll_frame, text="No Protein(s)", font=(window_font, (window_font_size + 30), font_style), fg_color=bright_colors[3],
                                     text_color=color_scheme).pack(fill='both', padx=10, pady=10)
                                CTkLabel(self.scroll_frame, text=f"{reversed_seq}" if len(str(reversed_seq)) < string_threshold else f"{reversed_seq[0:10]}...{reversed_seq[-1]}",
                                     fg_color=bright_colors[2], text_color=color_scheme, font=(window_font, (window_font_size + 30), font_style), corner_radius=corner).pack(fill='both', padx=10, pady=10)
                        else:
                            # Iterate Through Proteins And Display A Codon By Codon Independently
                            color_counter = 0
                            row_counter, column_counter = 0, 0
                            index_counter = 0
                            for letter in proteins:
                                if letter == 'M' and proteins[index_counter - 1] == '\'':
                                    row_counter += 1
                                    column_counter = 0
                                    color_counter = (color_counter + 1) % len(colors_1)
                                if letter in DNA_Codons.values():
                                    letter_label = CTkLabel(self.scroll_frame, text=str(letter), font=(window_font, (window_font_size + 20)),
                                             fg_color=colors_1[color_counter], text_color="white", corner_radius=corner)
                                    letter_label.grid(row=row_counter, column=column_counter, sticky='w', padx=5, pady=5)
                                    column_counter += 1
                                    self.window.update_idletasks()
                                    if (((letter_label.winfo_width() * column_counter) + (10 * column_counter)) + 50) >= self.scroll_frame.winfo_width():
                                        row_counter += 1
                                        column_counter = 0
                                index_counter += 1
                        break
                return