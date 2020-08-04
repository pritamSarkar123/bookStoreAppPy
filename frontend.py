"""
A program that stores the book info:
Title,Author,Year,ISBN

User can:
View all records
Search an entry
Add an entry
Update entry
Delete
Close

"""
from tkinter import *
import backend 

backend.connect_to_db()
selectedTuple=(0,"","",0,0)
def get_selected_row(event):
    global selectedTuple
    index=listOne.curselection()[0]
    selectedTuple=listOne.get(index)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry1.insert(END,selectedTuple[1])
    entry3.insert(END,selectedTuple[2])
    entry2.insert(END,selectedTuple[3])
    entry4.insert(END,selectedTuple[4])

def view_command():
    listOne.delete(0,END)
    rows=backend.view()
    if not len(rows):
        listOne.insert(END,"Empty list")
    else:
        for row in rows:
            listOne.insert(END,row)

def search_command():
    listOne.delete(0,END)
    try:
        title=title_text.get()
    except:
        title=""
    try:
        author=author_text.get()
    except:
        author=""
    try:
        year=int(year_text.get())
    except:
        year=0
    try:
        isbn=int(isbn_text.get())
    except:
        isbn=0
    for row in backend.search(title,author,year,isbn):
        listOne.insert(END,row)
    

def add_command():
    listOne.delete(0,END)
    try:
        title=title_text.get()
        author=author_text.get()
        year=int(year_text.get())
        isbn=int(isbn_text.get())
        backend.insert(title,author,year,isbn)
        # rows=backend.search(title,author,year,isbn)
        # for row in rows:
        #     listOne.insert(END,row)
        view_command()
    except:
        listOne.insert(END,"Wrong input")
    

def delete_command():
    global selectedTuple
    if selectedTuple!=(0,"","",0,0):
        backend.delete(selectedTuple[0])
        selectedTuple=(0,"","",0,0)
        view_command()
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
    else:
        listOne.delete(0,END)
        listOne.insert(END,"Nothing to delete")

def update_command():
    global selectedTuple
    if selectedTuple!=(0,"","",0,0):
        try:
            title=title_text.get()
            author=author_text.get()
            year=int(year_text.get())
            isbn=int(isbn_text.get())
            backend.update(selectedTuple[0],title,author,year,isbn)
            selectedTuple=(0,"","",0,0)
            view_command()
        except:
            listOne.delete(0,END)
            listOne.insert(END,"Wrong input")
    else:
        listOne.delete(0,END)
        listOne.insert(END,"Nothing to Update")

window=Tk()
window.wm_title("BookStore")
#------------------- Labels---------------------#
label1=Label(window,text="Title")
label1.grid(row=0,column=0)

label2=Label(window,text="Year")
label2.grid(row=1,column=0)

label3=Label(window,text="Author")
label3.grid(row=0,column=2)

label4=Label(window,text="ISBN")
label4.grid(row=1,column=2)

#-----------------Entries------------------#
title_text=StringVar()
entry1=Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

year_text=StringVar()
entry2=Entry(window,textvariable=year_text)
entry2.grid(row=1,column=1)

author_text=StringVar()
entry3=Entry(window,textvariable=author_text)
entry3.grid(row=0,column=3)

isbn_text=StringVar()
entry4=Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

#------------------ListBox----------------#
listOne=Listbox(window,height=6,width=35)
listOne.grid(row=2,column=0,rowspan=6,columnspan=2)
listOne.bind('<<ListboxSelect>>',get_selected_row)


#-------------------Scrol bAr-----------------#
scrollBarOne=Scrollbar(window)
scrollBarOne.grid(row=2,column=2,rowspan=6)

#------------merging scroll bar+ list box------#
listOne.configure(yscrollcommand=scrollBarOne.set)
scrollBarOne.configure(command=listOne.yview)


#-------------------Buttons------------------#

button1=Button(window,text="View all",width=12,command=view_command)
button1.grid(row=2,column=3)

button2=Button(window,text="Search entry",width=12,command=search_command)
button2.grid(row=3,column=3)

button3=Button(window,text="Add entry",width=12,command=add_command)
button3.grid(row=4,column=3)

button4=Button(window,text="Update",width=12,command=update_command)
button4.grid(row=5,column=3)

button5=Button(window,text="Delete",width=12,command=delete_command)
button5.grid(row=6,column=3)

button6=Button(window,text="Close",width=12,command=window.destroy)
button6.grid(row=7,column=3)

window.mainloop()