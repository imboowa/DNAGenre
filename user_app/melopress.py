import tkinter
from tkinter import *
from customtkinter import *
from DNAtoolkit.structures import *
from interface.GUI_attr import *
from pathlib import Path
import os



class MeloPress:

    """ Compression And Decompression Page """

    def __init__(self, username, firstname, lastname, filename, previous_window, back_window, signing_window):

        """ Making Window """

        previous_window.destroy()

        filename = Path(filename)

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
        frame_1.pack(fill="both", pady=10, padx=5)
        # Filename Label
        filename_label = CTkLabel(frame_1, text=f"FileName:", font=(window_font, window_font_size - 10, font_style), fg_color=bright_colors[2],
                                  text_color=bright_colors[4])
        filename_label.grid(row=0, column=0, padx=10, pady=10)
        new_filename = str(filename)[str(filename).rfind('/')+1:]
        filename_label_value = CTkLabel(frame_1, text=f"{new_filename[:string_threshold]}..." if len(new_filename) > string_threshold else f"{new_filename}", font=(window_font, window_font_size - 10),
                                        fg_color=bright_colors[2], text_color=bright_colors[4])
        filename_label_value.grid(row=0, column=1, sticky="w")
        # File Bytes Label
        try: filebytes = os.path.getsize(filename)
        except OSError: filebytes = "Unobtained"
        except Exception: filebytes = "Unobtained"
        filebytes_label = CTkLabel(frame_1, text=f"FileBytes:", font=(window_font, window_font_size - 10, font_style),
                                   fg_color=bright_colors[2], text_color=bright_colors[4])
        filebytes_label.grid(row=0, column=3, padx=10, pady=10)
        self.filebytes_label_value = CTkLabel(frame_1, text=f"{str(filebytes)[:string_threshold]}..." if len(str(filebytes)) > string_threshold else f"{str(filebytes)}", font=(window_font, window_font_size - 10), fg_color=bright_colors[2],
                                         text_color=bright_colors[4])
        self.filebytes_label_value.grid(row=0, column=4, sticky="w")
        # State Label--Compressed Or Decompressed
        state_label = CTkLabel(frame_1, text=f"State:", font=(window_font, window_font_size - 10, font_style),
                                   fg_color=bright_colors[2], text_color=bright_colors[4])
        state_label.grid(row=0, column=5, padx=10, pady=10)
        self.state_label_value = CTkLabel(frame_1, text=f"Unavailable", font=(window_font, window_font_size - 10), fg_color=bright_colors[2],
                                         text_color=bright_colors[4])
        self.state_label_value.grid(row=0, column=6, sticky="w")
        # Sequence Type
        seq_type_label = CTkLabel(frame_1, text=f"SeqType:", font=(window_font, window_font_size - 10, font_style),
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
        # Mother Frame For Frame And Make DNAGenre
        mother_frame_1 = CTkFrame(self.window, fg_color=color_scheme)
        mother_frame_1.pack(fill="both", padx=10)
        # Frame For Menu And Decompress Chunks
        frame_4 = CTkFrame(mother_frame_1, fg_color=color_scheme)
        frame_4.pack(side="left", fill="both", expand=True, pady=10, padx=10)
        menu_button = CTkButton(frame_4, text="Menu", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=bright_colors[2], corner_radius=corner, font=(window_font, window_font_size),
                                command=lambda: self.call_menu_window(username, firstname, lastname, signing_window))
        menu_button.pack(side="left", pady=10, padx=10)
        decompress_chunks_button = CTkButton(frame_4, text="D Chunk", fg_color=color_scheme, text_color=bright_colors[4],
                                             hover_color=bright_colors[2], corner_radius=corner, font=(window_font, window_font_size),
                                             command=lambda: self.start_decompression_chunks(filename, frame_2))
        decompress_chunks_button.pack(side="right", padx=10, pady=10)
        frame_5 = CTkFrame(mother_frame_1, fg_color=color_scheme)
        frame_5.pack(side="right", fill="both", expand=True, pady=10, padx=25)
        prep_c = CTkButton(frame_5, text="Prep C", fg_color=color_scheme, text_color=bright_colors[4],
                           hover_color=bright_colors[2], corner_radius=corner, font=(window_font, window_font_size),
                           command=lambda: self.handle_format_comrpession(filename, frame_2))
        prep_c.pack(side="left", padx=25, pady=10)
        make_DNAGenre = CTkButton(frame_5, text="Make DNAGenre", fg_color=color_scheme, text_color=bright_colors[4],
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
            self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}")
            self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}")
            try: filebytes = os.path.getsize(filename)
            except OSError: filebytes = "Unobtained"
            except Exception: filebytes = "Unobtained"
            self.filebytes_label_value.configure(text=f"{str(filebytes)[:string_threshold]}..." if len(str(filebytes)) > string_threshold else f"{str(filebytes)}")
            self.update_file_content(filename, self.text_box)
        else:
            label_1 = CTkLabel(frame, text="Error Formating", text_color=bright_colors[1], fg_color=color_scheme,font=(window_font, window_font_size - 10))

        label_1.place(relx=0.44, rely=0.05)

        try: self.window.after(1000, label_1.destroy)
        except tkinter.TclError: return


    def handle_format_comrpession(self, filename, frame: CTkFrame):

        """ Receives Errors From self.format_compression And Displays Them """

        if self.format_compression(filename) == 0:
            label_1 = CTkLabel(frame, text="Successful Prep", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
            self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}")
            self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}")
            try: filebytes = os.path.getsize(filename)
            except OSError: filebytes = "Unobtained"
            except Exception: filebytes = "Unobtained"
            self.filebytes_label_value.configure(text=f"{str(filebytes)[:string_threshold]}..." if len(str(filebytes)) > string_threshold else f"{str(filebytes)}")
            self.update_file_content(filename, self.text_box)
        else:
            label_1 = CTkLabel(frame, text="Prep Error", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))

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
        # Strip Last Newline
        result = result.strip()

        # Update File--Decompressed File--To DNAGenre Style
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
            with open(filename, "r") as file:
                file_data = file.read()
        except FileNotFoundError:
            return "Unobtained"
        except Exception:
            return "Unobtained"

        result = list()
        # Special Character
        special_char = '@'
        temp_sequence_1 = str()
        # Arrange Data
        new_file_data = file_data.splitlines()
        for line in new_file_data:
            counter_1 = 0
            current_line_data = ""
            # Found Invalid Character In line
            found_invalid_character = False
            line = line.strip()
            while counter_1 < len(line):
                if temp_sequence_1 and line[counter_1] not in VALID_NUCLEOTIDES:
                    found_invalid_character = True
                    result.append([special_char, temp_sequence_1])
                    temp_sequence_1 = ""
                elif line[counter_1] in VALID_NUCLEOTIDES and not found_invalid_character:
                    current_line_data += line[counter_1]
                else:
                    # Then This Must Be An Invalid Character Or A Valid Character In Invalid Data
                    found_invalid_character = True
                counter_1 += 1
            temp_sequence_1 += current_line_data
        # Save Last Sequence Since There Is No "not in VALID_NUCLEOTIDES" Character To Trigger Append To List
        if temp_sequence_1:
            result.append([special_char, temp_sequence_1])

        return result


    def format_compression(self, filename):

        """ Make A Fasta, Fastq Or Any Valid DNA/RNA File Ready For Compression """

        # Check For Errors
        result = self.prepare_data_compression(filename)
        if result == "Unobtained":
            return -1

        # Write To File
        with open(filename, "w") as file:
            for i in result:
                for j in i:
                    file.write(j + "\n")

        return 0


    def start_compression(self, filename, frame: CTkFrame):

        """ Prepares Compression And Results """

        value = self.compress(filename)

        # Update Text Or Data In Text Box
        self.update_file_content(filename, self.text_box)

        if value == 0:
            label_1 = CTkLabel(frame, text="Success C", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        elif value == 1:
            label_1 = CTkLabel(frame, text="DNA & RNA", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        elif value == 2:
            label_1 = CTkLabel(frame, text="Invalid Chars", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        # Error Code 3 Does Not Exist Anymore - Improper Length
        elif value == 4:
            label_1 = CTkLabel(frame, text="Already C", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        else:
            label_1 = CTkLabel(frame, text="Unsuccessful C", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))

        label_1.place(relx=0.44, rely=0.05)

        try: self.window.after(1000, label_1.destroy)
        except tkinter.TclError: return


    def start_decompression(self, filename, frame: CTkFrame):

        """ Prepares Decompression And Results """

        value = self.decompress(filename)

        # In This Situation, There Is No Need To Update The Text Box Because MeloPress Only Writes To This filename In Compression

        if value == 0:
            label_1 = CTkLabel(frame, text="Success D", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        elif value == 1:
            label_1 = CTkLabel(frame, text="Not Compressed", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        elif value == 2:
            label_1 = CTkLabel(frame, text="Bad File Header", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        else:
            label_1 = CTkLabel(frame, text="Unsuccessful D", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))

        label_1.place(relx=0.44, rely=0.05)

        try: self.window.after(1000, label_1.destroy)
        except tkinter.TclError: return


    def start_decompression_chunks(self, filename, frame: CTkFrame):

        """ Starts Decompression Of Compressed Chunks Of Data """

        value = self.decompress_chunks(filename)

        if value == 0:
            label_1 = CTkLabel(frame, text="Passed D Chunks", text_color=bright_colors[3], fg_color=color_scheme, font=(window_font, window_font_size - 10))
        else:
            label_1 = CTkLabel(frame, text="Failed D Chunks", text_color=bright_colors[1], fg_color=color_scheme, font=(window_font, window_font_size - 10))

        label_1.place(relx=0.44, rely=0.05)

        try: self.window.after(1000, label_1.destroy)
        except tkinter.TclError: return


    def compress(self, filename):

        """ Compresses Read Index Data In File And Writes To A New File Till All Read Indexes Are Finished """

        # Did We Already Compress This File
        if self.get_state_header_info(filename) == "Compressed":
            return 4

        # Is This A Compressed File
        if os.path.splitext(filename)[-1] == ".fgh":
            return None

        # Get Prepared Data
        result = self.prepare_data_compression(filename)
        if result == "Unobtained":
            return None
        elif not result:
            return None

        # Counter For Files In Directory Created Because Of File Improper Length Improvise
        counter_2 = 1
        is_RNA = None

        for pair in result:
            # Stores Current Read Index's Data
            try:
                temp_data_1 = pair[1]
            except IndexError:
                return None
            except Exception:
                return None

            # Counter For Every 4 Bits
            count_1 = 0
            # Stores A Copy For count_1
            temp_count_1 = 0
            # Byte Packed Into
            packing_byte = 0
            # Temporary Storage Of A Copy Of packing_byte Which Is Used In Improper Length
            temp_packing_byte = 0
            # Overall Counter
            counter_1 = 0
            # output buffer
            output = bytearray()

            temp_data_1 = bytearray(temp_data_1, "utf-8")
            total_length = len(temp_data_1)

            temp_data_2 = bytearray()

            # Note: output And temp_data_2 Have A Difference--output Has Data That Is Never Erased While temp_data Has Data That Can Be Erased

            while counter_1 < total_length:
                byte = temp_data_1[counter_1]
                match chr(byte):
                    case 'A':
                        packing_byte = (packing_byte << 2) | 0b00
                    case 'T':
                        if is_RNA is True:
                            # File Contains RNA And DNA
                            return 1
                        is_RNA = False
                        packing_byte = (packing_byte << 2) | 0b01
                    case 'C':
                        packing_byte = (packing_byte << 2) | 0b10
                    case 'G':
                        packing_byte = (packing_byte << 2) | 0b11
                    case 'U':
                        if is_RNA is False:
                            # File Contains RNA And DNA
                            return 1
                        is_RNA = True
                        packing_byte = (packing_byte << 2) | 0b01
                    case _:
                        # File Contains Invalid Characters
                        return 2

                # Save packing_byte To temp_packing_byte
                temp_packing_byte = packing_byte
                # Update Variables
                count_1 += 1
                counter_1 += 1

                # Save count_1
                temp_count_1 = count_1

                if count_1 == 4:
                    output.append(packing_byte)

                    temp_data_2.append(packing_byte)

                    count_1, packing_byte = 0, 0

            # Get Folder Name
            just_folder_name = str(filename)[str(filename).rfind('/'):str(filename).rfind('.')]
            new_folder_name = str(filename)[:str(filename).rfind('/')] + just_folder_name + "_fgh"

            # Make Directory file_1_fgh
            os.makedirs(new_folder_name, exist_ok=True)

            # Prepare Compressed Data And Header
            # Magic Prefix - #H9
            magic_prefix_1, magic_prefix_2, magic_prefix_3 = 0b00100011, 0b01001000, 0b00111001

            # Get Folder Name
            # Write Current Compressed Data To File counter_2 Index Like 1 Into Directory Called file_1_fgh As 1.fgh
            new_file = new_folder_name + "/" + str(counter_2) + ".fgh"

            # This Is For Improper Length files
            if temp_count_1 != 4:
                # The Fourth Bit (Bit 4) Indicates That This File Has An Improper Length
                header = 0b1111 if is_RNA else 0b1110
                if count_1 == 1:
                    if counter_2 == 1:
                        header = 0b01011111 if is_RNA else 0b01011110
                    else:
                        header = 0b00011111 if is_RNA else 0b00011110
                elif count_1 == 2:
                    if counter_2 == 1:
                        header = 0b01101111 if is_RNA else 0b01101110
                    else:
                        header = 0b00101111 if is_RNA else 0b00101110
                elif count_1 == 3:
                    if counter_2 == 1:
                        header = 0b01111111 if is_RNA else 0b01111110
                    else:
                        header = 0b00111111 if is_RNA else 0b00111110
                output.append(temp_packing_byte)

                temp_data_2.append(temp_packing_byte)

                try:
                    with open(new_file, "wb") as file:
                        file.write(bytes([magic_prefix_1, magic_prefix_2, magic_prefix_3]))
                        file.write(bytes([header]))
                        file.write(temp_data_2)
                except Exception:
                    return None

            # For Proper Length Files
            else:
                # Prepare Header Include A Bit That Shows That This Is Our File - .fgh
                # Show That This Is A Head File--The First File To Be Compressed--Or Not Using The Seventh Bit
                if counter_2 == 1:
                    header = 0b01000111 if is_RNA else 0b01000110
                else:
                    header = 0b00000111 if is_RNA else 0b00000110

                try:
                    with open(new_file, "wb") as file:
                        file.write(bytes([magic_prefix_1, magic_prefix_2, magic_prefix_3]))
                        file.write(bytes([header]))
                        file.write(output) if counter_2 == 1 else file.write(temp_data_2)
                except Exception:
                    return None

            # Show User Results
            self.state_label_value.configure(text=f"{self.get_state_header_info(filename)}")
            self.seq_type_label_value.configure(text=f"{self.get_seq_type_header_info(filename)}")

            counter_2 += 1

        return 0


    def decompress(self, filename, is_decompressing_chunks=False, mother_file=None, is_last_file=False, is_first_file=False):

        """ Decompresses Data In File And Writes To A New File """

        # File Must Be Compressed
        if self.get_state_header_info(filename) != "Compressed":
            return 1

        # File Must Be A .fgh File
        if os.path.splitext(filename)[-1] != ".fgh":
            return None

        # Open File
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return None
        except Exception:
            return None

        file_magic = file_data[:3]
        # Despite The Name Here, This Header Byte Has Information Like:
        # Does The File Have Improper Length Or Not
        # Is The Sequence Type (DNA or RNA)
        # Is The File Compressed Or Not
        # Is It An .fgh File
        # Is The File Length Indivisible By 4
        # How Many Bytes Are Allowed At The End Of A File With File Length That Is Indivisible By 4
        # Is This A Head File--File That Is The First In Compressed Chunks Folder From A Big File Due To Improper Length Incident
        # Is This A Segment File
        file_header = f"{file_data[3]:08b}"
        # Improper File Header
        if file_magic != b"#H9":
            return 2
        if file_header[-1] == "0":
            seq_type = "DNA"
        elif file_header[-1] == "1":
            seq_type = "RNA"
        else:
            return 2

        consider_improper_file_length = False
        acceptable_length = "00"
        if file_header[-4] == "1":
            consider_improper_file_length = True
            # Get The Count Of How Many Nucleotides Are Allowed At The End Of Improper Length Files
            acceptable_length = file_header[-6:-4]
            if acceptable_length == "00": acceptable_length = 0
            elif acceptable_length == "01": acceptable_length = 1
            elif acceptable_length == "10": acceptable_length = 2
            elif acceptable_length == "11": acceptable_length = 3

        # Check If File Is A Segment File
        if file_header[-8] == "1": is_a_segment_file = True
        else: is_a_segment_file = False

        output = bytearray()
        # Append The Formating Characters
        special_character = ord("@")
        newline_character = ord("\n")
        if not is_a_segment_file:
            output.append(special_character)
            output.append(newline_character)

        # Starting To Decompress At Index 4 Because Indexes 0,1,2,3 Have File Magic And File Header
        counter_1 = 4
        while counter_1 < len(file_data):
            byte = file_data[counter_1]
            count_1 = 0
            masking_byte = 0b11000000
            for i in range(0, 4):
                result = byte & masking_byte
                if result == 0x00:
                    if consider_improper_file_length and counter_1 == len(file_data) - 1:
                        # Add An "A" If The acceptable_length Has Not Been Met
                        # Subtracting 4 From acceptable_length Gives Index Where To Start Accepting "A"
                        if i >= (4 - acceptable_length):
                            output += b"A"
                        count_1 += 1
                        byte = byte << 2
                        continue
                    # Handle A
                    output += b"A"
                elif result == 0x40:
                    # Handle T Or U Respective Of seq_type
                    if seq_type == "RNA":
                        output += b"U"
                    else:
                        output += b"T"
                elif result == 0x80:
                    # Handle C
                    output += b"C"
                elif result == 0xC0:
                    # Handle G
                    output += b"G"
                # Just In Case - Not Needed
                else:
                    return None

                count_1 += 1
                byte = byte << 2
            counter_1 += 1

        if is_decompressing_chunks and not is_first_file:
            # Write To Mother File
            try:
                with open(mother_file, "ab") as file:
                    if not is_last_file:
                        file.write(output + b"\n")
                    else:
                        file.write(output)
            except Exception:
                return None
        elif is_decompressing_chunks and is_first_file:
            # Write To Mother File
            try:
                with open(mother_file, "wb") as file:
                    if not is_last_file:
                        file.write(output + b"\n")
                    else:
                        file.write(output)
            except Exception:
                return None
        else:
            # Write To That A New Kind Of File
            just_filename = str(filename)[str(filename).rfind('/'):str(filename).rfind('.')]
            new_filename = str(filename)[:str(filename).rfind('/')] + just_filename + ".hgf"
            try:
                with open(new_filename, "wb") as file:
                    file.write(output)
            except Exception:
                return None

        return 0


    def decompress_chunks(self, filename):

        """ Decompresses Compressed Chunks Of Bioinformatic Data """

        if self.get_state_header_info(filename) != "Compressed":
            return None

        # Check File Extension Too
        if os.path.splitext(filename)[-1] != ".fgh":
            return None

        # Open Given File
        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            return None
        except Exception:
            return None

        # If Head File Then Look For The Directory With Compressed Chunks
        header = file_data[3]
        new_header = f"{header:08b}"
        if new_header[-7] == "1":
            # Get Folder Name
            new_folder_name = str(filename)[:str(filename).rfind('/')]
            if os.path.exists(new_folder_name):
                files = [file for file in os.listdir(new_folder_name) if file.endswith(".fgh")]
                try:
                    # Arrange Then In A List From 1 To End
                    sorted_files = sorted(files, key=lambda file: int(os.path.splitext(file)[0]))
                except ValueError:
                    return None
                except Exception:
                    return None
            else:
                # Chunk Directory Missing
                return 2
        else:
            # Cannot Be Decompressed From Chunks
            return 1

        # Mother File
        # Remove "/" If It Is The Last Character In Filepath Even Though "Path" Removes It
        mother_file = new_folder_name[:-5] + ".hgf" if new_folder_name[-1] == "/" else new_folder_name[:-4] + ".hgf"

        # Use A For loop To Decompress File By File While Appending Data To Mother File
        total_length = len(sorted_files)
        counter_1 = 0
        for file in sorted_files:
            full_filename = new_folder_name + "/" + file
            if counter_1 == 0 and total_length == 1:
                value = self.decompress(full_filename, is_decompressing_chunks=True, mother_file=mother_file, is_last_file=True, is_first_file=True)
            elif counter_1 == 0:
                value = self.decompress(full_filename, is_decompressing_chunks=True, mother_file=mother_file, is_first_file=True)
            elif counter_1 == total_length - 1:
                value = self.decompress(full_filename, is_decompressing_chunks=True, mother_file=mother_file, is_last_file=True)
            else:
                value = self.decompress(full_filename, is_decompressing_chunks=True, mother_file=mother_file)
            counter_1 += 1
            if value == 0:
                continue
            else:
                return None

        # Finish
        return 0