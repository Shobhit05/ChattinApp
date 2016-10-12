from Tkinter import *
from socket import *


	
def connectioninfo(chatspace, EntryText):
    if EntryText != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            chatspace.insert(END, EntryText+'\n')
            chatspace.config(state=DISABLED)
            chatspace.yview(END)

def myupdate(chatspace, EntryText):
    if EntryText != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            LineNumber = float(chatspace.index('end'))-1.0
            chatspace.insert(END, "You: " + EntryText)
            chatspace.tag_add("You", LineNumber, LineNumber+0.4)
            chatspace.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            chatspace.config(state=DISABLED)
            chatspace.yview(END)


def update2(chatspace, EntryText):
    if EntryText != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            try:
                LineNumber = float(chatspace.index('end'))-1.0
            except:
                pass
            chatspace.insert(END, "Other: " + EntryText)
            chatspace.tag_add("Other", LineNumber, LineNumber+0.6)
            chatspace.tag_config("Other", foreground="#04B404", font=("Arial", 12, "bold"))
            chatspace.config(state=DISABLED)
            chatspace.yview(END)
