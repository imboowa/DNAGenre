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
            # Destroy Window And Call Next Window
            try: self.window.destroy()
            except tkinter.TclError: return
            User_Credential_Page()



if color_scheme == 'white':
    for i in range(len(bright_colors)):
        bright_colors[i] = dull_colors[i]

if __name__ == "__main__":
    App()