from interface.GUI_control import *
import datetime
from user_app.DNAsite import *
from DNAtoolkit.DataTools import *
from pathlib import Path


class User_Home:

    def __init__(self, username, firstname, lastname):

        """ User's Home Page """
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        # Get The Folder Path And Previous Last Session Before They Are Overwritten
        self.folder_path, last_session = self.get_user_data(username)
        # Is The Got Data Healthy
        if self.folder_path is None or last_session is None:
            return
        # Prepare Our Information For Display
        last_month_day_year, last_hour_minute = last_session.split('|')
        # Now Get The Time Now And Overwrite The Old Time in Database
        """ Save Login Time """
        insert_last_session(usage_database_file, username, f"{datetime.datetime.now().month:02}/{datetime.datetime.now().day:02}/"
                                                           f"{datetime.datetime.now().year}|{datetime.datetime.now().hour:02}:"
                                                           f"{datetime.datetime.now().minute:02}")
        """ User Home Page Window """
        self.user_home_window = Tk()
        self.user_home_window.title(f"{username[:string_threshold]}..." if len(username) > string_threshold else f"{username}")
        self.user_home_window.geometry(f"1080x{self.user_home_window.winfo_screenheight()}")
        self.user_home_window.config(bg=f"{color_scheme}")
        self.user_home_window.eval("tk::PlaceWindow . center")
        self.user_home_window.resizable(False, False)
        """ Frame For Username """
        self.frame_1 = CTkFrame(self.user_home_window, fg_color=color_scheme, corner_radius=corner,
                              height=(self.user_home_window.winfo_height() / 0.25), width=(self.user_home_window.winfo_width() / 0.5))
        self.frame_1.grid(row=0, column=0, padx=50)
        """ Show Username """
        username_label = CTkLabel(self.frame_1, text=f"{username[:string_threshold]}..." if len(username) > string_threshold else f"{username}", font=(window_font, (window_font_size + 20)), fg_color=color_scheme, text_color=bright_colors[5])
        username_label.grid(row=0, column=0, pady=50, padx=50)
        """ Frame For User Info """
        self.frame_2 = CTkFrame(self.user_home_window, fg_color=color_scheme, corner_radius=corner,
                              height=(self.user_home_window.winfo_height() / 0.25), width=(self.user_home_window.winfo_width() / 0.5))
        self.frame_2.grid(row=0, column=1)
        """ User Info """
        last_session_label = CTkLabel(self.frame_2, text=f"{str(last_month_day_year)} {str(last_hour_minute)}", font=(window_font, window_font_size),
                                      fg_color=color_scheme, text_color=text_color)
        last_session_label.pack(anchor='w', pady=10)
        firstname_label = CTkLabel(self.frame_2, text=f"{firstname[:string_threshold]}..." if len(firstname) > string_threshold else f"{firstname}", font=(window_font, window_font_size), fg_color=color_scheme, text_color=text_color)
        firstname_label.pack(anchor='w', pady=10)
        lastname_label = CTkLabel(self.frame_2, text=f"{lastname[:string_threshold]}..." if len(lastname) > string_threshold else f"{lastname}", font=(window_font, window_font_size), fg_color=color_scheme, text_color=text_color)
        lastname_label.pack(anchor='w', pady=10)
        """ Everything Frame Files, Folder """
        self.frame_3 = CTkScrollableFrame(self.user_home_window, fg_color=bright_colors[3], corner_radius=corner, height=300,
                                          scrollbar_fg_color=bright_colors[3],scrollbar_button_color=bright_colors[3],
                                          scrollbar_button_hover_color=bright_colors[3], width=(self.user_home_window.winfo_width() - 40))
        """ Files """
        # Counter For The Folder Files Limit
        folder_files_limit_1 = 0
        self.folder_start, self.folder_stop = 0, view_limit
        # If The Database Folder Path Is Valid (could be old user)
        if os.path.isdir(str(self.folder_path)):
            """ Entry For Reading Folders """
            self.folder_entry = CTkEntry(self.user_home_window, placeholder_text="Enter a Folder",
                                         placeholder_text_color=bright_colors[0],
                                         corner_radius=corner, height=100, width=600, fg_color=color_scheme, text_color=bright_colors[5],
                                         border_color=bright_colors[2], border_width=border, font=(window_font, (window_font_size + 20)))
            self.folder_entry.grid(row=1, column=0, padx=30, pady=10)
            """ Frame For Buttons """
            self.frame_5 = CTkFrame(self.user_home_window, fg_color=color_scheme, width=200)
            self.frame_5.grid(row=1, column=1, pady=10, padx=10)
            """ Buttons For Reading And Create """
            create_folder = CTkButton(self.frame_5, text="Create", font=(window_font, window_font_size), fg_color=color_scheme,
                                      text_color=bright_colors[4],
                                      corner_radius=corner, hover_color=bright_colors[2], command=self.create_dir)
            create_folder.place(relx=0.01, rely=0.2)
            read_folder = CTkButton(self.frame_5, text="Read", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                    corner_radius=corner, hover_color=bright_colors[2],
                                    command=lambda: self.increase_button("Show new user files", username))
            read_folder.place(relx=0.01, rely=0.55)
            # If Folder Path In Database Was Invalid (blocked here), The User Could Still Enter A New Choice
            # Open Folder, Put Frame And Populate It With The Folder Files
            folder_path_files = open_folder(str(self.folder_path))
            if folder_path_files is None:
                return
            """ Viewport Controllers """
            end_label_1 = CTkButton(self.user_home_window, text="<", font=(window_font, window_font_size),
                                    fg_color=color_scheme,
                                    text_color=bright_colors[4], hover_color=color_scheme, corner_radius=corner,
                                    command=lambda: self.increase_button("Show Additional Files-", username))
            end_label_1.grid(row=2, column=0, padx=10, sticky="news")
            end_label_2 = CTkButton(self.user_home_window, text=">", font=(window_font, window_font_size),
                                    fg_color=color_scheme,
                                    text_color=bright_colors[4], hover_color=color_scheme, corner_radius=corner,
                                    command=lambda: self.increase_button("Show Additional Files+", username))
            end_label_2.grid(row=2, column=1, padx=10, sticky="news")
            # Label To Show Location In Navigation
            self.location_label = CTkLabel(self.user_home_window, text=f"", font=(window_font,window_font_size), fg_color=color_scheme, text_color=text_color)
            self.location_label.place(relx=0.5, rely=0.45)
            """ Displaying The Files """
            self.frame_3_1 = CTkScrollableFrame(self.user_home_window, scrollbar_button_color=bright_colors[3], fg_color=bright_colors[3],
                                           scrollbar_fg_color=bright_colors[3], scrollbar_button_hover_color=bright_colors[3],
                                           corner_radius=corner, height=300, width=(self.user_home_window.winfo_width() - 40))
            self.frame_3_1.place(rely=0.5, relx=0.010)
            """ Show Files """
            for file in folder_path_files:
                if folder_files_limit_1 == view_limit:
                    break
                path_start_index = str(self.folder_path).rindex('/') + 1
                file_label = CTkButton(self.frame_3_1,
                                       text=f"{str(self.folder_path[path_start_index:])}/{str(file)}",
                                       font=(window_font, window_font_size), fg_color=color_scheme,
                                       text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                       command=lambda f='/' + file: self.start_DNA_analysis(str(self.folder_path) + str(f)))
                file_label.pack(anchor='w', pady=5)
                folder_files_limit_1 += 1
        # If It Is Invalid, Then Ask New User For New Choice
        elif not os.path.isdir(str(self.folder_path)):
            """ Entry For Reading Folders """
            self.folder_entry = CTkEntry(self.user_home_window,placeholder_text="Enter a Folder",placeholder_text_color=bright_colors[0],
                                         corner_radius=corner, height=100, width=600, fg_color=color_scheme, text_color=bright_colors[5],
                                         border_color=bright_colors[2], border_width=border, font=(window_font, (window_font_size + 20)))
            self.folder_entry.grid(row=1, column=0, padx=30, pady=10)
            """ Frame For Buttons """
            self.frame_5 = CTkFrame(self.user_home_window, fg_color=color_scheme, width=200)
            self.frame_5.grid(row=1, column=1, pady=10, padx=10)
            """ Buttons For Reading And Create """
            create_folder = CTkButton(self.frame_5, text="Create", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                      corner_radius=corner, hover_color=bright_colors[2], command=self.create_dir)
            create_folder.place(relx=0.01, rely=0.2)
            read_folder = CTkButton(self.frame_5, text="Read", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[4],
                                      corner_radius=corner, hover_color=bright_colors[2],
                                    command=lambda: self.increase_button("Show new user files", username))
            read_folder.place(relx=0.01, rely=0.55)
        self.user_home_window.mainloop()


    def get_database(self):

        """ Reading Database """
        database_content = open_file(usage_database_file)
        if database_content is None:
            return None
        # Return A List of Lists Containing Our Data
        return database_content


    def get_user_data(self, username):

        """ Getting User Data """
        data = self.get_database()
        if data is None:
            return None, None
        # If Data Was Fine, Then Loop Through The Data
        for line in data:
            database_username, database_folder_path, last_session = line[0].split(",")
            # If User Is Found, Then Return Their Database Folder Path And Last Session
            if database_username == username:
                return database_folder_path, last_session
        # If Not Found, Return None
        return None, None


    def create_dir(self):

        """ Get User Folder To Create It """
        folder_path = str(self.folder_entry.get())
        try:
            # If '/' Not In Folder Path, Then We Will Create It At Desktop
            if '/' not in folder_path:
                # Getting Home Path For The System
                home_dir = Path.home()
                home_desktop_dir = home_dir / "Desktop"
                new_dir = f"{home_desktop_dir}/{str(folder_path)}"
                # Checking For Errors Like Empty String And If Folder Already Exists
                if os.path.exists(str(new_dir)) or not str(new_dir):
                    label = CTkLabel(self.user_home_window, text="Error Creating Folder",
                                     font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                    label.place(rely=0.87, relx=0.4)
                    try: self.user_home_window.after(1000, label.destroy)
                    except tkinter.TclError: return None
                    return None
                else:
                    # No Errors Hence Make New Directory
                    try:
                        os.mkdir(str(new_dir))
                    # Any Exception Here, Is An Error
                    except Exception:
                        return None
                    label = CTkLabel(self.user_home_window, text="Success Creating Folder",
                                     font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[3])
                    label.place(rely=0.87, relx=0.4)
                    try: self.user_home_window.after(1000, label.destroy)
                    except tkinter.TclError: return None
                    return 0
            # If User Entered A Good Folder Path, We Just Check If It Exists Or Not Empty
            elif os.path.exists(folder_path) or not folder_path:
                label = CTkLabel(self.user_home_window, text="Error Creating Folder",
                                 font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.87, relx=0.4)
                try: self.user_home_window.after(1000, label.destroy)
                except tkinter.TclError: return None
                return None
            # If Absolute Path Is Received And Checked, Then Create A File At That Location
            else:
                try:
                    os.mkdir(folder_path)
                # Any Exception, Is An Error
                except Exception:
                    return None
                label = CTkLabel(self.user_home_window, text="Success Creating Folder",
                                 font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[3])
                label.place(rely=0.87, relx=0.4)
                try: self.user_home_window.after(1000, label.destroy)
                except tkinter.TclError: return None
                return 0
        # Any Exception, Is An Error
        except Exception:
            label = CTkLabel(self.user_home_window, text="Error Creating Folder",
                             font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
            label.place(rely=0.87, relx=0.4)
            try: self.user_home_window.after(1000, label.destroy)
            except tkinter.TclError: return None
            return None


    def start_DNA_analysis(self, filename):

        """ Validating File """
        if validate_file(filename) == 0:
            DNA_label_entry = CTkEntry(self.user_home_window, placeholder_text="Enter Read Index",
                                 font=(window_font, (window_font_size - 10)), fg_color=color_scheme, text_color=bright_colors[5],
                                 height=30, width=300, border_width=border, border_color=bright_colors[2],
                                 placeholder_text_color=bright_colors[0])
            DNA_label_entry.place(rely=0.915, relx=0.09)
            seq_type_entry = CTkEntry(self.user_home_window, placeholder_text="Enter DNA or RNA",
                                       font=(window_font, (window_font_size - 10)), fg_color=color_scheme, text_color=bright_colors[5],
                                       height=30, width=300, border_width=border, border_color=bright_colors[2],
                                       placeholder_text_color=bright_colors[0])
            seq_type_entry.place(rely=0.915, relx=0.45)
            submit_DNA_label_button = CTkButton(self.user_home_window, text="Submit", font=(window_font, (window_font_size - 5)),
                                      text_color=bright_colors[4], corner_radius=corner, fg_color=color_scheme, hover_color=bright_colors[2],
                                      command=lambda: DNA_analysis(filename, str(DNA_label_entry.get()), str(seq_type_entry.get()).upper(), self.user_home_window, self.username, self.firstname, self.lastname, User_Home))
            submit_DNA_label_button.place(rely=0.915, relx=0.8)
            return
        # If File Is Invalid, Show Error
        else:
            warning_2 = CTkLabel(self.user_home_window, text="File Problem", font=(window_font, window_font_size), fg_color=color_scheme,
                                 text_color=bright_colors[1])
            warning_2.place(rely=0.87, relx=0.4)
            try: self.user_home_window.after(1000, warning_2.destroy)
            except tkinter.TclError: return
            return


    def increase_button(self, button, username):

        """ Button Manager """
        button_system[button] += 1

        """ Assessing Buttons """
        if button == "Show new user files" and button_system[button] > 0:
            """ Displaying Folder Files For New User """
            # Since Read Button Is Pressed, Get What The User Claims Is A Folder Path
            # Try To Open That Folder Path
            folder_path_files_1 = open_folder(str(self.folder_entry.get()))
            # If It Is Not A Folder, Then Show Error And Return
            if folder_path_files_1 is None:
                warning_1 = CTkLabel(self.user_home_window, text="Folder Problem", font=(window_font, window_font_size), fg_color=color_scheme,
                                   text_color=bright_colors[1])
                warning_1.place(rely=0.87, relx=0.4)
                try: self.user_home_window.after(1000, warning_1.destroy)
                except tkinter.TclError: return
                return
            # Counter For The Folder Files Limit
            folder_files_limit_2 = 0
            # If User Folder Path Is Right, Then Reconfirm If It Is Indeed And Check If It Has The '/'
            if os.path.isdir(str(self.folder_entry.get())) and str(self.folder_entry.get()).find("/") != -1:
                """ Put Folder Path Into Usage Database """
                insert_folder_path(usage_database_file, username, str(self.folder_entry.get()))
                """ Viewport Controllers """
                # Arrows For Left And Right Navigation
                end_label_1 = CTkButton(self.user_home_window, text="<", font=(window_font, window_font_size),
                                        fg_color=color_scheme,
                                        text_color=bright_colors[4], hover_color=color_scheme,
                                        corner_radius=corner,
                                        command=lambda: self.increase_button("Show Additional Files-", username))
                end_label_1.grid(row=2, column=0, padx=10, sticky='news')
                end_label_2 = CTkButton(self.user_home_window, text=">", font=(window_font, window_font_size),
                                        fg_color=color_scheme,
                                        text_color=bright_colors[4], hover_color=color_scheme,
                                        corner_radius=corner,
                                        command=lambda: self.increase_button("Show Additional Files+", username))
                end_label_2.grid(row=2, column=1, padx=10, sticky='news')
                # Label To Show Location In Navigation
                self.location_label = CTkLabel(self.user_home_window, text=f"", font=(window_font, window_font_size),
                                          fg_color=color_scheme, text_color=text_color)
                self.location_label.place(relx=0.5, rely=0.45)
                """ Frame For Displaying The Files """
                self.frame_3_1 = CTkScrollableFrame(self.user_home_window, scrollbar_button_color=bright_colors[3],
                                           fg_color=bright_colors[3], scrollbar_button_hover_color=bright_colors[3],
                                           scrollbar_fg_color=bright_colors[3], corner_radius=corner,
                                           height=300, width=(self.user_home_window.winfo_width() - 40))
                self.frame_3_1.place(rely=0.5, relx=0.010)
                """ Displaying The Files In The Folder From User """
                for file in folder_path_files_1:
                    # Check First If View Limit Is Reached
                    if folder_files_limit_2 == view_limit:
                        break
                    path_start_index = self.folder_entry.get().rindex('/') + 1
                    file_label = CTkButton(self.frame_3_1, text=f"{str(self.folder_entry.get()[path_start_index:])}/{str(file)}", font=(window_font, window_font_size), fg_color=color_scheme,
                                           text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                           command=lambda f='/'+file: self.start_DNA_analysis(str(self.folder_entry.get())+str(f)))
                    file_label.pack(anchor='w', pady=5)
                    folder_files_limit_2 += 1
                return


        elif button == "Show Additional Files+" and button_system[button] > 0:

            # Recalling To Get The New Folder Path
            new_folder_path_1, last_session = self.get_user_data(username)
            if new_folder_path_1 is None or last_session is None:
                return
            # Using That New Folder Path To Reopen Folder
            new_folder_path_files_1 = open_folder(str(new_folder_path_1))
            if new_folder_path_files_1 is None:
                return
            # If The Stop Is Less Than Files In Folder, Increment Till The End Hence Showing Forward Files
            if self.folder_stop < len(new_folder_path_files_1):
                self.folder_start += view_limit
                self.folder_stop += view_limit
                try: self.location_label.configure(text=f"{(self.folder_start // view_limit) + 1}/{math.ceil(len(new_folder_path_files_1) / view_limit)}")
                except tkinter.TclError: return
            try:
                # Clear Frame
                for widget_2 in self.frame_3_1.winfo_children():
                    widget_2.destroy()
            except tkinter.TclError:
                return
            # Show The Files
            if new_folder_path_1 is not None:
                for file in new_folder_path_files_1[self.folder_start: self.folder_stop]:
                    file_label = CTkButton(self.frame_3_1,
                                           text=f"{str(new_folder_path_1)[str(new_folder_path_1).rfind('/')+1:]}/{str(file)}",
                                           font=(window_font, window_font_size), fg_color=color_scheme,
                                           text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                           command=lambda f='/' + file: self.start_DNA_analysis(str(new_folder_path_1) + str(f)))
                    file_label.pack(anchor='w', pady=5)
                return


        elif button == "Show Additional Files-" and button_system[button] > 0:

            # Recalling To Get The New Folder Path
            new_folder_path_2, last_session = self.get_user_data(username)
            if new_folder_path_2 is None or last_session is None:
                return
            # Using That New Folder Path To Reopen Folder
            new_folder_path_files_2 = open_folder(str(new_folder_path_2))
            if new_folder_path_files_2 is None:
                return
            # If Start Is Getting Greater Than Or Equal To, Then Subtract Back Hence Showing Previous Files
            if self.folder_start >= view_limit:
                self.folder_start -= view_limit
                self.folder_stop -= view_limit
                try: self.location_label.configure(text=f"{int(self.folder_start/view_limit)+1}/{math.ceil(len(new_folder_path_files_2)/view_limit)}")
                except tkinter.TclError: return
            try:
                # Clear Frame
                for widget_2 in self.frame_3_1.winfo_children():
                    widget_2.destroy()
            except tkinter.TclError:
                return
            # Show The Files
            if new_folder_path_2 is not None:
                for file in new_folder_path_files_2[self.folder_start: self.folder_stop]:
                    file_label = CTkButton(self.frame_3_1,
                                           text=f"{str(new_folder_path_2)[str(new_folder_path_2).rfind('/')+1:]}/{str(file)}",
                                           font=(window_font, window_font_size), fg_color=color_scheme,
                                           text_color=bright_colors[4], hover_color=bright_colors[2], corner_radius=corner,
                                           command=lambda f='/' + file: self.start_DNA_analysis(str(new_folder_path_2) + str(f)))
                    file_label.pack(anchor='w', pady=5)
                return