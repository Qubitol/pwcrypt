pwcrypt
===
A little Python tool to crypt and decrypt passwords on the basis of a chosen key.
It uses a very simple algorithm, based on translation of the password's characters on the basis of the key's characters.
So, keep you key safe and don't tell anyone.
The tool does not store **anything** inside it (read the code if you don't believe me).

If you use this tool, you are solely responsible on keeping your data safe.
As I said, the encryption algorithm is really simple.
This tool aims to help you in adding one more level of protection to the passwords you store (for example) in a book you carry around, which in principle anyone can find and read.

Install the requirements before using the tool, by running:  
`python -m pip install -r requirements.txt`  
and run with:  
`./pwcrypt`

### Postilla for Windows users
You can run the tool using the *Windows Subsystem for Linux*, but remember to activate an X server (such as [Xming](http://www.straightrunning.com/XmingNotes/) or [Vcxsrv](https://sourceforge.net/projects/vcxsrv/)) and to export the `DISPLAY` variable.
