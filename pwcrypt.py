import tkinter as tk
import tkinter.font as tkFont

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

# set fonts
fontLabel = tkFont.Font(family = "Segoe UI", size = 16)
fontPassword = tkFont.Font(family = "Consolas", size = 16)

# labels
tk.Label(master, text = "Password", font = fontLabel).grid(row = 0, sticky = tk.E, pady = (20,5), padx = (20,5))
tk.Label(master, text = "New password", font = fontLabel).grid(row = 1, sticky = tk.E, pady = (5,20), padx = (20,5))

# entry for password
pw = tk.Entry(master, width = 50, font = fontPassword)
pw.grid(row = 0, column = 1, sticky = tk.W, pady = (20,5), padx = (5,0))

# output password
new_pw_text = tk.StringVar()
new_pw = tk.Entry(master, textvariable = new_pw_text, width = 50, state = "readonly", font = fontPassword)
new_pw.grid(row = 1, column = 1, sticky = tk.W, columnspan = 1, pady = (5,20), padx = (5,0))

# radio buttons for encrypt/decrypt
decrypt = tk.BooleanVar()
tk.Radiobutton(master, text = "Encrypt", variable = decrypt, value = False, font = fontLabel).grid(row = 2, column = 2, sticky = tk.W, padx = 20, pady = (10,5))
tk.Radiobutton(master, text = "Decrypt", variable = decrypt, value = True, font = fontLabel).grid(row = 3, column = 2, sticky = tk.W, padx = 20, pady = (5,20))

# entry for key
tk.Label(master, text = "Key", font = fontLabel).grid(row = 2, column = 0, rowspan = 2, sticky = tk.E, pady = (10,20), padx = (20,5))
key = tk.Entry(master, width = 50, show = "*", font = fontPassword)
key.grid(row = 2, column = 1, columnspan = 1, rowspan = 2, sticky = tk.W, pady = (10,20), padx = (5,0))

# button for action
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
button.grid(row = 0, column = 2, rowspan = 2, padx = 30, pady = 30, ipadx = 5, ipady = 5)

master.mainloop()