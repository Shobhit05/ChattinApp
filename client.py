# creating a noraml chat window #


from chatfns import *
import socket
import thread
from Tkinter import *
window=Tk()
window.title("Chat window")
window.geometry("500x500")
window.resizable(width=False,height=True)



# connecting to the partner #
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.1.1'
port=1234
address=(host,port)
data=''





#MOUSE EVENTS #


def Clickaction():
    
    entrytext=entrybox.get("0.0",END)
    
    LoadMyEntry(chatspace, entrybox)
   
    chatspace.yview(END)
 
    chatspace.config(state=DISABLED)
    
    entrybox.delete("0.0",END)
    
    
    s.sendall(entrytext)


    




# keyboard events #

def Pressaction(event):
    chatspace.config(state=NORMAL)
    Clickaction()
def Disablentry(event):
    chatspace.config(state=DISABLED)
    
















# creating a space for text message to be displayed #

chatspace=Text(window, bd=0,bg="grey",height="8",width="500",font="Arial")
chatspace.insert(END,"Connecting to your Partner \n \n")
chatspace.config(state=DISABLED)


# creating a scrollbar #

scrollbar=Scrollbar(window,command=chatspace.yview,cursor="heart")
chatspace['yscrollcommand'] = scrollbar.set

# Create the entry box for the message typing  #

entrybox=Text(window,bd=0,bg="grey" ,width="29" ,height="5" ,font="Arial")
entrybox.bind("<Return>",Disablentry)
entrybox.bind("<KeyRelease-Return>",Pressaction)


# create the send button #
sendbutton=Button(window, font=30, text="Send", width="12", height=5,bd=0, bg="green", activebackground="red",

                 command=Clickaction)




#placing the components in the chat window #

chatspace.place(x=6,y=6,height=386,width=488) # x= shift from x and y axis #
scrollbar.place(x=480,y=6,height=386)
entrybox.place(x=150,y=401,height=120,width=340)
sendbutton.place(x=4,y=401,height=80,width=140)




# connecting to the port #

def recievedata():
    try:
        global LoadConnectionInfo
        s.connect(address)
        LoadConnectionInfo(chatspace, '[ Succesfully connected ]')

    except:
         LoadConnectionInfo(chatspace, '[ Unable to connect ]')
         return


    while 1:
        try:
            
            data=s.recv(1024)
            

        except:
            LoadConnectionInfo(chatspace, '\n [ Your partner has disconnected ] \n')

        if data != '':
            print data
            chatspace.insert(END,data)
            if window.focus_get()==None:
                FlashMyWindow("Chat window")

        else:
            LoadConnectionInfo(chatspace, '\n [ Your partner has disconnected ] \n')
            break


thread.start_new_thread(recievedata,())

        








window.mainloop()







