from tkinter import *

def button_is_click():
    # my_label.config(text="Button got clicked")
    op = int(input.get()) * 1.60934
    output.config(text=op)

#Set window
window = Tk()
window.title("ABC")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

#input
input = Entry(width=10)
input.grid(column=2,row=1)

# inputLabel
input_unit = Label(text ="Miles")
input_unit.grid(column=3,row=1)

# Label
my_label = Label(text ="is equal to")
my_label.grid(column=1,row=2)

# Result
output = Label(text="")
output.grid(column=2,row=2)

# ResultLabel
output_unit = Label(text ="Km")
output_unit.grid(column=3,row=2)

#button
button = Button(text="Click me",command=button_is_click)
button.grid(column=2,row=3)



window.mainloop()

# *arg, **kwargs(**kw)
    #*arg store input as tuple
    # **kwargs store input as dictionary


#Sample:

# def all_aboard(a, *args, **kw): 
#     print(a, args, kw)

# all_aboard(4, 7, 3, 0, x=10, y=64)
    
    # result:
    #   4, (7,3,0), {"x":10, "y":64}