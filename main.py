# import tkinter
#
# # This capture is all about creating GUI using tkinter lib.
#
# window = tkinter.Tk()
#
# window.title("A GUI")
# window.minsize(width=500, height=300)
#
# # Labels
#
# my_label = tkinter.Label(text="This is a cool label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# window.mainloop()


# Practicing *args

def add(*args):
    return sum(args)


user_input = input("Please give me numbers separated by commas (exit to close): ").strip()
while user_input != 'exit':
    try:
        print(add(*[float(x.strip()) for x in user_input.split(",")]))
    except ValueError:
        print("Please only input numbers.")
    user_input = input('Please give me numbers separated by commas (exit to close): ').strip()


