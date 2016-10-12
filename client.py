import thread
from chatfns import *



#CONNECTION 

s = socket(AF_INET,SOCK_STREAM)
host = '127.0.1.1'
port = 8011
conn = ''
s.bind((host, port))


#MOUSE EVEVNST
def ClickAction():
   
    EntryText =entrybox.get("0.0",END)
    myupdate(chatspace, EntryText)

    
    chatspace.yview(END)

    
    entrybox.delete("0.0",END)
            
    
    conn.sendall(EntryText)
    

#KEYBOARD EVENT	



def PressAction(event):
	entrybox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	entrybox.config(state=DISABLED)

    

#CREATING CHAT TKINTER





window = Tk()
window.title('Lets chat')
window.geometry("500x500")
window.resizable(width=FALSE, height=FALSE)


chatspace = Text(window, bd=0, bg="grey", height="8", width="50", font="Arial",)
chatspace.insert(END, "Waiting to connect..\n")
chatspace.config(state=DISABLED)


scrollbar = Scrollbar(window, command=chatspace.yview, cursor="heart")
chatspace['yscrollcommand'] = scrollbar.set


SendButton = Button(window, font=30, text="Send", width="12", height=5,
                    bd=0, bg="yellow", activebackground="red",
                    command=ClickAction)


entrybox = Text(window, bd=0, bg="grey",width="29", height="5", font="Arial")
entrybox.bind("<Return>", DisableEntry)
entrybox.bind("<KeyRelease-Return>", PressAction)


scrollbar.place(x=476,y=6, height=386)
chatspace.place(x=6,y=6, height=386, width=470)
entrybox.place(x=128, y=401, height=90, width=365)
SendButton.place(x=6, y=401, height=90)

# GETTING CONNECTION 
def GetConnected():
    s.listen(1)
    global conn
    conn, addr = s.accept()
    connectioninfo(chatspace, 'Connected with the host ')
    
    while 1:
        try:
            data = conn.recv(1024)
            update2(chatspace, data)
            
        except:
            connectioninfo(chatspace, '\n  partner  disconnected \n  Waiting to connect. \n  ')
            GetConnected()

    
    
thread.start_new_thread(GetConnected,())



window.mainloop()

