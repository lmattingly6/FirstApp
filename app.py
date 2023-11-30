import tkinter as tk
#importing tkinter for classic widgets

window = tk.Tk(
)
#creating first window


#Creating Label widget
greeting = tk.Label(
    text="Hello, this is my first app! ",
    fg="white", 
    bg="black"
    )
greeting.pack() #Must include a pack




#Creating an entry box with a Label
textlabel = tk.Label(text="Write something here!")
textlabel.pack()

entry = tk.Entry(
    fg="yellow",
    bg = "blue",
    width=25
)
message = entry.get()
#This retrieves the entry and stores it 
# in memory
entry.pack()



#Creating a button
button = tk.Button(
    text="Click Here!!",
    width=15,
    height=2,
    bg="blue",
    fg="yellow",
)
button.pack()







window.mainloop()
#Must include mainloop for the window to 
#execute