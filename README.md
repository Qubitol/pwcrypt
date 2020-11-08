# pwcrypt
A little Python tool to crypt and decrypt passwords on the basis of a chosen key.
It uses a very simple algorithm, based on traslation of the password's characters on the basis of the key's characters.
So, keep you key safe and don't tell anyone.
The tool does not store **anything** inside it, once you have quit the application.

If you use this tool, you are solely responsible on keeping your data safe.
As I said, the encryption algorithm is really simple.
This tool aims to help you in adding one more level of protection to the passwords you store (for example) in a book you carry around, which in principle anyone can find and read.

## Using the script `pwcrypt`
Install the requirements before using the tool, by running:  
`python -m pip install -r requirements.txt`  
and run with:  
`./pwcrypt`

### Postilla for Windows users
You can run the tool using the *Windows Subsystem for Linux*, but remember to activate an X server (such as [Xming](http://www.straightrunning.com/XmingNotes/) or [Vcxsrv](https://sourceforge.net/projects/vcxsrv/)) and to export the `DISPLAY` variable.

[comment]: <> (## Using the `.exe` file)
[comment]: <> (In the directory `pwcrypt` you can also find the bundled app, drag the directory in your favorite location and run on Windows simply running the `pwcrypt.exe` file.)

## How does the program work?
After running the program, you will be prompted with a window with the following boxes.  
The first input box allows to specify a password to encrypt/decrypt.  
The third and last box allows to specify the encryption key, which will be displayed through "`*`", to hid it.  
You can further select "Encrypt" or "Decrypt" through the radio button.  
Once you have specified both a password and a key, you can press the 'Convert' button to run the conversion, the encrypted/decrypted password will be displayed in the second box.

Pressing the "trash" ![](./images/trash.png) button allows to clean the passwords fields.  
Pressing the "clip" ![](./images/copy.png) button allows to copy the encrypted/decrypted password to the clipboard.  
Holding the "eye" ![](./images/eye.png) button allows to see the key explicitly.  