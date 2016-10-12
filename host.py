import thread
from updating import *
from Tkinter import *
import socket

# CONNECTING WITH THE SERVER #



host = "127.0.1.1"
port = 1234 #any port u can give here 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)





#- MOUSE EVENTS 

def ClickAction():
    
    EntryText = entrybox.get("0.0",END)
    myupdate(chatspace, EntryText)

   
    chatspace.yview(END)

    
    entrybox.delete("0.0",END)
            
    
    s.sendall(EntryText)
# KEY BOARD ACTIONS #



def PressAction(event):
	entrybox.config(state=NORMAL)
	ClickAction()
def DisableEntry(event):
	entrybox.config(state=DISABLED)
    

# CREATING CHAT TKINTER 



window = Tk()
window.title('Lets Chat')
window.geometry("500x500")
window.resizable(width=FALSE, height=FALSE)


chatspace = Text(window, bd=0, bg="grey", height="8", width="50", font="Arial",)
chatspace.insert(END, "Connecting to your partner..\n")
chatspace.config(state=DISABLED)


scrollbar = Scrollbar(window, command=chatspace.yview, cursor="fleur")
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






# GETTING CONNECTION AND DATA 

def ReceiveData():
    try:
        s.connect((host, port))
        connectioninfo(chatspace, '[ Succesfully connected ]\n---------------------------------------------------------------')
    except:
        connectioninfo(chatspace, '[ Unable to connect ]')
        return
    
    while 1:
        try:
            data = s.recv(1024)
        except:
            connectioninfo(chatspace, '\n partner  disconnected  \n')
            break
        if data != '':
            update2(chatspace, data)
            
                
                
                
        else:
            connectioninfo(chatspace, '\n  partner disconnected  \n')
            break
    

thread.start_new_thread(ReceiveData,())

window.mainloop()
