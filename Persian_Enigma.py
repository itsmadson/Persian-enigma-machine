import tkinter as tk
from tkinter import ttk, font
import random

class PersianEnigmaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("دستگاه انیگما پارسی")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        self.alphabet = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        self.setup_font()
        self.setup_gui()
        self.r1, self.r2, self.r3 = self.rndm_rotor()
        
    def setup_font(self):
        available_fonts = font.families()
        persian_fonts = ['Noto Naskh Arabic', 'Arial Unicode MS', 'Tahoma', 'Times New Roman']
        
        self.persian_font = None
        for f in persian_fonts:
            if f in available_fonts:
                self.persian_font = f
                break
        
        if not self.persian_font:
            self.persian_font = 'TkDefaultFont'
            
    def setup_gui(self):
        container = tk.Frame(self.root, bg='black')
        container.pack(padx=20, pady=20, fill='both', expand=True)
        title = tk.Label(container, 
                        text="دستگاه رمز پارسی", 
                        font=(self.persian_font, 16, 'bold'),
                        bg='black', 
                        fg='white')
        title.pack(pady=(0, 20))
        input_label = tk.Label(container, 
                             text=":متن ورودی", 
                             font=(self.persian_font, 12),
                             bg='black', 
                             fg='white',
                             justify='right')
        input_label.pack(anchor='e')
        input_frame = tk.Frame(container, bg='black')
        input_frame.pack(fill='x', pady=(0, 20))
        self.input_text = tk.Text(input_frame, 
                                height=10, 
                                bg='#1e1e1e', 
                                fg='white',
                                font=(self.persian_font, 12),
                                insertbackground='white',
                                wrap=tk.WORD)
        self.input_text.pack(side='left', fill='x', expand=True)
        input_scroll = tk.Scrollbar(input_frame)
        input_scroll.pack(side='right', fill='y')
        self.input_text.config(yscrollcommand=input_scroll.set)
        input_scroll.config(command=self.input_text.yview)
        btn_frame = tk.Frame(container, bg='black')
        btn_frame.pack(fill='x', pady=(0, 20))
        button_texts = [("رمزنگاری", self.encrypt_text),
                       ("پاک کردن", self.clear_text),
                       ("روتور جدید", self.new_rotor)]
        for text, command in button_texts:
            btn = tk.Button(btn_frame, 
                          text=text,
                          font=(self.persian_font, 11),
                          command=command,
                          bg='#333333',
                          fg='white',
                          width=15,
                          relief='flat',
                          padx=10,
                          pady=5)
            btn.pack(side='right', padx=5)
        output_label = tk.Label(container, 
                              text=":متن رمزنگاری شده", 
                              font=(self.persian_font, 12),
                              bg='black', 
                              fg='white',
                              justify='right')
        output_label.pack(anchor='e')
        output_frame = tk.Frame(container, bg='black')
        output_frame.pack(fill='x')
        
        self.output_text = tk.Text(output_frame, 
                                 height=10, 
                                 bg='#1e1e1e', 
                                 fg='#00ff00',
                                 font=(self.persian_font, 12),
                                 insertbackground='white',
                                 wrap=tk.WORD)
        self.output_text.pack(side='left', fill='x', expand=True)
        
        output_scroll = tk.Scrollbar(output_frame)
        output_scroll.pack(side='right', fill='y')
        
        self.output_text.config(yscrollcommand=output_scroll.set)
        output_scroll.config(command=self.output_text.yview)

        self.input_text.tag_configure('rtl', justify='right')
        self.output_text.tag_configure('rtl', justify='right')
        
        self.input_text.bind('<KeyRelease>', self.handle_text_change)
        
    def handle_text_change(self, event=None):
        self.input_text.tag_add('rtl', '1.0', 'end')
        self.output_text.tag_add('rtl', '1.0', 'end')

    def rndm_rotor(self):
        r1 = list(self.alphabet)
        random.shuffle(r1)
        r2 = list(self.alphabet)
        random.shuffle(r2)
        r3 = list(self.alphabet)
        random.shuffle(r3)
        return r1, r2, r3

    def encrypt_text(self):
        input_text = self.input_text.get("1.0", "end-1c")
        if not input_text:
            return
            
        result = ""
        for char in input_text:
            if char in self.alphabet:
                c1 = self.r1[self.alphabet.find(char)]  # Fixed: added self.
                c2 = self.r2[self.alphabet.find(c1)]    # Fixed: added self.
                c3 = self.r3[self.alphabet.find(c2)]    # Fixed: added self.
                result += c3
            else:
                result += char
                
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", result)
        self.output_text.tag_add('rtl', '1.0', 'end')
        
    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        
    def new_rotor(self):
        self.r1, self.r2, self.r3 = self.rndm_rotor()
        self.clear_text()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PersianEnigmaGUI()
    app.run()