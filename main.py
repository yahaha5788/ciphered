import tkinter as tk
from tkinter import messagebox
from string import ascii_letters

from helpers.configs import main_cfg, desc_cfg, ButtonDescriptions, button_cfg, bg_color, light_bg, entry_cfg, label_cfg, fg_color, grayed_out
from helpers.tkclassextensions import DetailedButton, SwitchButton, PromptTextEntry, Shifter, CaesarOutputLabel, VigenereOutputLabel

def _hover_leave(event):
    description.configure(text="Hover over an object to see a description.")

def init_home() -> None:

    start = tk.Label(
        home_screen,
        text='Select a cipher type:',
        font=('Calibri', 10),
        bg=bg_color,
        fg='white')
    start.place(x=5, y=5)

    caesar_button = DetailedButton(
        home_screen,
        description=ButtonDescriptions.CAESAR.value,
        cnf=button_cfg,
        text="Caesar Cipher",
        command=caesar_screen.tkraise
    )
    caesar_button.place(x=5, y=40)
    caesar_button.bind('<Enter>', lambda c: description.configure(text=caesar_button.desc))
    caesar_button.bind('<Leave>', _hover_leave)

    vigenere_button = DetailedButton(
        home_screen,
        description=ButtonDescriptions.VIGENERE.value,
        text="Vigenere Cipher",
        cnf=button_cfg,
        command=vigenere_screen.tkraise)
    vigenere_button.place(x=5, y=80)
    vigenere_button.bind('<Enter>', lambda v: description.configure(text=vigenere_button.desc))
    vigenere_button.bind('<Leave>', _hover_leave)

def init_settings() -> None:
    pass

def init_caesar() -> None:

    switch_button = SwitchButton(
        caesar_screen,
        "Decoding text",
        "Encoding text",
        cnf=button_cfg
    )
    switch_button.place(x=170, y=5)
    switch_button.bind('<Enter>', lambda s: description.configure(text='Switch between encoding and decoding.'))
    switch_button.bind('<Leave>', _hover_leave)

    plaintext_getter = PromptTextEntry(
        caesar_screen,
        "Enter plaintext here...",
        entry_cfg=entry_cfg,
    )
    plaintext_getter.place(x=65, y=45)
    plaintext_getter.filler.place(x=70, y=48)
    plaintext_getter.bind('<Enter>', lambda p: description.configure(text='Enter the plaintext to encode here' if not switch_button.is_on else "Enter the ciphertext to decode here."))
    plaintext_getter.filler.bind('<Enter>', lambda p: description.configure(text='Enter the plaintext to encode here' if not switch_button.is_on else "Enter the ciphertext to decode here."))
    plaintext_getter.bind('<Leave>', _hover_leave)
    plaintext_getter.filler.bind('<Leave>', _hover_leave)

    shift_win_y = 90
    shift_win_x = 130

    shift_caption = tk.Label(
        caesar_screen,
        cnf=label_cfg,
        text="Shift: "
    )
    shift_caption.place(x=shift_win_x - 10, y=shift_win_y - 20)
    shift_caption.bind("<Enter>", lambda s: description.configure(text='The shift of the plaintext in the alphabet.' if not switch_button.is_on else "The shift of the original ciphertext."))
    shift_caption.bind("<Leave>", _hover_leave)

    shift = Shifter(
        caesar_screen,
        0,
        26,
        cnf=label_cfg
    )

    shift.place(x=shift_win_x, y=shift_win_y)
    shift.increase.place(x=shift_win_x + 20, y=shift_win_y)
    shift.decrease.place(x=shift_win_x - 25, y=shift_win_y)

    shift.bind("<Enter>", lambda s: description.configure(text='The shift of the plaintext in the alphabet.' if not switch_button.is_on else "The shift of the original ciphertext."))
    shift.increase.bind("<Enter>", lambda i: description.configure(text='Increase the shift by one.'))
    shift.decrease.bind("<Enter>", lambda i: description.configure(text='Decrease the shift by one.'))

    shift.bind("<Leave>", _hover_leave)
    shift.increase.bind("<Leave>", _hover_leave)
    shift.decrease.bind("<Leave>", _hover_leave)

    out_caption = tk.Label(
        caesar_screen,
        cnf=label_cfg,
        text="Output:"
    )
    out_caption.place(x=10, y=120)
    out_caption.bind("<Enter>", lambda o: description.configure(text='The output of the caesar cipher.'))
    out_caption.bind("<Leave>", _hover_leave)

    out = CaesarOutputLabel(
        caesar_screen,
        plaintext_getter,
        shift,
        switch_button,
        start_text="Ciphertext appears here...",
        wraplength='270',
        bg=bg_color,
        fg=grayed_out,
        justify='left',
        font=('Calibri', 10)
    )
    out.place(x=10, y=140)
    out.bind("<Enter>", lambda o: description.configure(text='The output of the caesar cipher.'))
    out.bind("<Leave>", _hover_leave)

    switch_button.state.trace_add("write", lambda *args: plaintext_getter.filler.configure(text='Enter plaintext here...' if not switch_button.state.get() else 'Enter ciphertext here...'))
    switch_button.state.trace_add("write", lambda *args: out.set_default(value = 'Ciphertext appears here...' if not switch_button.state.get() else 'Plaintext appears here...'))

    def _clear_all():
        shift.reset()
        plaintext_getter.text_var.set("")
        switch_button.set_state(False)
        home_screen.tkraise()

    back_button = DetailedButton(
        caesar_screen,
        description="Go back to the home screen.",
        text="<- Back",
        cnf=button_cfg,
        command=_clear_all)
    back_button.place(x=5, y=5)
    back_button.bind('<Enter>', lambda b: description.configure(text=back_button.desc))
    back_button.bind('<Leave>', _hover_leave)

def init_vigenere() -> None:

    back_button = DetailedButton(
        vigenere_screen,
        description="Go back to the home screen.",
        text="<- Back",
        cnf=button_cfg,
        command=home_screen.tkraise)
    back_button.place(x=5, y=5)
    back_button.bind('<Enter>', lambda b: description.configure(text=back_button.desc))
    back_button.bind('<Leave>', _hover_leave)

    switch_button = SwitchButton(
        vigenere_screen,
        "Decoding text",
        "Encoding text",
        cnf=button_cfg
    )
    switch_button.place(x=170, y=5)
    switch_button.bind('<Enter>', lambda s: description.configure(text='Switch between encoding and decoding.'))
    switch_button.bind('<Leave>', _hover_leave)

    plaintext_getter = PromptTextEntry(
        vigenere_screen,
        "Enter text here...",
        entry_cfg=entry_cfg
    )
    plaintext_getter.place(x=65, y=45)
    plaintext_getter.filler.place(x=70, y=48)

    def _keyword_check(d, S):
        if d == '1':
            if S not in ascii_letters:
                messagebox.showinfo("invalid keyword", f'the keyword can only contain letters, not "{S}"')
                return False
            elif S in keyword_getter.get():
                messagebox.showinfo("invalid keyword", f'the keyword cannot contain "{S}", it is a duplicate letter.')
                return False
            return True
        return True

    keyword_check = (root.register(_keyword_check), '%d', '%S')

    keyword_getter = PromptTextEntry(
        vigenere_screen,
        "Enter keyword here...",
        entry_cfg=entry_cfg,
        validate='key',
        validatecommand=keyword_check,
    )
    keyword_getter.place(x=65, y=75)
    keyword_getter.filler.place(x=70, y=78)

    result = VigenereOutputLabel(
        vigenere_screen,
        plaintext_getter,
        keyword_getter,
        switch_button,
        start_text="Ciphertext appears here...",
        wraplength='270',
        bg=bg_color,
        fg=grayed_out,
        justify='left',
        font=('Calibri', 10)
    )
    result.place(x=10, y=140)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("cipher")
    root.geometry("540x400")
    root.resizable(False, False)
    #root.attributes("-fullscreen", True)

    home_screen = tk.Frame(root, cnf=main_cfg)
    home_screen.place(x=0, y=0)
    desc_widget = tk.Frame(root, cnf=desc_cfg)
    desc_widget.pack(side='right')
    settings_screen = tk.Frame(root, cnf=main_cfg)
    settings_screen.place(x=0, y=0)

    caesar_screen = tk.Frame(root, cnf=main_cfg)
    caesar_screen.place(x=0, y=0)

    vigenere_screen = tk.Frame(root, cnf=main_cfg)
    vigenere_screen.place(x=0, y=0)

    description = tk.Label( # this is the only object in desc_widget, so i won't give it its own function
        desc_widget,
        text='Hover over an object to see a description.',
        wraplength='135',
        bg=light_bg,
        font=('Calibri', 10),
        fg=fg_color,
        justify='left'
    )
    description.place(x=0 ,y=0)


    init_home()
    init_caesar()
    init_vigenere()

    home_screen.tkraise()


    root.mainloop()