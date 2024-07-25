import tkinter as tk

# def on_button_click():
#     print("Button Clicked!")
#root=tk.Tk()
# label=tk.Label(root,text="Hello Prabesh")
# label.pack()
# button=tk.Button(root,text="Click Me",command=on_button_click)
# button.pack()

# def print_entry():
#     print(entry.get())


# button=tk.Button(root,text="Print Entry",command=print_entry)
# button.pack()

'''
def on_button_click1():
    label.config(text=entry.get())

root.title("Tkinter Example")

label=tk.Label(root,text="Enter something:")
label.pack()
entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="Update Label",command=on_button_click1)
button.pack()
root.mainloop()
'''
'''
def print_checked():
    print(var.get())
root=tk.Tk()
var=tk.IntVar()
button=tk.Button(root,text="Update Label",command=on_button_click1)
button.pack()
'''

'''
root= tk.Tk()
root.title("Title")
root.geometry("500x500")
def print_selected():
    print(var.get())

var=tk.StringVar(value="option 1")
radiobutton1 =tk.Radiobutton(root, text="option 1", variable=var, value="option 1")
radiobutton2 =tk.Radiobutton(root, text="option 2", variable=var, value="option 2")
radiobutton1.pack()
radiobutton2.pack()
button=tk.Button(root,text="printSelection",command=print_selected)
button.pack()
root.mainloop()

'''
'''
root= tk.Tk()
root.title("Title")
root.geometry("500x500")
def print_selection():
    selected= listbox.curselection()
    for i in selected:
        print(listbox.get(i))
listbox=tk.Listbox(root)
listbox.pack()
for item in["item 1","iten 2","item 3"]:
   listbox.insert(tk.END,item)
button=tk.Button(root,text="printSelection",command=print_selection)
button.pack()
root.mainloop()
'''
'''
root= tk.Tk()
root.title("Title")
root.geometry("500x500")
text=tk.Text(root, wrap=tk.NONE)
text.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

scrollbar=tk.Scrollbar(root,command=text.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)
for i in range(100):
    text.insert(tk.END,f"this is Line{i+1}\n")
root.mainloop()
'''
'''
from tkinter import ttk
def print_selection(event):
    print("Selected",combobox.get())
root=tk.Tk()
root.title("Combobox Example")
frame=tk.Frame(root)
frame.pack(fill=tk.BOTH,expand=True)
combobox=ttk.Combobox(frame,values=["CSIT","BIM","BCA","BHM"])
combobox.pack(side=tk.RIGHT,padx=10,pady=10,anchor='e')
combobox.bind("<<ComboboxSelected>>",print_selection)
root.mainloop()
tk.tk
'''
'''
#menu
def on_new():
    print("new file")
def on_open():
    print("open file")
def on_exit():
    print("exit file")
root=tk.Tk()
root.title(" menu and Combobox Example")
menubar=tk.Menu(root)
file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label='New',command=on_new)
file_menu.add_command(label='Open',command=on_open)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=on_exit)
file_menu.add_cascade(label='File',menu=file_menu)
root.config(menu=menubar)
root.mainloop()
tk.tk
'''
