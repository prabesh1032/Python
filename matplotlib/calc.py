import tkinter as tk
def evaluate_expression(event=None):
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except Exception as e:
        entry.delete(0,tk.END)
root=tk.Tk()
entry=tk.Entry(root,width=16,font=('Arial',24),bd=8,insertwidth=2,bg='powder blue', justify='right')
entry.grid(row=0,column=0,columnspan=4)
buttons=[
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',1,0),('2',1,1),('3',1,2),('-',1,3),
    ('0',4,0),(',',4,1),('=',4,2),('+',4,3),
]
for(text,row,col) in buttons:
    if text=='=':
        button=tk.Button(root, text=text,padx=16,pady=16,bd=8,fg='black',font=('Arial',20,'bold')
                        bg="powder blue",command=evaluate_expression)
        button.grid(row=row,column=col,columnspan=1)
        root.bind('<Return>',evaluate_expression)
    else:
        button=tk.Button(root, text=text,padx=16,pady=16,bd=8,fg='black',font=('Arial',20,'bold')
                        bg="powder blue", command=lamda t=text)