from tkinter import *

# Also note above, different way to import.

# This capture is all about creating GUI using tkinter lib.

window = Tk()

window.title("A GUI")
window.minsize(width=500, height=300)

# Labels

my_label = Label(text="This is a cool label", font=("Arial", 24, "bold"))
my_label.pack()

# How to update a tkinter label (Reminder, a label could just be text.)

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_event():
    print("Button has been pressed")
    my_label.config(text="Button Pressed")


button = Button(text="Click Me", command=button_event)
button.pack()

text_entry = Entry(width=10)
text_entry.pack()

window.mainloop()

# Practicing *args
#
# def add(*args):
#     return sum(args)
#
#
# user_input = input("Please give me numbers separated by commas (exit to close): ").strip()
# while user_input != 'exit':
#     try:
#         print(add(*[float(x.strip()) for x in user_input.split(",")]))
#     except ValueError:
#         print("Please only input numbers.")
#     user_input = input('Please give me numbers separated by commas (exit to close): ').strip()
#
#
