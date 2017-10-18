try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import *
    from Tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))

# initialize a TreeView
myTreeView = ttk.Treeview(content)
myTreeView["columns"] = ("Index", "Value", "Price", "LAST_PRICE")
myTreeView.column("Index", stretch=False, width=150)
myTreeView.column("Value", stretch=False, width=100)
myTreeView.column("Price", stretch=False, width=100)
myTreeView.column("LAST_PRICE", stretch=False, width=100)
myTreeView.heading("Index", text="Index")
myTreeView.heading("Value", text="Value")
myTreeView.heading("Price", text="Price")
myTreeView.heading("LAST_PRICE", text="Last Price")

# attach a Horizontal (x) scrollbar to the frame
treeXScroll = ttk.Scrollbar(content, orient=HORIZONTAL)
treeXScroll.configure(command=myTreeView.xview)
myTreeView.configure(xscrollcommand=treeXScroll.set)

# initialize the Label and Entry
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

# initialize Checkbuttons
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)

# initialize Buttons
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# set position of all above objects by grid
content.grid(column=0, row=0, sticky=(N, S, E, W))
myTreeView.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
treeXScroll.grid(column=0, row=3, columnspan=3, sticky=W + E)
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=4)
two.grid(column=1, row=4)
three.grid(column=2, row=4)
ok.grid(column=3, row=4)
cancel.grid(column=4, row=4)

# Handling Resize
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

# run UI
root.mainloop()
