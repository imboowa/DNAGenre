import math
import statistics
from DNAtoolkit.DNAtools import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import interface
from interface.GUI_methods import *
from user_app.user_script import *
import json


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
        self.total_len = 0
        for i in DNA_data.values():
            self.total_len += len(i)
        try: self.seq_len.configure(text=f"Seq(s) Length {self.total_len:.3e}" if len(str(self.total_len)) > string_threshold else f"Seq(s) Length {self.total_len:,}",
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
        self.DNA_count = countNucFrequency("".join(DNA_data.values()), seq_type)
        if self.DNA_count != -1 and self.DNA_count != -2:
            # Figure For Nucleotide Count
            fig_1 = Figure(figsize=(5,4), dpi=100)
            plot_1 = fig_1.add_subplot(111)
            plot_1.set_title("Nucleotide Count")
            plot_1.set_ylabel("Count")
            plot_1.set_xlabel("Nucleotides")
            plot_1.bar(self.DNA_count.keys(), self.DNA_count.values())
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
        if self.DNA_count != -1 and self.DNA_count != -2:
            self.nuc_count_mean = round(float(self.total_len / len(self.DNA_count.keys())), 3) if self.total_len > 0 else 0.0
            self.nuc_count_median = statistics.median(self.DNA_count.values())
            self.nuc_count_mode = statistics.mode(self.DNA_count.values())
            self.nuc_count_range = max(self.DNA_count.values()) - min(self.DNA_count.values())
            mean_label = CTkLabel(self.frame_1, text=f"Mean Nuc Count: {self.nuc_count_mean:.3e}" if len(str(self.nuc_count_mean)) > string_threshold else f"Mean Nuc Count: {self.nuc_count_mean:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            mean_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
            median_label = CTkLabel(self.frame_1, text=f"Median Nuc Count: {self.nuc_count_median:.3e}" if len(str(self.nuc_count_median)) > string_threshold else f"Median Nuc Count: {self.nuc_count_median:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            median_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
            mode_label = CTkLabel(self.frame_1, text=f"Mode Nuc Count: {self.nuc_count_mode:.3e}" if len(str(self.nuc_count_mode)) > string_threshold else f"Mode Nuc Count: {self.nuc_count_mode:,}",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            mode_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
            range_label = CTkLabel(self.frame_1, text=f"Range Nuc Count: {self.nuc_count_range:.3e}\n" if len(str(self.nuc_count_range)) > string_threshold else f"Range Nuc Count: {self.nuc_count_range:,}\n",
                     text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner, font=(window_font, (window_font_size - 10)))
            range_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
            nuc_count_label = CTkLabel(self.frame_1, text=''.join({f"{key}: {value:.3e}\n" if len(str(value)) > string_threshold else f"{key}: {value:,}\n" for key, value in self.DNA_count.items()}), font=(window_font, (window_font_size - 10)),
                                       fg_color=bright_colors[3], text_color=color_scheme, corner_radius=corner)
            nuc_count_label.grid(row=4, column=0, sticky='w', pady=5, padx=5)
            """ Percentages """
            # AC Percent
            ac_total = 0
            for i in DNA_data.values():
                ac_total += str(i).count("A") + str(i).count("C")
            self.overall_ac_percent = float((ac_total / self.total_len) * 100) if self.total_len > 0 else 0.0
            AC_percent = CTkLabel(self.frame_1, text=f"AC: {round(self.overall_ac_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            AC_percent.grid(row=5, column=0, sticky='w', padx=5, pady=5)
            # AT Percent
            at_total = 0
            au_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    at_total += str(i).count("A") + str(i).count("T")
                self.overall_at_percent = float((at_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                AT_percent = CTkLabel(self.frame_1, text=f"AT: {round(self.overall_at_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                AT_percent.grid(row=6, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    au_total += str(i).count("A") + str(i).count("U")
                self.overall_au_percent = float((au_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                AU_percent = CTkLabel(self.frame_1, text=f"AU: {round(self.overall_au_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                AU_percent.grid(row=6, column=0, sticky='w', padx=5, pady=5)
            # AG Percent
            ag_total = 0
            for i in DNA_data.values():
                ag_total += str(i).count("A") + str(i).count("G")
            self.overall_ag_percent = float((ag_total / self.total_len) * 100) if self.total_len > 0 else 0.0
            AG_percent = CTkLabel(self.frame_1, text=f"AG: {round(self.overall_ag_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            AG_percent.grid(row=7, column=0, sticky='w', padx=5, pady=5)
            # CT Percent
            ct_total = 0
            cu_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    ct_total += str(i).count("C") + str(i).count("T")
                self.overall_ct_percent = float((ct_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                CT_percent = CTkLabel(self.frame_1, text=f"CT: {round(self.overall_ct_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                CT_percent.grid(row=8, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    cu_total += str(i).count("C") + str(i).count("U")
                self.overall_cu_percent = float((cu_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                CU_percent = CTkLabel(self.frame_1, text=f"CU: {round(self.overall_cu_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                CU_percent.grid(row=8, column=0, sticky='w', padx=5, pady=5)
            # CG Percent
            cg_total = 0
            for i in DNA_data.values():
                cg_total += str(i).count("C") + str(i).count("G")
            self.overall_cg_percent = float((cg_total / self.total_len) * 100) if self.total_len > 0 else 0.0
            CG_percent = CTkLabel(self.frame_1, text=f"CG: {round(self.overall_cg_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
                                  text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
            CG_percent.grid(row=9, column=0, sticky='w', padx=5, pady=5)
            # TG Percent
            tg_total = 0
            ug_total = 0
            if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
                for i in DNA_data.values():
                    tg_total += str(i).count("T") + str(i).count("G")
                self.overall_tg_percent = float((tg_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                TG_percent = CTkLabel(self.frame_1, text=f"TG: {round(self.overall_tg_percent, rounder)}%",
                                      font=(window_font, (window_font_size - 10)),
                                      text_color=color_scheme, fg_color=bright_colors[3], corner_radius=corner)
                TG_percent.grid(row=10, column=0, sticky='w', padx=5, pady=5)
            elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
                for i in DNA_data.values():
                    ug_total += str(i).count("U") + str(i).count("G")
                self.overall_ug_percent = float((ug_total / self.total_len) * 100) if self.total_len > 0 else 0.0
                TU_percent = CTkLabel(self.frame_1, text=f"UG: {round(self.overall_ug_percent, rounder)}%", font=(window_font, (window_font_size - 10)),
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
        counter_1 = 1
        for key, value in list(DNA_data.items())[:view_limit]:
            gc_result = gc_content(str(value))
            if gc_result != -1:
                gc_per_subseq[str(counter_1)] = round(gc_result, rounder)
            else:
                gc_per_subseq[str(counter_1)] = 0.00
            counter_1 += 1
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
        counter_2 = 1
        for key, value in list(DNA_data.items())[:view_limit]:
            at_result = at_content(str(value), seq_type)
            if at_result != -1 and at_result != -2:
                at_per_subseq[str(counter_2)] = round(at_result, rounder)
            else:
                at_per_subseq[str(counter_2)] = 0.00
            counter_2 += 1
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
        self.A_probability = round((self.DNA_count['A']/self.total_len), rounder) if self.total_len > 0 else 0.00
        A_probability = CTkLabel(self.frame_3, text=f"P(A): {self.A_probability}", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        A_probability.pack(anchor='w', padx=5, pady=5)
        self.T_probability = 0.00
        self.U_probability = 0.00
        if seq_type == list(NUCLEOTIDE_BASE.keys())[0]:
            self.T_probability = round((self.DNA_count['T']/self.total_len), rounder) if self.total_len > 0 else 0.00
            T_probability = CTkLabel(self.frame_3, text=f"P(T): {self.T_probability}", text_color=color_scheme,
                                    fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
            T_probability.pack(anchor='w', padx=5, pady=5)
        elif seq_type == list(NUCLEOTIDE_BASE.keys())[1]:
            self.U_probability = round((self.DNA_count["U"]/self.total_len), rounder) if self.total_len > 0 else 0.00
            U_probability = CTkLabel(self.frame_3, text=f"P(U): {self.U_probability}", text_color=color_scheme,
                                     fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
            U_probability.pack(anchor='w', padx=5, pady=5)
        self.G_probability = round((self.DNA_count["G"]/self.total_len), rounder) if self.total_len > 0 else 0.00
        G_probability = CTkLabel(self.frame_3, text=f"P(G): {self.G_probability}", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        G_probability.pack(anchor='w', padx=5, pady=5)
        self.C_probability = round((self.DNA_count["C"]/self.total_len), rounder) if self.total_len > 0 else 0.00
        C_probability = CTkLabel(self.frame_3, text=f"P(C): {self.C_probability}", text_color=color_scheme,
                                 fg_color=bright_colors[3], font=(window_font, (window_font_size - 10)))
        C_probability.pack(anchor='w', pady=5, padx=5)
        """ Probabilities """
        try: self.p_start_A = round(len(list(filter(lambda x: x[0] == "A", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_start_A = "Unobtained"
        except Exception: self.p_start_A = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence Start is A): {self.p_start_A}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_start_T_or_U = round(len(list(filter(lambda x: x[0] == "T", DNA_data.values())))/len(DNA_data.values()), rounder) if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else round(len(list(filter(lambda x: x[0] == "U", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_start_T_or_U = "Unobtained"
        except Exception: self.p_start_T_or_U = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence Start is T): {self.p_start_T_or_U}" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else f"P(Sequence Start is U): {self.p_start_T_or_U}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_start_G = round(len(list(filter(lambda x: x[0] == "G", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_start_G = "Unobtained"
        except Exception: self.p_start_G = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence Start is G): {self.p_start_G}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_start_C = round(len(list(filter(lambda x: x[0] == "C", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_start_C = "Unobtained"
        except Exception: self.p_start_C = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence Start is C): {self.p_start_C}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)

        try: self.p_end_A = round(len(list(filter(lambda x: x[-1] == "A", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_end_A = "Unobtained"
        except Exception: self.p_end_A = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence End is A): {self.p_end_A}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_end_T_or_U = round(len(list(filter(lambda x: x[-1] == "T", DNA_data.values())))/len(DNA_data.values()), rounder) if seq_type == list(NUCLEOTIDE_BASE.keys())[0] else round(len(list(filter(lambda x: x[0] == "U", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_end_T_or_U = "Unobtained"
        except Exception: self.p_end_T_or_U = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence End is T): {self.p_end_T_or_U}" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else f"P(Sequence End is U): {self.p_end_T_or_U}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_end_G = round(len(list(filter(lambda x: x[-1] == "G", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_end_G = "Unobtained"
        except Exception: self.p_end_G = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence End is G): {self.p_end_G}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        try: self.p_end_C = round(len(list(filter(lambda x: x[-1] == "C", DNA_data.values())))/len(DNA_data.values()), rounder)
        except IndexError: self.p_end_C = "Unobtained"
        except Exception: self.p_end_C = "Unobtained"
        CTkLabel(self.frame_3, text=f"P(Sequence End is C): {self.p_end_C}",
                 font=(window_font, (window_font_size - 10)), fg_color=bright_colors[3], text_color=color_scheme).pack(anchor='w', padx=5, pady=5)
        """ Frame For The Navigation Buttons """
        self.frame_6 = CTkFrame(self.window, fg_color=color_scheme)
        self.frame_6.pack(fill='both', side='bottom')
        # Sub Frames
        sub_frame_1 = CTkFrame(self.frame_6, fg_color=color_scheme)
        sub_frame_1.pack(side='left', fill="both", expand=True)
        sub_frame_2 = CTkFrame(self.frame_6, fg_color=color_scheme)
        sub_frame_2.pack(side='right', fill="both", expand=True)
        """ Navigation Buttons """
        button_left = CTkButton(sub_frame_1, text="Back", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=color_scheme, font=(window_font, window_font_size), command=lambda: self.call_menu_window(username, firstname, lastname, signing_window, menu_window))
        button_left.pack(side="left")
        self.export_button = CTkButton(sub_frame_2, text="Export", fg_color=color_scheme, text_color=bright_colors[4],
                                  hover_color=color_scheme, font=(window_font, window_font_size), command=lambda: self.export_window_data())
        self.export_button.pack(side="left")
        button_right = CTkButton(sub_frame_2, text="Next", fg_color=color_scheme, text_color=bright_colors[4],
                                hover_color=color_scheme,font=(window_font, window_font_size), command=lambda: next_window(username, firstname, lastname, self.window, DNA_data, menu_window, seq_type, menu_window, filename, signing_window, from_requirements=True))
        button_right.pack(side="right")
        try:
            # Configure The Height Since It Depends On The Navigation Height
            self.frame_3.configure(height=(self.window.winfo_height() - (self.frame_6.winfo_height() + 145)))
        except tkinter.TclError: return
        self.window.mainloop()


    def export_window_data(self):

        """ Exports Bioinformatic Data To JSON File """

        # Calculating GC Per Key In The File
        gc_per_subseq = dict()
        counter_1 = 1
        for key, value in list(self.DNA_data.items()):
            gc_result = gc_content(str(value))
            if gc_result != -1:
                gc_per_subseq[str(counter_1)] = round(gc_result, rounder)
            else:
                gc_per_subseq[str(counter_1)] = 0.00
            counter_1 += 1

        # Calculating AT/AU Per Key In The File
        at_per_subseq = dict()
        counter_2 = 1
        for key, value in list(self.DNA_data.items()):
            at_result = at_content(str(value), self.seq_type)
            if at_result != -1 and at_result != -2:
                at_per_subseq[str(counter_2)] = round(at_result, rounder)
            else:
                at_per_subseq[str(counter_2)] = 0.00
            counter_2 += 1

        bio_data = {
            "Seq(s) Length": self.total_len,
            "Nucleotide Count": self.DNA_count,
            "Mean Nuc Count": self.nuc_count_mean,
            "Median Nuc Count": self.nuc_count_median,
            "Mode Nuc Count": self.nuc_count_mode,
            "Range Nuc Count": self.nuc_count_range,
            "AC Percentage": round(self.overall_ac_percent, rounder),
            "AT Percentage": round(self.overall_at_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "AU Percentage": round(self.overall_au_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "AG Percentage": round(self.overall_ag_percent, rounder),
            "CT Percentage": round(self.overall_ct_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "CU Percentage": round(self.overall_cu_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "CG Percentage": round(self.overall_cg_percent, rounder),
            "TG Percentage": round(self.overall_tg_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "UG Percentage": round(self.overall_ug_percent, rounder) if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "GC Content Per Read Index": gc_per_subseq,
            "AT Content Per Read Index": at_per_subseq if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "AU Content Per Read Index": at_per_subseq if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "P(A)": self.A_probability,
            "P(T)": self.T_probability,
            "P(U)": self.U_probability,
            "P(G)": self.G_probability,
            "P(C)": self.C_probability,
            "P(Sequence Start is A)": self.p_start_A,
            "P(Sequence Start is T)": self.p_start_T_or_U if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "P(Sequence Start is U)": self.p_start_T_or_U if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "P(Sequence Start is G)": self.p_start_G,
            "P(Sequence Start is C)": self.p_start_C,
            "P(Sequence End is A)": self.p_end_A,
            "P(Sequence End is T)": self.p_end_T_or_U if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else 0.00,
            "P(Sequence End is U)": self.p_end_T_or_U if self.seq_type == list(NUCLEOTIDE_BASE.keys())[1] else 0.00,
            "P(Sequence End is G)": self.p_end_G,
            "P(Sequence End is C)": self.p_end_C,
        }

        with open(current_export_file, "w") as file:
            json.dump(bio_data, file, indent=4)


    def call_menu_window(self, username, firstname, lastname, signing_window, menu):

        """ Calling Menu Window """

        # A Tip On App Usage
        if interface.GUI_attr.tip_switch == 0:
            frame_1 = CTkFrame(self.window, fg_color=bright_colors[5], width=100, height=5)
            frame_1.place(relx=0.36, rely=0.9)
            tip_off = CTkLabel(self.window, text_color=text_color, text="Tip: " + str(tips[3]),
                               fg_color=color_scheme, font=(window_font, (window_font_size - 10)))
            tip_off.place(relx=0.215, rely=0.865)
            custom_progressbar_tips(self.window, frame_1, color_scheme, tip_off, self.export_button)
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
                # Add 1 To self.backward_1 Since It Starts At 0
                counter_1 = self.backward_1 + 1
                for key, value in list(self.DNA_data.items())[self.backward_1: self.forward_1]:
                    gc_result = gc_content(str(value))
                    if gc_result != -1:
                        gc_content_subseq_1[str(counter_1)] = round(gc_result, rounder)
                    else:
                        gc_content_subseq_1[str(counter_1)] = 0.00
                    counter_1 += 1
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
                # Add 1 To self.backward_1 Since It Starts At 0
                counter_2 = self.backward_1 + 1
                for key, value in list(self.DNA_data.items())[self.backward_1: self.forward_1]:
                    gc_result = gc_content(str(value))
                    if gc_result != -1:
                        gc_content_subseq_2[str(counter_2)] = round(gc_result, rounder)
                    else:
                        gc_content_subseq_2[str(counter_2)] = 0.00
                    counter_2 += 1
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
                # Add 1 To self.backward_1 Since It Starts At 0
                counter_3 = self.backward_2 + 1
                for key, value in list(self.DNA_data.items())[self.backward_2: self.forward_2]:
                    at_result = at_content(str(value), self.seq_type)
                    if at_result != -1 and at_result != -2:
                        at_content_subseq_1[str(counter_3)] = round(at_result, rounder)
                    else:
                        at_content_subseq_1[str(counter_3)] = 0.00
                    counter_3 += 1
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
                # Add 1 To self.backward_1 Since It Starts At 0
                counter_4 = self.backward_2 + 1
                for key, value in list(self.DNA_data.items())[self.backward_2: self.forward_2]:
                    at_result = at_content(str(value), self.seq_type)
                    if at_result != -1 and at_result != -2:
                        at_content_subseq_2[str(counter_4)] = round(at_result, rounder)
                    else:
                        at_content_subseq_2[str(counter_4)] = 0.00
                    counter_4 += 1
                self.plot_3.cla()
                self.plot_3.set_title("AT Percent Per Read Index" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percent Per Read Index")
                self.plot_3.set_ylabel("AT Percentage(s)" if self.seq_type == list(NUCLEOTIDE_BASE.keys())[0] else "AU Percentage(s)")
                self.plot_3.set_xlabel("Read Indexes")
                self.plot_3.plot(at_content_subseq_2.keys(), at_content_subseq_2.values(), c=bright_colors[1], marker='o')
                self.canvas_3.draw()