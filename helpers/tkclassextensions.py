import tkinter as tk
from ciphers.caesarcipher import caesar_cipher
from helpers.configs import grayed_out, light_bg, fg_color


class DetailedButton(tk.Button):
    def __init__(self, master: tk.BaseWidget, description: str, **kwargs):
        super().__init__(master=master, **kwargs)
        self.desc = description # idk i'm bored

class SwitchButton(tk.Button):
    def __init__(self, master: tk.BaseWidget, on_text: str, off_text: str, **kwargs):
        self.state = tk.BooleanVar()
        super().__init__(master=master, text=off_text, command=self.toggle, textvariable=self.state)
        self.is_on = False
        self.on_text = on_text
        self.off_text = off_text

    def toggle(self):
        self.is_on = not self.is_on
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
        self.content = tk.IntVar()
        self.indices: list[int] = []
        for x in range(lower, upper):
            self.indices.append(x)
        self.current_index = lower
        super().__init__(master=master, text=self.current_index, textvariable=self.content, **kwargs)
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
            self.content.set(self.current_index)
        else:
            self.current_index += 1
            self.content.set(self.current_index)

    def decrease(self):
        if self.current_index == self.lower:
            self.current_index = self.upper - 1
            self.content.set(self.current_index)
        else:
            self.current_index -= 1
            self.content.set(self.current_index)

    def reset(self):
        self.current_index = self.lower
        self.content.set(self.current_index)

class CaesarOutputLabel(tk.Label):
    def __init__(self, master, dependency: PromptTextEntry, shift: Shifter, start_text: str, **kwargs):
        super().__init__(master=master, text=start_text, **kwargs)
        self.default = start_text
        self.dependency: tk.Entry = dependency
        self.shift_get: tk.IntVar = shift.content
        self.text_get: tk.StringVar = dependency.text_var

        self.shift_get.trace_add("write", self.run_updates)
        self.text_get.trace_add("write", self.run_updates)

    def run_updates(self, *args):
        plaintext = self.text_get.get()
        if len(plaintext) != 0:
            shift = self.shift_get.get()
            ciphertext = caesar_cipher(plaintext, shift)
            self.configure(text=ciphertext, fg=fg_color)
        else:
            self.configure(text=self.default, fg=grayed_out)


