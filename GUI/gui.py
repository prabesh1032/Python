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



# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Function to be called when the button is clicked
def say_hello():
    label.config(text="Hello, World!")

# Add a label widget
label = tk.Label(window, text="Click the button")
label.pack(pady=30)

# Add a button widget
button = tk.Button(window, text="Click Me", command=say_hello)
button.pack(pady=10)

# Start the main event loop
window.mainloop()

import tkinter as tk

# Function to calculate the result based on the operation
def calculate(operation):
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero"
    
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widgets for user input
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry1.pack(pady=5)
entry2.pack(pady=5)

# Buttons for different operations
button_add = tk.Button(window, text="Add", command=lambda: calculate("add"))
button_subtract = tk.Button(window, text="Subtract", command=lambda: calculate("subtract"))
button_multiply = tk.Button(window, text="Multiply", command=lambda: calculate("multiply"))
button_divide = tk.Button(window, text="Divide", command=lambda: calculate("divide"))

# Arrange buttons in the window
button_add.pack(pady=5)
button_subtract.pack(pady=5)
button_multiply.pack(pady=5)
button_divide.pack(pady=5)

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()









import tkinter as tk

# Function to update the input
def update_input(number):
    current = input_label['text']
    input_label.config(text=current + str(number))

# Function to set the operation
def set_operation(op):
    global first_number, operation
    first_number = int(input_label['text'])
    operation = op
    input_label.config(text="")

# Function to calculate the result
def calculate_result():
    second_number = int(input_label['text'])
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number if second_number != 0 else "Error"
    input_label.config(text=str(result))

# Function to clear input
def clear_input():
    input_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Label to display the current input/result
input_label = tk.Label(window, text="", width=12, anchor='e', relief="sunken")
input_label.pack(pady=10)

# Create number buttons (1-9)
button_frame = tk.Frame(window)
button_frame.pack()

for i in range(1, 10):
    button = tk.Button(button_frame, text=str(i), width=5, height=2, 
                       command=lambda num=i: update_input(num))
    button.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

# Operation buttons
tk.Button(window, text="+", width=5, height=2, command=lambda: set_operation("+")).pack(side="left", padx=5)
tk.Button(window, text="-", width=5, height=2, command=lambda: set_operation("-")).pack(side="left", padx=5)
tk.Button(window, text="*", width=5, height=2, command=lambda: set_operation("*")).pack(side="left", padx=5)
tk.Button(window, text="/", width=5, height=2, command=lambda: set_operation("/")).pack(side="left", padx=5)
tk.Button(window, text="=", width=5, height=2, command=calculate_result).pack(side="left", padx=5)
tk.Button(window, text="C", width=5, height=2, command=clear_input).pack(side="left", padx=5)

# Start the main event loop
window.mainloop()


import tkinter as tk

def calculate_simple_interest():
    # Retrieve values from the text boxes
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    
    # Calculate simple interest
    interest = (principal * rate * time) / 100
    
    # Display the result in the result_entry text box
    result_entry.delete(0, tk.END)  # Clear the existing result
    result_entry.insert(0, str(interest))

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")

# Create and place labels and text boxes
tk.Label(root, text="Principal:").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Rate (%):").grid(row=1, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Time (years):").grid(row=2, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

tk.Label(root, text="Interest:").grid(row=3, column=0)
result_entry = tk.Entry(root)
result_entry.grid(row=3, column=1)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_simple_interest)
calculate_button.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
'''
import tkinter as tk

def on_button_click():
    # Get the text from the entry widget and display it in the label
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

# Create the main window
root = tk.Tk()
root.title("Basic GUI Example")

# Create a label
label = tk.Label(root, text="Enter something:")
label.pack(pady=10)  # Use pack layout with some padding

# Create a text field (entry)
entry = tk.Entry(root)
entry.pack(pady=10)  # Use pack layout with some padding

# Create a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)  # Use pack layout with some padding

# Create a second frame to demonstrate grid layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Create additional widgets in the frame using grid layout
label2 = tk.Label(frame, text="Grid Layout Example")
label2.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(frame)
entry2.grid(row=0, column=1, padx=10, pady=10)

button2 = tk.Button(frame, text="Submit", command=lambda: label2.config(text=f"You entered: {entry2.get()}"))
button2.grid(row=0, column=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
