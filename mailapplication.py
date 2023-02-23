from tkinter import*
import smtplib


#Main Screen
master = Tk()
master.title("Mail Appllication")

#Functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notify.config(text= "All Fields Required", fg ="red" )
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notify.config(text= "Email has been sent", fg="green")
    except:
        notify.config(text= "Error Sending mail", fg ="red")

def reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')




#Graphics 
Label(master, text="Email App", font = ("calibri",15)).grid(row = 0, sticky = N)
Label(master, text="Use the form below to send an Email", font = ("calibri",11)).grid(row = 1, sticky = W, padx= 5)
Label(master, text="Email", font = ("calibri",11)).grid(row = 2, sticky = W, padx= 5)
Label(master, text="Password", font = ("calibri",11)).grid(row = 3, sticky = W, padx= 5)
Label(master, text="To", font = ("calibri",11)).grid(row = 4, sticky = W, padx= 5)
Label(master, text="Subject", font = ("calibri",11)).grid(row = 5, sticky = W, padx= 5)
Label(master, text="Body", font = ("calibri",11)).grid(row = 6, sticky = W, padx= 5)

notify = Label(master, text="", font = ("calibri",11))
notify.grid(row = 7, sticky = S, padx= 5)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#Entries
usernameEntry = Entry(master, textvariable=temp_username)
usernameEntry.grid(row=2, column=0)
passwordEntry = Entry(master, show= "*", textvariable=temp_password)
passwordEntry.grid(row=3, column=0)
receiverEntry = Entry(master, textvariable=temp_receiver)
receiverEntry.grid(row=4, column=0)
subjectEntry = Entry(master, textvariable=temp_subject)
subjectEntry.grid(row=5, column= 0)
bodyEntry = Entry(master, textvariable=temp_body)
bodyEntry.grid(row=6, column= 0)

#Buttons
Button(master, text="send", command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(master,text="Reset", command=reset).grid(row=7, sticky=W, pady=45, padx=45)


master.mainloop()