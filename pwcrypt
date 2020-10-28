#! /usr/bin/env python3

import sys
if not sys.version_info[0] == 3:
    sys.exit('pwcrypt works only with Python 3.')

import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import pyperclip

### Define some constants
WIDTH_ENTRY = 40
SIZE_IMG = 30

### Define ASCII table (copied from string module)
whitespace      = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters   = ascii_lowercase + ascii_uppercase
digits          = '0123456789'
hexdigits       = digits + 'abcdef' + 'ABCDEF'
octdigits       = '01234567'
punctuation     = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable       = digits + ascii_letters + punctuation + whitespace

### ASCII chars used
chars = digits + ascii_letters + punctuation
len_chars = len(chars)

### Define the main functions
def map_num(string):
    ''' make a string a list of numbers, which are their position in the 'chars' list'''
    return list(map(lambda x: chars.find(x), string))

### Build the interface
master = tk.Tk()

# define fonts
fontLabel = tkFont.Font(family = "Segoe UI", size = 16)
fontPassword = tkFont.Font(family = "Consolas", size = 16)

# labels
tk.Label(master, text = "Password", font = fontLabel).grid(row = 0, sticky = tk.E, pady = (20,5), padx = (20,5))
tk.Label(master, text = "New password", font = fontLabel).grid(row = 1, sticky = tk.E, pady = (5,20), padx = (20,5))

# entry for password
pw = tk.Entry(master, width = WIDTH_ENTRY, font = fontPassword, exportselection = 0)
pw.grid(row = 0, column = 1, sticky = tk.W, pady = (20,5), padx = (5,0))

# output password
new_pw_text = tk.StringVar()
new_pw = tk.Entry(master, textvariable = new_pw_text, width = WIDTH_ENTRY, state = "readonly", font = fontPassword)
new_pw.grid(row = 1, column = 1, sticky = tk.W, columnspan = 1, pady = (5,20), padx = (5,0))

# entry for key
tk.Label(master, text = "Key", font = fontLabel).grid(row = 2, column = 0, rowspan = 2, sticky = tk.E, pady = (10,20), padx = (20,5))
key = tk.Entry(master, width = WIDTH_ENTRY, show = "*", font = fontPassword, exportselection = 0)
key.grid(row = 2, column = 1, columnspan = 1, rowspan = 2, sticky = tk.W, pady = (10,20), padx = (5,0))

# radio buttons for encrypt/decrypt
decrypt = tk.BooleanVar()
tk.Radiobutton(master, text = "Encrypt", variable = decrypt, value = False, font = fontLabel).grid(row = 2, column = 3, sticky = tk.W, padx = 20, pady = (10,5))
tk.Radiobutton(master, text = "Decrypt", variable = decrypt, value = True, font = fontLabel).grid(row = 3, column = 3, sticky = tk.W, padx = 20, pady = (5,20))

# button for convert
def transform_password():
    ''' encrypt/decrypt a password according to a key '''
    the_key = key.get()
    password = pw.get()
    len_key = len(the_key)
    factor  = -1 if decrypt.get() else 1
    if len_key == 0:
        new_pw_text.set("ERROR: key not provided")
        new_pw.config(fg = "red")
        return
    num_key = map_num(the_key)
    if any([n == -1 for n in num_key]):
        new_pw_text.set("ERROR: invalid character in key.")
        new_pw.config(fg = "red")
        return
    num_pw = map_num(password)
    if any([n == -1 for n in num_pw]):
        new_pw_text.set("ERROR: invalid character in password.")
        new_pw.config(fg = "red")
        return
    reshaped_key = [num_key[pos % len_key] for pos in range(len(password))]
    new_password = list(map(lambda p, k: chars[(p+factor*(k+1)) % len_chars], num_pw, reshaped_key)) # the +1 allows to ensure a minimum shift of 1, even if we have the first character of 'chars' (position 0 would mean shift 0 otherwise)
    new_pw_text.set("".join(new_password))
    new_pw.config(fg = "black")

button = tk.Button(master, text = "Convert", command = transform_password, font = fontLabel)
button.grid(row = 0, column = 3, rowspan = 2, padx = 30, pady = 30, ipadx = 5, ipady = 5)

# button for trash
def trash():
    pw.delete(0, tk.END)
    new_pw_text.set("")
button_trash_pic_bis = Image.open("./icons/trash.png").resize((SIZE_IMG, SIZE_IMG), Image.ANTIALIAS)
button_trash_pic = ImageTk.PhotoImage(button_trash_pic_bis)
button_trash = tk.Button(master, command = trash, font = fontPassword, image = button_trash_pic, width = SIZE_IMG, height = SIZE_IMG)
button_trash.grid(row = 0, column = 2, sticky = tk.W, padx = 0, pady = (20,5))

# button for copy in clipboard
def clipboard():
    temp = tk.Tk()
    temp.withdraw()
    temp.clipboard_clear()
    temp.clipboard_append(new_pw.get())
    pyperclip.copy(new_pw.get())
    temp.update()
    temp.destroy()
button_copy_pic_bis = Image.open("./icons/copy.png").resize((SIZE_IMG, SIZE_IMG), Image.ANTIALIAS)
button_copy_pic = ImageTk.PhotoImage(button_copy_pic_bis)
button_copy = tk.Button(master, command = clipboard, font = fontPassword, image = button_copy_pic, width = SIZE_IMG, height = SIZE_IMG)
button_copy.grid(row = 1, column = 2, sticky = tk.W, padx = 0, pady = (5,20))

# button to see the key
def start_show_key(event):
    key.config(show = "")
def stop_show_key(event):
    key.config(show = "*")
button_show_pic_bis = Image.open("./icons/eye.png").resize((SIZE_IMG, SIZE_IMG), Image.ANTIALIAS)
button_show_pic = ImageTk.PhotoImage(button_show_pic_bis)
button_show = tk.Button(master, font = fontPassword, image = button_show_pic, width = SIZE_IMG, height = SIZE_IMG)
button_show.grid(row = 2, column = 2, rowspan = 2, sticky = tk.W, padx = 0, pady = (10,20))
button_show.bind("<ButtonPress-1>", start_show_key)
button_show.bind("<ButtonRelease-1>", stop_show_key)

# save the current clipboard
temp = tk.Tk()
temp.withdraw()
temp.clipboard_clear()
temp.clipboard_append(pyperclip.paste())
temp.update()
temp.destroy()

### Mainloop
master.mainloop()
