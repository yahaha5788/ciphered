import tkinter as tk

from ciphers.caesarcipher import caesar_cipher
from ciphers.vigenerecipher import vigenere_cipher
from helpers.configs import grayed_out, light_bg, fg_color


class DetailedButton(tk.Button):
    def __init__(self, master: tk.BaseWidget, description: str, **kwargs):
        super().__init__(master=master, **kwargs)
        self.desc = description # idk i'm bored

class SwitchButton(tk.Button):
    def __init__(self, master: tk.BaseWidget, on_text: str, off_text: str, **kwargs):
        self.state = tk.BooleanVar()
        super().__init__(master=master, text=off_text, command=self.toggle, **kwargs)
        self.is_on = False
        self.state.set(False)
        self.on_text = on_text
        self.off_text = off_text

    def toggle(self):
        self.is_on = not self.is_on
        self.state.set(self.is_on)
        if self.is_on:
            self.configure(text=self.on_text)
        else:
            self.configure(text=self.off_text)


    def set_state(self, state: bool):
        if state is True:
            self.configure(text=self.on_text)
            self.is_on = True
        else:
            self.configure(text=self.off_text)
            self.is_on = False
        self.state.set(self.is_on)

class PromptTextEntry(tk.Entry):
    def __init__(self, master: tk.BaseWidget, prompt_text: str, entry_cfg: dict, **kwargs):
        self.text_var = tk.StringVar()
        super().__init__(master=master, cnf=entry_cfg, textvariable=self.text_var, **kwargs)

        self.prompt_cfg: dict = {
            'bg': light_bg,
            'fg': grayed_out,
            'font': ('Calibri', 10),
            'justify': 'left',
            'bd': 0
        }

        self.prompt = prompt_text
        self.filler = tk.Label(master, text=prompt_text, cnf=self.prompt_cfg)
        self.filler.bind('<Button-1>', self.focus_set())

        self.text_var.trace_add("write", self.run_updates)

    def run_updates(self, *args):
        text = self.text_var.get()
        if len(text) > 0:
            self.filler.lower(self)
        if len(text) == 0:
            self.filler.tkraise(self)

class Shifter(tk.Label):
    def __init__(self, master, lower: int, upper: int, **kwargs):
        self.number = tk.IntVar()
        self.indices: list[int] = []
        for x in range(lower, upper):
            self.indices.append(x)
        self.current_index = lower
        super().__init__(master=master, text=self.current_index, textvariable=self.number, **kwargs)
        self.upper = upper
        self.lower = lower



        self.btn_cfg: dict = {
            'bg': light_bg,
            'fg': fg_color,
            'borderwidth': '1',
            'relief': 'groove',
            'font': ('Calibri', 10)
        }

        self.increase = tk.Button(
            master,
            cnf=self.btn_cfg,
            text='->',
            command=self.increase
        )
        self.decrease = tk.Button(
            master,
            cnf=self.btn_cfg,
            text='<-',
            command=self.decrease
        )

    def increase(self):
        if self.current_index == self.upper - 1:
            self.current_index = self.lower
            self.number.set(self.current_index)
        else:
            self.current_index += 1
            self.number.set(self.current_index)

    def decrease(self):
        if self.current_index == self.lower:
            self.current_index = self.upper - 1
            self.number.set(self.current_index)
        else:
            self.current_index -= 1
            self.number.set(self.current_index)

    def reset(self):
        self.current_index = self.lower
        self.number.set(self.current_index)

class CaesarOutputLabel(tk.Label):
    def __init__(self, master, plaintext_source: PromptTextEntry, shift_source: Shifter, encode_source: SwitchButton, start_text: str, **kwargs):
        super().__init__(master=master, text=start_text, **kwargs)
        self.default = start_text

        self.shift_get: tk.IntVar = shift_source.number
        self.text_get: tk.StringVar = plaintext_source.text_var
        self.encode_get: tk.BooleanVar = encode_source.state

        self.shift_get.trace_add("write", self.run_updates)
        self.text_get.trace_add("write", self.run_updates)
        self.encode_get.trace_add("write", self.run_updates)

    def run_updates(self, *args):
        plaintext = self.text_get.get()
        encode = not self.encode_get.get() #if true then encoding if false decode
        if len(plaintext) != 0:
            shift = self.shift_get.get()
            if encode is True:
                ciphertext = caesar_cipher(plaintext, shift)
            else:
                shift = abs(shift - 26)
                ciphertext = caesar_cipher(plaintext, shift)
            self.configure(text=ciphertext, fg=fg_color)
        else:
            self.configure(text=self.default, fg=grayed_out)

    def set_default(self, value: str):
        self.default = value
        if len(self.text_get.get()) == 0:
            self.configure(text=self.default)

class VigenereOutputLabel(tk.Label):
    def __init__(self, master, plaintext_source: PromptTextEntry, keyword_source: PromptTextEntry, encode_source: SwitchButton, start_text: str, **kwargs):
        super().__init__(master=master, text=start_text, **kwargs)
        self.default = start_text

        self.plaintext_getter = plaintext_source.text_var
        self.keyword_getter = keyword_source.text_var
        self.encode_getter = encode_source.state

        self.plaintext_getter.trace_add("write", self.run_updates)
        self.keyword_getter.trace_add("write", self.run_updates)
        self.encode_getter.trace_add("write", self.run_updates)

    def run_updates(self, *args):
        plaintext: str = self.plaintext_getter.get()
        encode: bool = not self.encode_getter.get()
        keyword: str = self.keyword_getter.get()
        if len(plaintext) != 0 and len(keyword) != 0:
            text = vigenere_cipher(plaintext, keyword, encode=encode)
            self.configure(text=text, fg=fg_color)
        else:
            self.configure(text=self.default, fg=grayed_out)

    def set_default(self, value: str):
        self.default = value
        if len(self.plaintext_getter.get()) == 0:
            self.configure(text=self.default)