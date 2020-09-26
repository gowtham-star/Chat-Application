import time
import socket
import sys
from Tkinter import *
def sendmessage():
    output1=en.get()
    conn.send(output1.encode())
    if 'count' not in sendmessage.__dict__:
        sendmessage.count=8
    Label(text=name+": "+output1,bg="#aed581",padx=12,pady=6,relief="ridge",anchor=W).grid(row=sendmessage.count,column=3)
    sendmessage.count+=2
def recvmessage():
    if 'cnt' not in recvmessage.__dict__:
        recvmessage.cnt = 9
    message=conn.recv(1024)
    message=message.decode()
    message=s_name+": "+message
    Label(text=message,bg="#fff",padx=12,pady=6,relief="ridge",anchor=E).grid(row=recvmessage.cnt,column=1)
    recvmessage.cnt=recvmessage.cnt+2
    print("")
    print(name+":"+message)
    print("")
def senddocument():
    fname=en2.get()
    f = open(fname, 'rb')
    print "Sending Data ...."  
    l = f.read()
    while True:      
        for line in l:
            conn.send(line)    
        break
    print("Data Sent ....")
def recvdocument():
    data=conn.recv(1024)       
    print data
    f=open("recievedfile1.txt","w")
    f.write(data)
    

print("    welcome to chat room  ")
print("")
print("initialising....")
time.sleep(1)
s=socket.socket()
#Host name
host=socket.gethostname()
port=700
s.bind((host,port))
print("")
print("Servers Address: "+host)
print("")
name=raw_input(str("Please Enter Your Name: "))
s.listen(1)
print("")
print("waiting for incoming connections...")
print("")
conn,addr=s.accept()
print("Connected  :)")
s_name=conn.recv(1024)
s_name=s_name.decode()
print("")
print(s_name+" is connected to the chat..")
print("")
conn.send(name.encode())

top=Tk()
#For sending messages
Label(top,text="Enter Your Chat:",bg="#00b0ff",padx=20,pady=6,relief="ridge",anchor=W).grid(row=4,column=1)
en=Entry(top,bd=4,fg="#d50000",justify=LEFT,width=26)
en.grid(row=4,column=2)
Button(top,text="Send",command= sendmessage,activebackground="#55AA55",bd=3,bg="#88CC88",padx=10,pady=1).grid(row=4,column=3)
Button(top,text="Refresh",command= recvmessage,activebackground="#55AA55",bd=3,bg="#88CC88",padx=20,pady=1,width=10).grid(row=5,column=2)

#For sending documents

Label(top,text="Enter File name to send:",bg="#00b0ff",padx=20,pady=6,relief="ridge",anchor=W).grid(row=0,column=1)
en2=Entry(top,bd=4,fg="#d50000",justify=LEFT,width=26)
en2.grid(row=0,column=2)
Button(top,text="Send Document",command= senddocument,activebackground="#55AA55",bd=3,bg="#88CC88",padx=10,pady=1).grid(row=0,column=3)
Button(top,text="Recieve Document",command= recvdocument,activebackground="#55AA55",bd=3,bg="#88CC88",padx=20,pady=1,width=10).grid(row=1,column=2)


top.title(name)
top.geometry("450x600")
top.mainloop()
