import tkinter
from tkinter import *
from customtkinter import *
from DNAtoolkit.structures import *
from interface.GUI_attr import *
from pathlib import Path



class MeloPress:

    """ Compression And Decompression Page """

    def __init__(self, username, firstname, lastname, filename, previous_window, back_window, signing_window):

        """ Making Window """

        previous_window.destroy()

        self.window = Tk()
        self.window.title("MeloPress")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.config(bg=f"{color_scheme}")
        self.window.eval("tk::PlaceWindow . center")
        self.window.resizable(False, False)
        # Useful Variables
        self.back_window = back_window
        self.file_content = None
        """ Mother Frame For Filename, File Bytes, State, Is Seq Type """
        frame_1 = CTkFrame(self.window, fg_color=bright_colors[2])
        frame_1.pack(fill="both", pady=10, padx=10)
        # Filename Label
        filename_label = CTkLabel(frame_1, text=f"FileName:", font=(window_font, window_font_size - 10, font_style), fg_color=bright_colors[2],
                                  text_color=bright_colors[4])
        filename_label.grid(row=0, column=0, padx=10, pady=10)
        new_filename = str(filename)[str(filename).rfind('/')+1:]
        filename_label_value = CTkLabel(frame_1, text=f"{new_filename[:string_threshold]}..." if len(new_filename) > string_threshold else f"{new_filename}", font=(window_font, window_font_size - 10),
                                        fg_color=bright_colors[2], text_color=bright_colors[4])
        filename_label_value.grid(row=0, column=1, sticky="w")
        # File Bytes Label
        try: filebytes = os.path.getsize(Path(filename))
        except OSError: filebytes = "Unobtained"
        except Exception: filebytes = "Unobtained"
        filebytes_label = CTkLabel(frame_1, text=f"FileBytes:", font=(window_font, window_font_size - 10, font_style),
                                   fg_color=bright_colors[2], text_color=bright_colors[4])
        filebytes_label.grid(row=0, column=3, padx=10, pady=10)
        filebytes_label_value = CTkLabel(frame_1, text=f"{str(filebytes)[:string_threshold]}..." if len(str(filebytes)) > string_threshold else f"{str(filebytes)}", font=(window_font, window_font_size - 10), fg_color=bright_colors[2],
                                         text_color=bright_colors[4])
        filebytes_label_value.grid(row=0, column=4, sticky="w")
        # State Label--Compressed Or Decompressed
        state_label = CTkLabel(frame_1, text=f"State:", font=(window_font, window_font_size - 10, font_style),
                                   fg_color=bright_colors[2], text_color=bright_colors[4])
        state_label.grid(row=0, column=5, padx=10, pady=10)
        self.state_label_value = CTkLabel(frame_1, text=f"Unavailable", font=(window_font, window_font_size - 10), fg_color=bright_colors[2],
                                         text_color=bright_colors[4])
        self.state_label_value.grid(row=0, column=6, sticky="w")
        # Sequence Type
        seq_type_label = CTkLabel(frame_1, text=f"SequenceType:", font=(window_font, window_font_size - 10, font_style),
                                  fg_color=bright_colors[2], text_color=bright_colors[4])
        seq_type_label.grid(row=0, column=7, padx=10, pady=10)
        self.seq_type_label_value = CTkLabel(frame_1, text="Unavailable", font=(window_font, window_font_size - 10), fg_color=bright_colors[2],
                                        text_color=bright_colors[4])
        self.seq_type_label_value.grid(row=0, column=8, sticky="w")
        """ Mother Frame For Compress And Decompress Buttons """
        frame_2 = CTkFrame(self.window, fg_color=color_scheme)
        frame_2.pack(fill="both", pady=10, padx=10)
        # Compress Button
        compress_button = CTkButton(frame_2, text="Compress", font=(window_font, window_font_size), fg_color=color_scheme,
                                    text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                    command=lambda: self.start_compression(filename, frame_2))
        compress_button.pack(side="left", padx=10)
        # Decompress Button
        decompress_button = CTkButton(frame_2, text="Decompress", font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                      command=lambda: self.start_decompression(filename, frame_2))
        decompress_button.pack(side="right", padx=10)
        """ Mother Frame For File Content """
        frame_3 = CTkFrame(self.window, fg_color="whitesmoke")
        frame_3.pack(fill="both", expand=True, pady=10, padx=10)
        # File Content Label
        self.text_box = CTkTextbox(frame_3, fg_color="whitesmoke", text_color="black", border_color=color_scheme, border_width=border,
                            font=(window_font, window_font_size - 10), corner_radius=0)
        self.text_box.pack(fill="both", expand=True)
        """ Button For Menu And Make DNAGenre """
        menu_button = CTkButton(self.window, text="Menu", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=bright_colors[2], corner_radius=corner, font=(window_font, window_font_size),
                                command=lambda: self.call_menu_window(username, firstname, lastname, signing_window))
        menu_button.pack(side="left", pady=10, padx=10)
        make_DNAGenre = CTkButton(self.window, text="Make DNAGenre", fg_color=color_scheme, text_color=bright_colors[4],
                                  hover_color=bright_colors[2], corner_radius=corner, font=(window_font, window_font_size),
                                  command=lambda: self.handle_file_formating(filename, frame_2))
        make_DNAGenre.pack(side="right", padx=10, pady=10)
        self.window.after_idle(lambda: self.update_file_content(filename, self.text_box))
        self.window.after_idle(lambda: self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}"))
        self.window.after_idle(lambda: self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}"))
        self.window.mainloop()


    @staticmethod
    def get_state_header_info(filename):

        """ Returns File State In File Header """

        # Open The File
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return "Unobtained"
        except Exception:
            return "Unobtained"

        # Check Magic Bytes
        magic_bytes = file_data[0:3]
        if magic_bytes != b"#H9":
            return "Unavailable"

        # Get File State In File Header Information
        byte_2 = file_data[3]
        header = f"{byte_2:08b}"

        # Is This Our Kind Of File - .fgh
        if header[-3] != "1":
            return "Unavailable"

        file_state = "Compressed" if header[-2] == "1" else "Uncompressed"
        return file_state


    def get_seq_type_header_info(self, filename):

        """ Returns File Sequence Type In File Header """

        # Only Show Seq Type For Compression Files
        if self.get_state_header_info(filename) == "Uncompressed":
            return "Unavailable"

        # Open The File
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return "Unobtained"
        except Exception:
            return "Unobtained"

        # Check Magic Bytes
        magic_bytes = file_data[0:3]
        if magic_bytes != b"#H9":
            return "Unavailable"

        # Get File Sequence type In File Header Information
        byte_1 = file_data[3]
        header = f"{byte_1:08b}"

        # Is This Our Kind Of File - .fgh
        if header[-3] != "1":
            return "Unavailable"

        if header[-1] == "0":
            file_sequence_type = "DNA"
        elif header[-1] == "1":
            file_sequence_type = "RNA"
        else:
            file_sequence_type = "Unavailable"
        return file_sequence_type


    def update_file_content(self, filename, text_box: CTkTextbox):

        """ Returns File Content """

        text_box.configure(state="normal")
        text_box.delete("1.0", END)

        try:
            with open(filename, "rb") as file:
                self.file_content = file.read()
                text_box.insert("1.0", self.file_content)
        except FileNotFoundError:
            text_box.insert("1.0", "")
        except Exception:
            text_box.insert("1.0", "")

        text_box.configure(state="disabled")


    def call_menu_window(self, username, firstname, lastname, signing_window):

        """ Calls Menu Window """

        self.window.destroy()
        self.back_window(username, firstname, lastname, signing_window)


    def handle_file_formating(self, filename, frame: CTkFrame):

        """ Receives Errors From Formatting File For DNAGenre Style """

        if self.format_for_DNAGenre(filename) == 0:
            label_1 = CTkLabel(frame, text="Successful F", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)

            self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}")
            self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}")
            self.update_file_content(filename, self.text_box)

            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        else:
            label_1 = CTkLabel(frame, text="Error Formating", text_color=bright_colors[1], fg_color=color_scheme,font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return


    @staticmethod
    def format_for_DNAGenre(filename):

        """ Formats File--Decompressed File--To Be Compatible With DNAGenre Format """

        # Open
        try:
            with open(filename, "r") as file:
                file_data = file.read()
        except FileNotFoundError:
            return None
        except Exception:
            return None

        # Format
        new_file_data = file_data.splitlines()
        result = str()
        counter_1 = 1
        for line in new_file_data:
            if line.strip().startswith('@'):
                result += f"{line.strip()}_{counter_1}\n"
                counter_1 += 1
            else:
                for char in line:
                    if char in VALID_NUCLEOTIDES:
                        result += char
                result += "\n"

        # Update File-Decompressed File--To DNAGenre Style
        try:
            with open(filename, "w") as file:
                file.write(result)
        except Exception:
            return None

        return 0


    @staticmethod
    def prepare_data_compression(filename):

        """ Prepare File Data For Compression """

        # Open File
        try:
            with open(filename, "rb") as file:
                file_data = file.read().decode("utf-8")
        except FileNotFoundError:
            return "Unobtained"
        except Exception:
            return "Unobtained"

        # Arrange Data
        result = list()
        # Special Character
        special_char = '@'
        temp_sequence_1 = str()
        # Arrange Data
        new_file_data = file_data.splitlines()
        for line in new_file_data:
            counter_1 = 0
            current_line_data = ""
            line = line.strip()
            while counter_1 < len(line):
                if temp_sequence_1 and line[counter_1] not in VALID_NUCLEOTIDES:
                    result.append([special_char, temp_sequence_1])
                    temp_sequence_1 = ""
                elif line[counter_1] in VALID_NUCLEOTIDES:
                    current_line_data += line[counter_1]
                counter_1 += 1
            temp_sequence_1 += current_line_data
        # Save Last Sequence
        if temp_sequence_1:
            result.append([special_char, temp_sequence_1])

        # Format Data
        incident_1 = "TAAA"
        special_char = '@'
        new_result = list()
        for pair in result:
            counter_2 = 0
            is_incident_1 = False
            while counter_2 < len(pair[1]):
                temp_sequence_2 = pair[1][counter_2:counter_2 + 4]
                if temp_sequence_2 == incident_1 and counter_2 + 4 >= len(pair[1]):
                    temp_edit = pair[1] + special_char
                    new_result.append([special_char, temp_edit])
                    is_incident_1 = True
                counter_2 += 4
            if not is_incident_1:
                new_result.append([special_char, pair[1]])

        return new_result


    def start_compression(self, filename, frame: CTkFrame):

        """ Prepares Compression And Results """

        value = self.compress(filename)
        if value == 0:
            label_1 = CTkLabel(frame, text="Success C", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 1:
            label_1 = CTkLabel(frame, text="DNA & RNA", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 2:
            label_1 = CTkLabel(frame, text="Invalid Chars", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 3:
            label_1 = CTkLabel(frame, text="Improper Length", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 4:
            label_1 = CTkLabel(frame, text="Already C", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        else:
            label_1 = CTkLabel(frame, text="Unsuccessful C", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return


    def start_decompression(self, filename, frame: CTkFrame):

        """ Prepares Decompression And Results """

        value = self.decompress(filename)
        if value == 0:
            label_1 = CTkLabel(frame, text="Success D", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 1:
            label_1 = CTkLabel(frame, text="Not Compressed", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        elif value == 2:
            label_1 = CTkLabel(frame, text="Bad File Header", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return
        else:
            label_1 = CTkLabel(frame, text="Unsuccessful D", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            label_1.place(relx=0.44, rely=0.05)
            try: self.window.after(1000, label_1.destroy)
            except tkinter.TclError: return


    def compress(self, filename):

        """ Compresses Data In File And Writes To A New File """

        # Did We Already Compress This File
        if self.get_state_header_info(filename) == "Compressed":
            return 4

        # Get Prepared Data
        data = str()
        result = self.prepare_data_compression(filename)
        for pair in result:
            try:
                data += pair[0] + '\n' + pair[1] + '\n'
            except IndexError:
                return None
            except Exception:
                return None
        # Remove Last NewLine
        data = data.strip()

        # Counter For Every 4 Bits
        count_1 = 0
        # Byte Packed Into
        packing_byte = 0
        # Overall Counter
        counter_1 = 0
        # Last Bytes Are Indivisible By 4
        last_bytes_indivisibility = 0
        # output buffer
        output = bytearray()
        is_RNA = None

        data = bytearray(data, "utf-8")
        total_length = len(data)

        while counter_1 < total_length:
            byte = data[counter_1]
            match chr(byte):
                case 'A':
                    last_bytes_indivisibility = 0
                    packing_byte = (packing_byte << 2) | 0b00
                    count_1 += 1
                    counter_1 += 1
                case 'T':
                    last_bytes_indivisibility = 0
                    if is_RNA is True:
                        # File Contains RNA And DNA
                        return 1
                    is_RNA = False
                    packing_byte = (packing_byte << 2) | 0b01
                    count_1 += 1
                    counter_1 += 1
                case 'C':
                    last_bytes_indivisibility = 0
                    packing_byte = (packing_byte << 2) | 0b10
                    count_1 += 1
                    counter_1 += 1
                case 'G':
                    last_bytes_indivisibility = 0
                    packing_byte = (packing_byte << 2) | 0b11
                    count_1 += 1
                    counter_1 += 1
                case 'U':
                    last_bytes_indivisibility = 0
                    if is_RNA is False:
                        # File Contains RNA And DNA
                        return 1
                    is_RNA = True
                    packing_byte = (packing_byte << 2) | 0b01
                    count_1 += 1
                    counter_1 += 1
                case '@':
                    if count_1 != 0:
                        # Indivisibility In File Length
                        return 3
                    last_bytes_indivisibility = 1
                    output.append(byte)
                    count_1, packing_byte = 0, 0
                    counter_1 += 1
                case '\n':
                    if count_1 != 0:
                        # Indivisibility In File Length
                        return 3
                    output.append(byte)
                    count_1, packing_byte = 0, 0
                    counter_1 += 1
                case _:
                    # File Contains Invalid Characters
                    return 2
            if count_1 == 4:
                last_bytes_indivisibility = 1
                output.append(packing_byte)
                count_1, packing_byte = 0, 0

        # Magic Prefix - #H9
        magic_prefix_1, magic_prefix_2, magic_prefix_3 = 0b00100011, 0b01001000, 0b00111001

        # Prepare Header Include A Bit That Shows That This Is Our File - .fgh
        header = 0b111 if is_RNA else 0b110

        # Was This File Length Divisible By 4
        if count_1 != 0: return 3
        if last_bytes_indivisibility == 0: return 3

        # Write To That A New Kind Of File
        just_filename = str(filename)[str(filename).rfind('/'):str(filename).rfind('.')]
        new_filename =  str(filename)[:str(filename).rfind('/')] + just_filename + ".fgh"
        try:
            with open(new_filename, "wb") as file:
                file.write(bytes([magic_prefix_1, magic_prefix_2, magic_prefix_3]))
                file.write(bytes([header]))
                file.write(output)
        except Exception:
            return None

        # Show User Results
        self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}")
        self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}")
        
        return 0


    def decompress(self, filename):

        """ Decompresses Data In File And Writes To A New File """

        # File Must Be Compressed
        if self.get_state_header_info(filename) != "Compressed":
            return 1

        # Open File
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return None
        except Exception:
            return None

        file_magic = file_data[:3]
        sequence_type_byte = f"{file_data[3]:08b}"
        # Improper File Header
        if file_magic != b"#H9":
            return 2
        if sequence_type_byte[-1] == "0":
            seq_type = "DNA"
        elif sequence_type_byte[-1] == "1":
            seq_type = "RNA"
        else:
            return 2

        output = bytearray()

        counter_1 = 4
        special_character = ord('@')
        newline_character = ord('\n')
        while counter_1 < len(file_data):
            byte = file_data[counter_1]
            count_1 = 0
            if byte == special_character:
                # Check Forward
                counter_1 += 1
                if counter_1 >= len(file_data):
                    break
                temp_byte = file_data[counter_1]
                counter_1 -= 1
                # Allows @ Character To Appear Behind
                if temp_byte == newline_character:
                    output += b"@"
                    counter_1 += 1
                    continue
            if byte == newline_character:
                # Check Backward
                counter_1 -= 1
                if counter_1 < 0:
                    break
                temp_byte = file_data[counter_1]
                counter_1 += 1
                # Allows Newline Character To Appear In front
                if temp_byte == special_character:
                    output += b"\n"
                    counter_1 += 1
                    continue
                # Check Forward
                counter_1 += 1
                if counter_1 >= len(file_data):
                    break
                temp_byte = file_data[counter_1]
                counter_1 -= 1
                # Allows Newline Char To Appear Behind
                if temp_byte == special_character:
                    output += b"\n"
                    counter_1 += 1
                    continue
            masking_byte = 0b11000000
            for i in range(0, 4):
                result = byte & masking_byte
                if result == 0x00:
                    # Handle A
                    output += b"A"
                    count_1 += 1
                    byte = byte << 2
                elif result == 0x40:
                    # Handle T
                    if seq_type == "RNA":
                        output += b"U"
                    else:
                        output += b"T"
                    count_1 += 1
                    byte = byte << 2
                elif result == 0x80:
                    # Handle C
                    output += b"C"
                    count_1 += 1
                    byte = byte << 2
                elif result == 0xC0:
                    # Handle G
                    output += b"G"
                    count_1 += 1
                    byte = byte << 2
            counter_1 += 1

        # Write To That A New Kind Of File
        just_filename = str(filename)[str(filename).rfind('/'):str(filename).rfind('.')]
        new_filename = str(filename)[:str(filename).rfind('/')] + just_filename + ".hgf"
        try:
            with open(new_filename, "wb") as file:
                file.write(output)
        except Exception:
            return None

        return 0