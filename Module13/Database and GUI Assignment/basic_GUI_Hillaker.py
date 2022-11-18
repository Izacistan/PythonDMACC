import tkinter as tinker

#Declare functions
def pick_breakfast():
    label.config(text="We've had one, yes.")

def pick_second_breakfast():
    label.config(text="But what about Second Breakfast?")

def pick_lunch():
    label.config(text="I don't think he knows about second breakfast, Pip.")

def pick_dinner():
    label.config(text="Dinner? Supper?")

#GUI
MAIN_WINDOW = tinker.Tk()
#Title
MAIN_WINDOW.title("Favorite Meal")
label = tinker.Label(MAIN_WINDOW, text="Waiting")
label.grid(row=5)

#Check buttons
var1 = tinker.IntVar()
check = tinker.Checkbutton(MAIN_WINDOW, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)

var2 = tinker.IntVar()
check = tinker.Checkbutton(MAIN_WINDOW, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)

var3 = tinker.IntVar()
check = tinker.Checkbutton(MAIN_WINDOW, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)

var4 = tinker.IntVar()
check = tinker.Checkbutton(MAIN_WINDOW, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)

#Exit GUI
exit_button = tinker.Button(MAIN_WINDOW, text='Exit', width=25, command=MAIN_WINDOW.destroy)
exit_button.grid(row=6)

MAIN_WINDOW.mainloop()