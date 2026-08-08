from interface.GUI_makers import *
from interface.GUI_methods import *
from interface.GUI_attr import button_system
from customtkinter import *
from tkinter import *
import datetime


class App:

    """ Home Page """

    def __init__(self):

        """ Making Window """

        self.window = Tk()
        self.window.title("DNAGenre")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.config(bg=f"{color_scheme}")
        self.window.eval("tk::PlaceWindow . center")
        self.window.resizable(False, False)
        """ Designing The Home Page """
        label_1 = CTkLabel(self.window, text='', font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[5])
        label_1.place(rely=0.5,relx=0.45)
        # Animating Words
        animate_words(self.window, "DNAGenre", label_1)
        """ Start Button """
        button = CTkButton(self.window, text="Get Started", font=(window_font, window_font_size), fg_color=color_scheme,
                           text_color=text_color, hover_color=bright_colors[2], corner_radius=corner, command=lambda: self.increase_button("Start"))
        button.place(rely=0.6, relx=0.443)
        """ Copyright """
        copy_right = CTkLabel(self.window, text=f"© {datetime.datetime.now().year}"
                              if len(str(datetime.datetime.now().year)) <= string_threshold
                              else f"© {str(datetime.datetime.now().year)[:string_threshold]}...",
                              font=(window_font, (window_font_size - 10)), fg_color=color_scheme, text_color=bright_colors[5])
        copy_right.place(rely=0.95, relx=0.485)
        self.window.mainloop()


    def increase_button(self, button):

        """ Managing The Button System """

        button_system[button] += 1

        """ Login Page """
        if button == "Start" and button_system["Start"] > 0:
            user_info_key, user_usage_key, user_code_key = str(), str(), str()
            # Get Key For User Information File
            try:
                with open(user_info_key_file, "rb") as file:
                    user_info_key = file.read()
            except FileNotFoundError:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7,relx=0.40)
                self.window.after(1000, label.destroy)
                return
            except Exception:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            # Get Key For User Usage File
            try:
                with open(user_usage_key_file, "rb") as file:
                    user_usage_key = file.read()
            except FileNotFoundError:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            except Exception:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            # Get Key For User Code File
            try:
                with open(user_code_key_file, "rb") as file:
                    user_code_key = file.read()
            except FileNotFoundError:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            except Exception:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            # Skip File Headers Inside Files With Decryption Keys
            new_user_info_key, new_user_usage_key, new_user_code_key = user_info_key[4:], user_usage_key[4:], user_code_key[4:]
            # Decrypt All Three Files
            if decrypt(user_database_file, user_info_key_file, new_user_info_key) is None:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            if decrypt(usage_database_file, user_usage_key_file, new_user_usage_key) is None:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            if decrypt(user_code_file, user_code_key_file, new_user_code_key) is None:
                label = CTkLabel(self.window, text="Decryption Failed", font=(window_font, window_font_size), fg_color=color_scheme, text_color=bright_colors[1])
                label.place(rely=0.7, relx=0.40)
                self.window.after(1000, label.destroy)
                return
            # Destroy Window And Call Next Window
            try: self.window.destroy()
            except tkinter.TclError: return
            User_Credential_Page()



if color_scheme == 'white':
    for i in range(len(bright_colors)):
        bright_colors[i] = dull_colors[i]

if __name__ == "__main__":
    App()

    """ Encrypt All Three Files """

    # Encrypt user_database.db
    encrypt(user_database_file, user_info_key_file)
    # Encrypt usage_database.db
    encrypt(usage_database_file, user_usage_key_file)
    # Encrypt user_code.txt
    encrypt(user_code_file, user_code_key_file)