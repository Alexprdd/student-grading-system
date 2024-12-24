import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

#function

gradebook={                                                               
}

#adding to listbox/update function

def update():
    if surnameentry.get()=="":
        messagebox.showerror("Error!","Surname needs to be filled")
    else:
        key=surnameentry.get()
        if key not in gradebook.keys():
            listbox.insert(tk.END, key)
        gradebook[key]=(firstnameentry.get(),addressentry.get(), mobileentry.get(),emailentry.get(),birthdayentry.get())
        clear_all()
    print(gradebook)
    
def clear_all():            
    firstnameentry.delete(0,tk.END)
    surnameentry.delete(0,tk.END)
    addressentry.delete(0,tk.END)
    mobileentry.delete(0,tk.END)
    emailentry.delete(0,tk.END)
    birthdayentry.delete(0,tk.END)

def edit():
    clear_all()
    dataindex=listbox.curselection()
    if dataindex:
        key=listbox.get(dataindex)
        surnameentry.insert(0, key)
        details=gradebook[key]
        firstnameentry.insert(0,details[0])
        addressentry.insert(0, details[1])
        mobileentry.insert(0, details[2])
        emailentry.insert(0, details[3])
        birthdayentry.insert(0, details[4])
    else:
        messagebox.showerror("Error!","Select an item for editing")

def delete():
    dataindex=listbox.curselection()
    if dataindex:
        key=listbox.get(dataindex)
        del gradebook[key]
        listbox.delete(dataindex)
    else:
        messagebox.showerror("Error!","Please make sure you have selected a property")

def display(event):
    topwindow=tk.Toplevel(window)
    dataindex=listbox.curselection()
    data=""
    if dataindex:
        key=listbox.get(dataindex)
        details=gradebook[key]
        data+="Firstname  :   "+ details[0]+"\n"
        data+="Surname  :   "+ key+"\n"
        data+="Address  :   "+ details[1]+"\n"
        data+="Mobile  :   "+ details[2]+"\n"
        data+="Email  :   "+ details[3]+"\n"
        data+="Birthday  :   "+ details[4]+"\n"
    toplabel=tk.Label(topwindow)
    toplabel.config(text=data)
    toplabel.pack()

#save files

def save():
    dummycheck="fnfnnfnne"
    filetosave=asksaveasfile(defaultextension=".txt")
    if filetosave is not None:
        for item in listbox.get(0, tk.END):
            print(item.strip(), file=filetosave)
        listbox.delete(0, tk.END)


#open files

def open_file():
    file=askopenfile(mode="r", filetypes=[("text files","*.txt")])
    if file is not None:
        listbox.delete(0, tk.END)
        filedata=file.readlines()
        for data in filedata:
            listbox.insert(tk.END, data)
#design

#window

window=tk.Tk()
window.title("Student Grading System")
window.geometry("700x700")

titlelabel=tk.Label(window, text="My Student Grading System: ", font=("Arial", 12), bg="lightgrey")
titlelabel.place(x=105,y=10)

#listbox

listbox=tk.Listbox(window, width=50, height=25)
listbox.place(x=10,y=50)
listbox.bind("<<ListboxSelect>>", display)
#buttons

openFile=tk.Button(window, text="Open File Containing Grades", bd=2, width=30, bg="lightgrey",command=open_file)
openFile.place(x=350, y=10)

savefile=tk.Button(window, text="Save file Containing Grades", bd=2, width=25, bg="lightgrey",command=save)
savefile.place(x=250, y=650)

delete_button=tk.Button(window, text="Delete Record", bd=2, width=15, bg="lightgrey", command=delete)
delete_button.place(x=200, y=475)

edit_button=tk.Button(window, text="Edit Record/Grade", bd=2, width=15, bg="lightgrey", command=edit)
edit_button.place(x=10, y=475)

Update=tk.Button(window, text="Update/Add to Record", bd=2, width=20, bg="lightgrey", command=update)
Update.place(x=500, y=375)

#secondary labels

firstnamelabel=tk.Label(window, text="First name:", font=("Arial", 10), bg="lightgrey")
firstnamelabel.place(x=400, y=75)

surnamelabel=tk.Label(window, text="Surname: ", font=("Arial", 10), bg="lightgrey")
surnamelabel.place(x=400, y=125)

birthdaylabel=tk.Label(window,text="Date of birth:", font=("Arial", 10), bg="lightgrey")    
birthdaylabel.place(x=400, y=175)

mobilelabel=tk.Label(window, text="Parents Mobile:", font=("Arial", 10), bg="lightgrey")    
mobilelabel.place(x=400, y=225)

emaillabel=tk.Label(window ,text="Parents Email:", font=("Arial", 10), bg="lightgrey")  
emaillabel.place(x=400, y=275)  

addresslabel=tk.Label(window,text="Address:", font=("Arial", 10), bg="lightgrey")    
addresslabel.place(x=400, y=325)

#entries for ^^^

firstnameentry=tk.Entry(window, width=20, bd=2)
firstnameentry.place(x=500,y=75)

surnameentry=tk.Entry(window, width=20, bd=2)
surnameentry.place(x=500,y=125)

birthdayentry=tk.Entry(window, width=20, bd=2)
birthdayentry.place(x=500,y=175)

mobileentry=tk.Entry(window, width=20, bd=2)
mobileentry.place(x=500,y=225)

emailentry=tk.Entry(window, width=20, bd=2)
emailentry.place(x=500,y=275)

addressentry=tk.Entry(window, width=20, bd=2)
addressentry.place(x=500,y=325)
 

window.mainloop()