from Tkinter import *
from socket import *


	
def LoadConnectionInfo(chatspace, entrybox):
    if entrybox != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            chatspace.insert(END, entrybox+'\n')
            chatspace.config(state=DISABLED)
            chatspace.yview(END)

def LoadMyEntry(chatspace, entrybox):
    if entrybox != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            LineNumber = float(chatspace.index('end'))-1.0
            chatspace.insert(END, "You: " + str(entrybox))
            chatspace.tag_add("You", LineNumber, LineNumber+0.4)
            chatspace.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            chatspace.config(state=DISABLED)
            chatspace.yview(END)


def LoadOtherEntry(chatspace, entrybox):
    if entrybox != '':
        chatspace.config(state=NORMAL)
        if chatspace.index('end') != None:
            try:
                LineNumber = float(chatspace.index('end'))-1.0
            except:
                pass
            chatspace.insert(END, "Other: " + str(entrybox))
            chatspace.tag_add("Other", LineNumber, LineNumber+0.6)
            chatspace.tag_config("Other", foreground="#04B404", font=("Arial", 12, "bold"))
            chatspace.config(state=DISABLED)
            chatspace.yview(END)
