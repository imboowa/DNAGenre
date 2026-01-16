import math
import statistics
from DNAtoolkit.DNAtools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import interface
from interface.GUI_methods import *
from user_app.user_script import *


class Requirements_1:

    def __init__(self, username, firstname, lastname, filename, DNA_data, seq_type, next_window, menu_window, signing_window):

        # Useful Variables
        self.DNA_data = DNA_data
        self.seq_type = seq_type
        # Window
        self.window = Tk()
        self.window.config(bg=color_scheme)
        self.window.title(f"{str(filename)[str(filename).rindex('/')+1:]}..." if len(str(filename)[str(filename).rindex('/')+1:]) > string_threshold else f"{str(filename)[str(filename).rindex('/')+1:]}")
        self.window.geometry(f"1080x{self.window.winfo_screenheight()}")
        self.window.propagate(True)
        self.window.eval("tk::PlaceWindow . center")
        self.window.resizable(False, False)
        """ Frame For Deep Analysis """
        self.mother_frame = CTkScrollableFrame(self.window, fg_color=color_scheme, scrollbar_fg_color=color_scheme,
                                               scrollbar_button_color=color_scheme, scrollbar_button_hover_color=color_scheme)
        self.mother_frame.pack(fill='both', expand=True)
        """ Sequence Length """
        self.seq_len = CTkLabel(self.mother_frame, text="", font=(window_font, (window_font_size - 10)),
                                fg_color=color_scheme, text_color=bright_colors[5])
        self.seq_len.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        # Calculating The Sequence Length
        total_len = 0
        for i in DNA_data.values():
            total_len += len(i)
        try: self.seq_len.configure(text=f"Seq(s) Length {total_len:.3e}" if len(str(total_len)) > number_threshold else f"Seq(s) Length {total_len:,}",
                               fg_color=bright_colors[5], text_color=color_scheme, corner_radius=corner)
        except tkinter.TclError: return
        """ Nuc Count """
        self.nuc_count = CTkLabel(self.mother_frame, text=f"Nucleotide Count", font=(window_font, window_font_size),
                                  fg_color=color_scheme, text_color=bright_colors[5])
        self.nuc_count.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        """ Script Button """
        script_label_button = CTkButton(self.mother_frame, text="Script", font=(window_font, window_font_size),
                                        text_color=bright_colors[4], corner_radius=corner, fg_color=bright_colors[2],
                                        hover_color=bright_colors[2],
                                        command=lambda: User_Script(filename, DNA_data, username,
                                                                    firstname, lastname, self.window, menu_window, signing_window))
        script_label_button.place(relx=0.35, rely=0.055)
        # Frame For Nucleotide Count
        self.framer_1 = CTkFrame(self.mother_frame, fg_color=color_scheme)
        self.framer_1.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        # Calculating Nucleotide Count
        DNA_count = countNucFrequency("".join(DNA_data.values()), seq_type)
        if DNA_count != -1 and DNA_count != -2:
            # Figure For Nucleotide Count
            fig_1 = Figure(figsize=(5,4), dpi=100)
            plot_1 = fig_1.add_subplot(111)
            plot_1.set_title("Nucleotide Count")
            plot_1.set_ylabel("Count")
            plot_1.set_xlabel("Nucleotides")
            plot_1.bar(DNA_count.keys(), DNA_count.values())
            # Put In Canvas
            canvas_1 = FigureCanvasTkAgg(fig_1, master=self.framer_1)
            canvas_1.get_tk_widget().grid(row=2, column=0, sticky='w', padx=5, pady=5)
            canvas_1.draw()
        """ Frame For Word Analysis On Nucleotide Count """
        self.frame_1 = CTkScrollableFrame(self.mother_frame, scrollbar_button_hover_color=bright_colors[3],
                                          scrollbar_fg_color=bright_colors[3], scrollbar_button_color=bright_colors[3],
                                          fg_color=bright_colors[3])
        self.frame_1.grid(row=3, column=0, sticky='news', padx=5, pady=5)
        """ Mean, Median, Mode, Range """
        if DNA_count != -1 and DNA_count != -2:
            nuc_count_mean = round(float(total_len / len(DNA_count.keys())), 3) if total_len > 0 else 0.0
            nuc_count_median = statistics.median(DNA_count.values())
            nuc_count_mode = statistics.mode(DNA_count.values())
            nuc_count_range = max(DNA_count.values()) - min(DNA_count.values())
            mean_label = CTkLabel(self.frame_1, text=f"Mean Nuc Count {nuc_count_mean:.3e}" if len(str(nuc_count_mean)) > number_threshold else f"Mean Nuc Count: {nuc_count_mean:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            mean_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
            median_label = CTkLabel(self.frame_1, text=f"Median Nuc Count {nuc_count_median:.3e}" if len(str(nuc_count_median)) > number_threshold else f"Median Nuc Count: {nuc_count_median:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            median_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
            mode_label = CTkLabel(self.frame_1, text=f"Mode Nuc Count {nuc_count_mode:.3e}" if len(str(nuc_count_mode)) > number_threshold else f"Mode Nuc Count: {nuc_count_mode:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            mode_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
            range_label = CTkLabel(self.frame_1, text=f"Range Nuc Count {nuc_count_range:.3e}\n" if len(str(nuc_count_range)) > number_threshold else f"Range Nuc Count: {nuc_count_range:,}\n",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            range_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
            nuc_count_label = CTkLabel(self.frame_1, text=''.join({f"{key}: {value:.3e}\n" if len(str(value)) > number_threshold else f"{key}: {value:,}\n" for key, value in DNA_count.items()}), font=(window_font, (window_font_size - 10)),
                                       fg_color=bright_colors[3], text_color=color_scheme, corner_radius=corner)
            nuc_count_label.grid(row=4, column=0, sticky='w', pady=5, padx=5)
            """ Percentages """
            # AC Percent
            ac_total = 0
            for i in DNA_data.values():
                ac_total += str(i).count("A") + str(i).count("C")
            overall_ac_percent = float((ac_total / total_len) * 100) if total_len > 0 else 0.0
            AC_percent = CTkLabel(self.frame_1, text=f"AC: {round(overall_ac_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            AC_percent.grid(row=5, column=0, sticky='w', padx=5, pady=5)
            # AT Percent
            at_total = 0
            au_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    at_total += str(i).count("A") + str(i).count("T")
                overall_at_percent = float((at_total / total_len) * 100) if total_len > 0 else 0.0
                AT_percent = CTkLabel(self.frame_1, text=f"AT: {round(overall_at_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                AT_percent.grid(row=6, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    au_total += str(i).count("A") + str(i).count("U")
                overall_au_percent = float((au_total / total_len) * 100) if total_len > 0 else 0.0
                AU_percent = CTkLabel(self.frame_1, text=f"AU: {round(overall_au_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                AU_percent.grid(row=6, column=0, sticky='w', padx=5, pady=5)
            # AG Percent
            ag_total = 0
            for i in DNA_data.values():
                ag_total += str(i).count("A") + str(i).count("G")
            overall_ag_percent = float((ag_total / total_len) * 100) if total_len > 0 else 0.0
            AG_percent = CTkLabel(self.frame_1, text=f"AG: {round(overall_ag_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            AG_percent.grid(row=7, column=0, sticky='w', padx=5, pady=5)
            # CT Percent
            ct_total = 0
            cu_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    ct_total += str(i).count("C") + str(i).count("T")
                overall_ct_percent = float((ct_total / total_len) * 100) if total_len > 0 else 0.0
                CT_percent = CTkLabel(self.frame_1, text=f"CT: {round(overall_ct_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                CT_percent.grid(row=8, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    cu_total += str(i).count("C") + str(i).count("U")
                overall_cu_percent = float((cu_total / total_len) * 100) if total_len > 0 else 0.0
                CU_percent = CTkLabel(self.frame_1, text=f"CU: {round(overall_cu_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                CU_percent.grid(row=8, column=0, sticky='w', padx=5, pady=5)
            # CG Percent
            cg_total = 0
            for i in DNA_data.values():
                cg_total += str(i).count("C") + str(i).count("G")
            overall_cg_percent = float((cg_total / total_len) * 100) if total_len > 0 else 0.0
            CG_percent = CTkLabel(self.frame_1, text=f"CG: {round(overall_cg_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            CG_percent.grid(row=9, column=0, sticky='w', padx=5, pady=5)
            # TG Percent
            tg_total = 0
            ug_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    tg_total += str(i).count("T") + str(i).count("G")
                overall_tg_percent = float((tg_total / total_len) * 100) if total_len > 0 else 0.0
                TG_percent = CTkLabel(self.frame_1, text=f"TG: {round(overall_tg_percent, rounder)}%",
                                      font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                TG_percent.grid(row=10, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    ug_total += str(i).count("U") + str(i).count("G")
                overall_tu_percent = float((ug_total / total_len) * 100) if total_len > 0 else 0.0
                TU_percent = CTkLabel(self.frame_1, text=f"UG: {round(overall_tu_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                TU_percent.grid(row=10, column=0, sticky='w', padx=5, pady=5)
        """ Frame For Word Analysis On Nucleotide Count """
        self.frame_3 = CTkScrollableFrame(self.mother_frame, scrollbar_button_hover_color=bright_colors[3],
                                          scrollbar_fg_color=bright_colors[3], scrollbar_button_color=bright_colors[3],
                                          fg_color=bright_colors[3],width=(self.window.winfo_width() - (self.frame_1.winfo_width() + 570)))
        self.frame_3.place(relx=0.5, rely=0.01)
        """ Adding GC Per Subsequence Into Graph """
        # Calculating GC Per Key In The File
        gc_per_subseq = dict()
        for key, value in list(DNA_data.items())[:view_limit]:
            gc_result = gc_content(str(value))
            if gc_result != -1:
                gc_per_subseq[key] = round(gc_result, rounder)
        # Making A Graph
        self.framer_2 = CTkFrame(self.frame_3, fg_color=color_scheme)
        self.framer_2.pack(fill='both')
        # The Graph
        fig_2 = Figure(figsize=(5,4), dpi=100)
        self.plot_2 = fig_2.add_subplot(111)
        self.plot_2.set_xlabel("Read Indexes")
        self.plot_2.set_ylabel("GC Percentage(s)")
        self.plot_2.set_title("GC Percent Per Read Index")
        self.plot_2.plot(gc_per_subseq.keys(), gc_per_subseq.values(), c=bright_colors[4], marker='o')
        self.canvas_2 = FigureCanvasTkAgg(fig_2, master=self.framer_2)
        self.canvas_2.draw()
        self.canvas_2.get_tk_widget().pack(fill='both',expand=True)
        """ Navigate Buttons Frame """
        self.frame_4 = CTkFrame(self.frame_3, fg_color=bright_colors[3])
        self.frame_4.pack(fill='both')
        # Useful Variables For Navigation Only On The graph_left_1 And graph_right_1
        self.forward_1, self.backward_1 = view_limit, 0
        # Navigate Buttons
        graph_left_1 = CTkButton(self.frame_4, text="<", fg_color=bright_colors[3], text_color=bright_colors[4],
                                hover_color=bright_colors[3], font=(window_font, window_font_size), command=lambda: self.increase_button("Graph Left 1"))
        graph_left_1.pack(side='left')
        self.tracker_label_1 = CTkLabel(self.frame_4, text=f"", font=(window_font, window_font_size), fg_color=bright_colors[3], text_color=bright_colors[5])
        self.tracker_label_1.place(relx=0.45, rely=0.0)
        graph_right_1 = CTkButton(self.frame_4, text=">", fg_color=bright_colors[3], text_color=bright_colors[4],
                               hover_color=bright_colors[3], font=(window_font, window_font_size), command=lambda: self.increase_button("Graph Right 1"))
        graph_right_1.pack(side='right')
        """ Adding AT Per Sub Sequence Into Graph """
        # Calculating AT Per Read Index
        at_per_subseq = dict()
        for key, value in list(DNA_data.items())[:view_limit]:
            at_result = at_content(str(value), seq_type)
            if at_result != -1 and at_result != -2:
                at_per_subseq[key] = round(at_result, rounder)
        # Making A Graph
        self.framer_3 = CTkFrame(self.frame_3, fg_color=color_scheme)
        self.framer_3.pack(fill='both')
        # The Graph
        fig_3 = Figure(figsize=(5,4), dpi=100)
        self.plot_3 = fig_3.add_subplot(111)
        self.plot_3.set_title("AT Percent Per Read Index" if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percent Per Read Index")
        self.plot_3.set_ylabel("AT Percentage(s)" if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percentage(s)")
        self.plot_3.set_xlabel("Read Indexes")
        self.plot_3.plot(at_per_subseq.keys(), at_per_subseq.values(), c=bright_colors[1], marker='o')
        self.canvas_3 = FigureCanvasTkAgg(fig_3, master=self.framer_3)
        self.canvas_3.draw()
        self.canvas_3.get_tk_widget().pack(fill='both', expand=True)
        """ Navigate Buttons Frame """
        self.frame_5 = CTkFrame(self.frame_3, fg_color=bright_colors[3])
        self.frame_5.pack(fill='both')
        # Useful Variables For Navigation Only On The graph_left_2 And graph_right_2
        self.forward_2, self.backward_2 = view_limit, 0
        # Navigate Buttons
        graph_left_2 = CTkButton(self.frame_5, text="<", fg_color=bright_colors[3], text_color=bright_colors[4],
                                 hover_color=bright_colors[3], font=(window_font, window_font_size), command=lambda: self.increase_button("Graph Left 2"))
        graph_left_2.pack(side='left')
        self.tracker_label_2 = CTkLabel(self.frame_5, text=f"",font=(window_font, window_font_size), fg_color=bright_colors[3],text_color=bright_colors[5])
        self.tracker_label_2.place(relx=0.45, rely=0.0)
        graph_right_2 = CTkButton(self.frame_5, text=">", fg_color=bright_colors[3], text_color=bright_colors[4],
                                 hover_color=bright_colors[3], font=(window_font, window_font_size), command=lambda: self.increase_button("Graph Right 2"))
        graph_right_2.pack(side='right')
        """ Probability """
        CTkLabel(self.frame_3, text="Probability", font=(window_font, (window_font_size - 10), font_style), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        A_probability = CTkLabel(self.frame_3, text=f"P(A): {round((DNA_count['A']/total_len), rounder)}" if total_len > 0 else f"P(A): 0.0", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        A_probability.pack(anchor='w', padx=5, pady=5)
        if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
            T_probability = CTkLabel(self.frame_3, text=f"P(T): {round((DNA_count['T']/total_len), rounder)}" if total_len > 0 else f"P(T): 0.0", text_color=color_scheme,
                                    fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
            T_probability.pack(anchor='w', padx=5, pady=5)
        elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
            U_probability = CTkLabel(self.frame_3, text=f"P(U): {round((DNA_count["U"]/total_len), rounder)}" if total_len > 0 else f"P(U): 0.0", text_color=color_scheme,
                                     fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
            U_probability.pack(anchor='w', padx=5, pady=5)
        G_probability = CTkLabel(self.frame_3, text=f"P(G): {round((DNA_count["G"]/total_len), rounder)}" if total_len > 0 else f"P(G): 0.0", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        G_probability.pack(anchor='w', padx=5, pady=5)
        C_probability = CTkLabel(self.frame_3, text=f"P(C): {round((DNA_count["C"]/total_len), rounder)}" if total_len > 0 else f"P(C): 0.00", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        C_probability.pack(anchor='w', pady=5, padx=5)
        """ Probabilities """
        CTkLabel(self.frame_3, text=f"P(Sequence Start is A): {round(len(list(filter(lambda x: x[0] == "A", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence Start is T): {round(len(list(filter(lambda x: x[0] == "T", DNA_data.values())))/len(DNA_data.values()), rounder)}"
                 if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else f"P(Sequence Start is U): {round(len(list(filter(lambda x: x[0] == "U", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence Start is G): {round(len(list(filter(lambda x: x[0] == "G", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence Start is C): {round(len(list(filter(lambda x: x[0] == "C", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)

        CTkLabel(self.frame_3, text=f"P(Sequence End is A): {round(len(list(filter(lambda x: x[-1] == "A", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence End is T): {round(len(list(filter(lambda x: x[-1] == "T", DNA_data.values())))/len(DNA_data.values()), rounder)}"
                 if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else f"P(Sequence End is U): {round(len(list(filter(lambda x: x[0] == "U", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence End is G): {round(len(list(filter(lambda x: x[-1] == "G", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        CTkLabel(self.frame_3, text=f"P(Sequence End is C): {round(len(list(filter(lambda x: x[-1] == "C", DNA_data.values())))/len(DNA_data.values()), rounder)}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        """ Frame For The Navigation Buttons """
        self.frame_6 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_6.pack(fill='both', side='bottom')
        """ Navigation Buttons """
        button_left = CTkButton(self.frame_6, text="Back", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=color_scheme, font=(window_font, window_font_size), command=lambda: self.call_menu_window(username, firstname, lastname, signing_window, menu_window))
        button_left.pack(side="left")
        button_right = CTkButton(self.frame_6, text="Next", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=color_scheme,font=(window_font, window_font_size), command=lambda: next_window(username, firstname, lastname, self.window, DNA_data, menu_window, seq_type, menu_window, filename, signing_window, from_requirements=True))
        button_right.pack(side="right")
        try:
            # Configure The Height Since It Depends On The Navigation Height
            self.frame_3.configure(height=(self.window.winfo_height() - (self.frame_6.winfo_height() + 145)))
        except tkinter.TclError: return
        self.window.mainloop()


    def call_menu_window(self, username, firstname, lastname, signing_window, menu):

        """ Calling Menu Window """

        # A Tip On App Usage
        if interface.GUI_attr.tip_switch == 0:
            frame_1 = CTkFrame(self.window, fg_color=bright_colors[5], width=100, height=5)
            frame_1.place(relx=0.36, rely=0.9)
            tip_off = CTkLabel(self.window, text_color=text_color, text="Tip: " + str(tips[3]),
                               fg_color=color_scheme, font=(window_font, (window_font_size - 10)))
            tip_off.place(relx=0.215, rely=0.865)
            custom_progressbar_tips(self.window, frame_1, color_scheme, tip_off)
            interface.GUI_attr.tip_switch = 1
            return
        try: self.window.destroy()
        except tkinter.TclError: return
        menu(username, firstname, lastname, signing_window)


    def increase_button(self, button):

        """ Manage Button System  """

        button_system[button] += 1

        # The Graph Cannot Show Long X Values, Need Explanation Here
        if button == "Graph Left 1" and button_system[button] > 0:
            if self.backward_1 >= view_limit:
                self.forward_1 -= view_limit
                self.backward_1 -= view_limit
                try: self.tracker_label_1.configure(text=f"{(self.backward_1 // view_limit) + 1}/{math.ceil(len(self.DNA_data.keys()) / view_limit)}")
                except tkinter.TclError: return
                gc_content_subseq_1 = dict()
                for key, value in list(self.DNA_data.items())[self.backward_1: self.forward_1]:
                    gc_result = gc_content(str(value))
                    if gc_result != -1:
                        gc_content_subseq_1[key] = round(gc_result, rounder)
                self.plot_2.cla()
                self.plot_2.set_xlabel("Read Indexes")
                self.plot_2.set_ylabel("GC Percentage(s)")
                self.plot_2.set_title("GC Percent Per Read Index")
                self.plot_2.plot(gc_content_subseq_1.keys(), gc_content_subseq_1.values(), c=bright_colors[4], marker='o')
                self.canvas_2.draw()

        elif button == "Graph Right 1" and button_system[button] > 0:
            if self.forward_1 < len(self.DNA_data.keys()):
                self.forward_1 += view_limit
                self.backward_1 += view_limit
                try: self.tracker_label_1.configure(text=f"{(self.backward_1 // view_limit) + 1}/{math.ceil(len(self.DNA_data.keys()) / view_limit)}")
                except tkinter.TclError: return
                gc_content_subseq_2 = dict()
                for key, value in list(self.DNA_data.items())[self.backward_1: self.forward_1]:
                    gc_result = gc_content(str(value))
                    if gc_result != -1:
                        gc_content_subseq_2[key] = round(gc_result, rounder)
                self.plot_2.cla()
                self.plot_2.set_xlabel("Read Indexes")
                self.plot_2.set_ylabel("GC Percentage(s)")
                self.plot_2.set_title("GC Percent Per Read Index")
                self.plot_2.plot(gc_content_subseq_2.keys(), gc_content_subseq_2.values(), c=bright_colors[4], marker='o')
                self.canvas_2.draw()

        elif button == "Graph Right 2" and button_system[button] > 0:
            if self.forward_2 < len(self.DNA_data.keys()):
                self.forward_2 += view_limit
                self.backward_2 += view_limit
                try: self.tracker_label_2.configure(text=f"{(self.backward_2 // view_limit) + 1}/{math.ceil(len(self.DNA_data.keys()) / view_limit)}")
                except tkinter.TclError: return
                at_content_subseq_1 = dict()
                for key, value in list(self.DNA_data.items())[self.backward_2: self.forward_2]:
                    at_result = at_content(str(value), self.seq_type)
                    if at_result != -1 and at_result != -2:
                        at_content_subseq_1[key] = round(at_result, rounder)
                self.plot_3.cla()
                self.plot_3.set_title("AT Percent Per Read Index" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percent Per Read Index")
                self.plot_3.set_ylabel("AT Percentage(s)" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percentage(s)")
                self.plot_3.set_xlabel("Read Indexes")
                self.plot_3.plot(at_content_subseq_1.keys(), at_content_subseq_1.values(), c=bright_colors[1], marker='o')
                self.canvas_3.draw()

        elif button == "Graph Left 2" and button_system[button] > 0:
            if self.backward_2 >= view_limit:
                self.forward_2 -= view_limit
                self.backward_2 -= view_limit
                try: self.tracker_label_2.configure(text=f"{(self.backward_2 // view_limit) + 1}/{math.ceil(len(self.DNA_data.keys()) / view_limit)}")
                except tkinter.TclError: return
                at_content_subseq_2 = dict()
                for key, value in list(self.DNA_data.items())[self.backward_2: self.forward_2]:
                    at_result = at_content(str(value), self.seq_type)
                    if at_result != -1 and at_result != -2:
                        at_content_subseq_2[key] = round(at_result, rounder)
                self.plot_3.cla()
                self.plot_3.set_title("AT Percent Per Read Index" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percent Per Read Index")
                self.plot_3.set_ylabel("AT Percentage(s)" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percentage(s)")
                self.plot_3.set_xlabel("Read Indexes")
                self.plot_3.plot(at_content_subseq_2.keys(), at_content_subseq_2.values(), c=bright_colors[1], marker='o')
                self.canvas_3.draw()