import tkinter
from tkinter import *
from customtkinter import *
from interface.GUI_attr import *
from decode.functions import *


class User_Script:

    """ Scripting Page """

    def __init__(self, filename, DNA_data, username, firstname, lastname, prev_window, menu_window, sign_window):

        """ Scripting Window """

        # Remove Old Window
        try: prev_window.destroy()
        except tkinter.TclError: return
        # Useful Variables
        self.DNA_data = DNA_data
        self.desired_read_index_data = list()
        self.debugging = False
        # Length For Updated List In Normal Mode
        self.updatedList_length = 0

        self.start = 0
        self.end = view_limit * 4
        # Used By navigate To See In Normal Mode
        self.theData = list()
        self.theResults = list()
        # Window
        self.script_window = Tk()
        self.script_window.title(f"{str(filename)[str(filename).rindex('/')+1:]}..." if len(str(filename)[str(filename).rindex('/')+1:]) > string_threshold else f"{str(filename)[str(filename).rindex('/')+1:]}")
        self.script_window.geometry(f"1080x{self.script_window.winfo_screenheight()}")
        self.script_window.config(bg=f"{color_scheme}")
        self.script_window.eval("tk::PlaceWindow . center")
        self.script_window.resizable(False, False)
        # Frame For Read Index And Get
        self.frame_1 = CTkFrame(self.script_window, fg_color=color_scheme)
        self.frame_1.pack(pady=10)
        # Read Index Entry
        self.read_index_entry = CTkEntry(self.frame_1, placeholder_text="Enter Read Index", placeholder_text_color=bright_colors[0],
                                    text_color=bright_colors[5], font=(window_font, window_font_size), fg_color=color_scheme,
                                    height=60, width=600, border_width=border, border_color=bright_colors[2])
        self.read_index_entry.pack(side="left", padx=40)
        # Get Button
        self.run_button = CTkButton(self.frame_1, text="Run", font=(window_font, window_font_size), fg_color=color_scheme,
                               text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2], width=300,
                               height=60, command=lambda: self.run_script())
        self.run_button.pack(side="right", padx=40)
        # Mother Frame
        self.mother_frame_1 = CTkFrame(self.script_window, fg_color=color_scheme)
        self.mother_frame_1.pack(fill='both')
        # User Code Label
        user_code_label = CTkLabel(self.mother_frame_1, text="User Code", font=(window_font, window_font_size), fg_color=color_scheme,
                                   text_color=bright_colors[5])
        user_code_label.pack(side="left", padx=50)
        # Frame For Information Label, Run Button, And Debug Button
        self.frame_2 = CTkFrame(self.mother_frame_1, fg_color=color_scheme)
        self.frame_2.pack(side="right", padx=40, pady=5)
        # Information Label
        information_label = CTkLabel(self.frame_2, text="Information", font=(window_font, window_font_size), fg_color=color_scheme,
                                     text_color=bright_colors[5])
        information_label.grid(row=0, column=0, padx=10, pady=5)
        # Run Button
        set_button = CTkButton(self.frame_2, text="Set", font=(window_font, window_font_size), fg_color=color_scheme,
                               text_color=bright_colors[4], corner_radius=corner, hover_color=bright_colors[2],
                               command=lambda: self.set_debug())
        set_button.grid(row=0, column=1, padx=5, pady=5)
        # Debug Button
        self.debug_label = CTkLabel(self.frame_2, text=f"Debug\n{self.debugging}", font=(window_font, window_font_size - 10), fg_color=color_scheme,
                                 text_color=bright_colors[4])
        self.debug_label.grid(row=0, column=2, padx=5, pady=5)
        # Mother Frame For Code Editor And Process Information
        self.mother_frame_2 = CTkFrame(self.script_window, fg_color=color_scheme)
        self.mother_frame_2.pack(fill="both")
        # Code Editor Text Area
        self.code_editor = CTkTextbox(self.mother_frame_2, fg_color=bright_colors[5], text_color=color_scheme, border_color=bright_colors[2],
                                      border_width=border, corner_radius=corner, font=(window_font, (window_font_size - 10)),
                                      height=350)
        self.code_editor.tag_config("tag", background=bright_colors[3])
        self.code_editor.pack(side="left", expand=True, fill="both", padx=10, pady=5)
        # Information Frame
        self.frame_3 = CTkFrame(self.mother_frame_2, fg_color=bright_colors[3], height=350)
        self.frame_3.pack(side="right", expand=True, fill="both", padx=10, pady=5)
        # Mother Frame For Results
        self.mother_frame_3 = CTkScrollableFrame(self.script_window, fg_color=color_scheme, orientation="horizontal",
                                                 scrollbar_fg_color=color_scheme, scrollbar_button_color=color_scheme,
                                                 scrollbar_button_hover_color=color_scheme, height=160)
        self.mother_frame_3.pack(fill="both")
        # Mother Frame For Navigation Buttons
        self.mother_frame_4 = CTkFrame(self.script_window, fg_color=color_scheme)
        self.mother_frame_4.pack(fill="both")
        # Subframe For self.move_left And self.move_right And self.index_label
        self.subframe = CTkFrame(self.mother_frame_4, fg_color=color_scheme)
        self.subframe.pack(fill="both")
        # Left Navigation Button
        self.move_left = CTkButton(self.subframe, text="<", font=(window_font, window_font_size - 10), fg_color=color_scheme,
                                   text_color=color_scheme, hover_color=color_scheme,
                                   command=lambda: self.navigate("move_left"), state="disabled")
        self.move_left.pack(side="left")
        # Shows User The Location In Updated List
        self.index_label = CTkLabel(self.subframe, text=f"[{self.start}-{self.end})" if len(str(self.end)) <= string_threshold else f"[{self.start}-{str(self.end)[:string_threshold]}...)",
                                    font=(window_font, window_font_size - 10), fg_color=color_scheme, text_color=bright_colors[5])
        self.index_label.place(relx=0.45, rely=0.0)
        # Right Navigation Button
        self.move_right = CTkButton(self.subframe, text=">", font=(window_font, window_font_size - 10), fg_color=color_scheme,
                                    text_color=color_scheme, hover_color=color_scheme,
                                    command=lambda: self.navigate("move_right"), state="disabled")
        self.move_right.pack(side="right")
        # Menu Button
        menu_button = CTkButton(self.mother_frame_4, text="Menu", font=(window_font, window_font_size - 10), fg_color=color_scheme,
                                text_color=bright_colors[4], hover_color=bright_colors[2],
                                command=lambda: self.back_to_menu(username, firstname, lastname, menu_window, sign_window))
        menu_button.pack(side="bottom")
        self.script_window.mainloop()


    def back_to_menu(self, username, firstname, lastname, menu_window, sign_window):

        """ Goes Back To Menu """

        try:
            self.script_window.destroy()
        except TclError: return
        menu_window(username, firstname, lastname, sign_window)


    def navigate(self, direction):

        """ Controls Navigation Buttons """

        if direction == "move_left":
            if self.start >= view_limit * 4:
                self.start -= view_limit * 4
                self.end -= view_limit * 4
                # Showing Debug's Updated List
                if self.debugging:
                    self.draw_updatedList(self.tempData, self.updatedList)
                # Showing Normal Mode's Updated List
                elif not self.debugging:
                    self.draw_updatedList(self.theData, self.theResults)
                # Update self.index_label
                if len(str(self.start)) > string_threshold:
                    self.index_label.configure(text=f"[{str(self.start)[:string_threshold]}...-{self.end})")
                elif len(str(self.end)) > string_threshold:
                    self.index_label.configure(text=f"[{self.start}-{str(self.end)[:string_threshold]}...)")
                elif len(str(self.start)) > string_threshold and len(str(self.end)) > string_threshold:
                    self.index_label.configure(text=f"[{str(self.start)[:string_threshold]}...-{str(self.end)[:string_threshold]}...)")
                else:
                    self.index_label.configure(text=f"[{self.start}-{self.end})")
        elif direction == "move_right":
            if self.end < self.updatedList_length:
                self.end += view_limit * 4
                self.start += view_limit * 4
                # Showing Debug's Updated List
                if self.debugging:
                    self.draw_updatedList(self.tempData, self.updatedList)
                # Showing Normal Mode's Updated List
                elif not self.debugging:
                    self.draw_updatedList(self.theData, self.theResults)
                # Update self.index_label
                self.index_label.configure(text=f"({self.start}-{self.end}]")


    def get_DNA_Data(self):

        """ Get The DNA Data """

        # Get Read Index
        read_index = str(self.read_index_entry.get())

        """ Look For Read Index In DNA Data """
        for key, value in self.DNA_data.items():
            if key == read_index:
                return value
        return None


    def get_User_code(self):

        """ Get The User Code """

        code = list()
        lineCode = ""
        for char in self.code_editor.get("1.0", "end"):
            if char == "\n":
                code.append(lineCode)
                # Reset lineCode
                lineCode = ""
            else:
                lineCode += char
        return code


    def set_debug(self):

        """ Set Debug Flag """

        if self.debugging:
            self.debugging = False
            # Clear Tag
            self.code_editor.tag_remove("tag", "1.0", "end")
            self.debug_label.configure(text=f"Debug\n{self.debugging}")
        elif not self.debugging:

            # Get Code
            self.codeLines = self.get_User_code()
            if not self.codeLines:
                return
            # Data To Be Checked
            self.tempData = self.get_DNA_Data()
            if self.tempData is None:
                return

            # Error Flags
            self.error_flags = {"out_of_bounds": 0,      # Indexing Out Of Bounds
                                "variable_access": 0,    # Accessing A Wrong Variable
                                "not_integer": 0,        # Not Using Integers
                                "zero_division": 0,      # Dividing By Zero
                                "bad_command": 0,        # Invalid Command
                                "bad_value_printr": 0,   # Inserting A Bad Value Into Output List That Is Not 0 Or 1
                                "argument_error": 0,     # Not Enough Arguments Or Error In Arguments To Function Call
                                "internal_error": 0,     # Indicates OS Or Python Has A Problem
                                "no_errors": True        # Global Status Flag
                                }

            # List To Be Updated
            self.updatedList = [0] * len(self.tempData)

            # dict To Store Variables And Values
            self.vars = dict()
            # Setting Defaults
            self.vars["a"] = len(self.tempData)
            self.vars["b"] = "0"
            self.vars["c"] = "0"

            # Flag For If Statements
            self.IF_FLAG: int = 1
            # Remembers Temporary Value For when
            self.tempValue: str = ""
            # Remembers Temporary Index For when
            self.tempIndex: int = 0
            # Program Counter
            self.execCounter: int = 0

            self.debugging = True
            self.debug_label.configure(text=f"Debug\n{self.debugging}")


    def draw_updatedList(self, tempData, updatedList):

        """ Draw Updated List On GUI """

        """ Showing Results """
        # Clear Frame
        if self.mother_frame_3.winfo_children():
            for widget in self.mother_frame_3.winfo_children():
                widget.destroy()
        # Showing Results
        # Remember We Are Shifting In The updatedList So We Need To Use The Values In The Shift Because They Reflect What Is Current
        # If We Start From 0 Then We Are Always Just Showing Values From 0 To viewLimit * 4 Hence Showing Wrong Values In updatedList
        start: int = self.start
        for i, nuc in enumerate(tempData[self.start:self.end]):
            if updatedList[start] == 1:
                if nuc == "A":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=color_scheme, fg_color="green", corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "T":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=color_scheme, fg_color="yellow", corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "G":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=color_scheme, fg_color="orange", corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "C":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=color_scheme, fg_color="blue", corner_radius=corner,
                             width=40, height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "U":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=color_scheme, fg_color="magenta", corner_radius=corner,
                             width=40, height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                # Preventing Weird Values That Are Not A,T,G,C,U
                else:
                    break
            else:
                if nuc == "A":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "T":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "G":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner, width=40,
                             height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "C":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner,
                             width=40, height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                elif nuc == "U":
                    CTkLabel(self.mother_frame_3, text=f"{nuc}\n{updatedList[start]}", font=(window_font, window_font_size),
                             text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner,
                             width=40, height=150).grid(row=0, column=i, sticky="w", padx=7, pady=5)
                # Preventing Weird Values That Are Not A,T,G,C,U
                else:
                    break
            start += 1


    def highlight_line(self, line_number):

        """ Highlight Line """

        # Remove General Or Overall Tag On Text
        self.code_editor.tag_remove("tag", "1.0", "end")

        start = f"{line_number + 1}.0"
        end = f"{line_number + 1}.end"

        self.code_editor.tag_add("tag", start, end)
        self.code_editor.see(start)


    def run_script(self):

        """ Run The Script """

        # Call Debugger If Debug Mode
        if self.debugging:
            self.run_debug_script()
            return

        # Reset Boundaries
        self.start = 0
        self.end = view_limit * 4
        # Update self.index_label
        self.index_label.configure(text=f"[{self.start}-{self.end})" if len(str(self.end)) <= string_threshold else f"[{self.start}-{self.end}...)")
        # Disable The Button
        self.run_button.configure(state="disabled")
        # Update The Window
        self.script_window.update_idletasks()

        # Get Code
        codeLines = self.get_User_code()
        if not codeLines:
            # Enable The Disabled Buttons
            self.run_button.configure(state="normal")

            # Force Window To Redraw
            self.script_window.update_idletasks()
            self.script_window.update()
            return

        # Data To Be Checked
        tempData = self.get_DNA_Data()
        if tempData is None:
            # Enable The Disabled Buttons
            self.run_button.configure(state="normal")

            # Force Window To Redraw
            self.script_window.update_idletasks()
            self.script_window.update()
            return

        # Error Flags
        error_flags = {"out_of_bounds": 0,            # Indexing Out Of Bounds
                       "variable_access": 0,          # Accessing A Wrong Variable
                       "not_integer": 0,              # Not Using Integers
                       "zero_division": 0,            # Dividing By Zero
                       "bad_command": 0,              # Invalid Command
                       "bad_value_output": 0,         # Inserting A Bad Value Into Output List That Is Not 0 Or 1
                       "argument_error": 0,           # Not Enough Arguments Or Error In Arguments To Function Call
                       "internal_error": 0,           # Indicates OS Or Python Has A Problem
                       "no_errors": True              # Global Status Flag
                       }

        # List To Be Updated
        updatedList = [0] * len(tempData)

        # dict To Store Variables And Values
        vars = dict()
        # Setting Defaults
        vars["a"] = len(tempData)
        vars["b"] = "0"
        vars["c"] = "0"

        # Flag For If Statements
        IF_FLAG: int = 1
        # Remembers Temporary Value For when
        tempValue: str = ""
        # Remembers Temporary Index For when
        tempIndex: int = 0
        # Program Counter
        execCounter: int = 0
        while len(codeLines) > execCounter >= 0 and error_flags["no_errors"] and not self.debugging:
            try:
                vars, error_flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList = executeLine(codeLines[execCounter], vars, error_flags, execCounter, tempIndex, tempValue, IF_FLAG, tempData, updatedList)
            except IndexError:
                # User Did Not Give Full Arguments On A Function Call
                error_flags["argument_error"] = 1
                error_flags["no_errors"] = False
            except Exception:
                # Imagine Python Or The OS Run Into Problems Like User Doing An Infinite Loop, Stack Overflow
                error_flags["internal_error"] = 1
                error_flags["no_errors"] = False
            execCounter += 1

        # Is self.frame_3 Full, Remove Widgets
        if self.frame_3.winfo_children():
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        # Subframe For Variable Showcase
        frame_1 = CTkScrollableFrame(self.frame_3, fg_color="blue")
        frame_1.pack(side="top", expand=True, fill="both", padx=10, pady=5)
        # Showcasing Variables
        row_counter = 0
        column_counter = 0
        for key, value in vars.items():
            if len(str(key)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}...::{value[:string_threshold]}",
                         text_color=bright_colors[5], font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            elif len(str(value)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}::{value[:string_threshold]}...",
                         text_color=bright_colors[5], font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            elif len(str(key)) > string_threshold and len(str(value)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}...::{value[:string_threshold]}...",
                         text_color=bright_colors[5], font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            else:
                CTkLabel(frame_1, text=f"{key}::{value}", font=(window_font, window_font_size - 10),
                         text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner).grid(row=row_counter,
                        column=column_counter, padx=10, pady=5, sticky="w")
            column_counter += 1
            if column_counter == 2:
                row_counter += 1
                column_counter = 0
        # Showcasing Errors
        if not error_flags["no_errors"]:
            # Subframe For Showcasing Errors
            frame_2 = CTkScrollableFrame(self.frame_3, fg_color="black")
            frame_2.pack(side="bottom", expand=True, fill="both", padx=10, pady=5)
            # Get Error
            for index, value in enumerate(list(error_flags.values())):
                if value == 1:
                    CTkLabel(frame_2, text=f"Line: {str(execCounter)}" if len(str(execCounter)) <= string_threshold else f"Line: {str(execCounter)[:string_threshold]}...",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=0, column=0, sticky="w", padx=5, pady=5)
                    CTkLabel(frame_2,
                             text=f"Content: {str(codeLines[execCounter - 1])}" if len(str(codeLines[execCounter - 1])) <= string_threshold else f"Content: {str(codeLines[execCounter - 1])[:string_threshold]}...",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=1, column=0, sticky="w", padx=5, pady=5)
                    CTkLabel(frame_2,
                             text=f"Error: {list(error_flags.keys())[index]}",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=2, column=0, sticky="w", padx=5, pady=5)
                    # In Order To Show One Error At A Time
                    break

        self.updatedList_length = len(tempData)
        # Make The tempData And updatedList Global For navigate To See
        self.theData = tempData
        self.theResults = updatedList
        # Drawing Results On Screen
        self.draw_updatedList(tempData, updatedList)

        # Enable The Disabled Buttons
        self.run_button.configure(state="normal")
        self.move_right.configure(state="normal")
        self.move_left.configure(state="normal")
        self.move_right.configure(text_color=bright_colors[4])
        self.move_left.configure(text_color=bright_colors[4])

        # Force Window To Redraw
        self.script_window.update_idletasks()
        self.script_window.update()


    def run_debug_script(self):

        """ Runs The Debug Script """

        if len(self.codeLines) > self.execCounter >= 0 and self.error_flags["no_errors"] and self.debugging:
            # Highlight Line
            self.highlight_line(self.execCounter)
            try:
                self.vars, self.error_flags, self.execCounter, self.tempIndex, self.tempValue, self.IF_FLAG, self.updatedList = executeLine(self.codeLines[self.execCounter], self.vars, self.error_flags, self.execCounter, self.tempIndex, self.tempValue, self.IF_FLAG, self.tempData, self.updatedList)
            except IndexError:
                # User Did Not Give Full Arguments On A Function Call
                self.error_flags["argument_error"] = 1
                self.error_flags["no_errors"] = False
            except Exception:
                # Imagine Python Or OS Run Into Errors Like Stack Overflow, Infinite Loop Etc
                self.error_flags["internal_error"] = 1
                self.error_flags["no_errors"] = False
            self.execCounter += 1

        # Is self.frame_3 Full, Remove Widgets
        if self.frame_3.winfo_children():
            for widget in self.frame_3.winfo_children():
                widget.destroy()
        # Subframe For Variable Showcase
        frame_1 = CTkScrollableFrame(self.frame_3, fg_color="blue")
        frame_1.pack(side="top", expand=True, fill="both", padx=10, pady=5)
        # Showcasing Variables
        row_counter = 0
        column_counter = 0
        for key, value in self.vars.items():
            if len(str(key)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}...::{value[:string_threshold]}",
                         text_color=bright_colors[5],font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            elif len(str(value)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}::{value[:string_threshold]}...",
                         text_color=bright_colors[5], font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            elif len(str(key)) > string_threshold and len(str(value)) > string_threshold:
                CTkLabel(frame_1, text=f"{key[:string_threshold]}...::{value[:string_threshold]}...",
                         text_color=bright_colors[5], font=(window_font, window_font_size - 10), fg_color=color_scheme,
                         corner_radius=corner).grid(row=row_counter, column=column_counter, padx=10, pady=5, sticky="w")
            else:
                CTkLabel(frame_1, text=f"{key}::{value}", font=(window_font, window_font_size - 10),
                         text_color=bright_colors[5], fg_color=color_scheme, corner_radius=corner).grid(row=row_counter,
                         column=column_counter, padx=10, pady=5, sticky="w")
            column_counter += 1
            if column_counter == 2:
                row_counter += 1
                column_counter = 0
        # Showcasing Errors
        if not self.error_flags["no_errors"]:
            # Subframe For Showcasing Errors
            frame_2 = CTkScrollableFrame(self.frame_3, fg_color="black")
            frame_2.pack(side="bottom", expand=True, fill="both", padx=10, pady=5)
            # Get Error
            for index, value in enumerate(list(self.error_flags.values())):
                if value == 1:
                    CTkLabel(frame_2, text=f"Line: {str(self.execCounter)}" if len(
                        str(self.execCounter)) <= string_threshold else f"Line: {str(self.execCounter)[:string_threshold]}...",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=0, column=0, sticky="w", padx=5, pady=5)
                    CTkLabel(frame_2,
                             text=f"Content: {str(self.codeLines[self.execCounter - 1])}" if len(str(self.codeLines[self.execCounter - 1])) <= string_threshold else f"Content: {str(self.codeLines[self.execCounter - 1])[:string_threshold]}...",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=1, column=0, sticky="w", padx=5, pady=5)
                    CTkLabel(frame_2,
                             text=f"Error: {list(self.error_flags.keys())[index]}",
                             font=(window_font, window_font_size - 10), fg_color=color_scheme, corner_radius=corner,
                             text_color=bright_colors[1]).grid(row=2, column=0, sticky="w", padx=5, pady=5)
                    # In Order To Show One Error At A Time
                    break

        # Redrawing On Every Run
        self.draw_updatedList(self.tempData, self.updatedList)

        # Update Window
        self.script_window.update_idletasks()
        self.script_window.update()