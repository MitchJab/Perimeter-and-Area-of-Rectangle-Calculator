#Name: Jabari Mitchell
#Date: Nov 27 2022
#Name of Program: Space eaters
#Description: Create a GUI and calculates the perimeter and width of a program
# Imports
from tkinter import *
from tkinter.tix import *

# Define functions:
# function for resetting the window
# Define a function to show the error message
def ResetButtonfunc():
    entry_width.delete(0,END)
    entry_length.delete(0,END)
    label_area_output["text"] = ""
    label_perimeter_output["text"] = ""
# #Calculate Perimeter Function
def calculate_value():
    #Validating the input
    try:
        valid_length = float(entry_length.get())
        valid_width = float(entry_width.get())
        #Ensuring numbers are positive and calculating input
        if valid_length > 0 and valid_width > 0:

            Calculate_value = 0
            calculate_total_area = valid_length * valid_width
            calculate_total_perimeter = valid_length + valid_width * 2
         #output label
            label_perimeter_output.configure(text = "{:,.2f}".format(calculate_total_perimeter))
            label_area_output.configure(text = "{:,.2f}".format(calculate_total_area))
#if integer is not positive this will give an error message
            pass
        else:
            print("ERROR PLEASE ENTER A POSITIVE INTEGER")
    except:
         print("ERROR PLEASE ENTER A Numeric Value")

#exit function
def close_window():
        exit()
#creating window, size, and title
window=Tk()
window.geometry("300x200")
window.minsize(width = 500, height = 500)
window.title("Space Eaters: Calculator")

tooltip = Balloon(window)
# Row 0 Widgets - length
label_length = Label(text = "Length")
label_length.grid(row = 0, column = 0, padx = 5, pady = 5)
entry_length = Entry()
entry_length.grid(row = 0, column = 1, padx = 5, pady = 5)
tooltip.bind_widget(entry_length, msg = "Enter the total length")

#Row 1 Widgets - width
label_width = Label(text = "Width")
label_width.grid(row = 1, column = 0, padx = 5, pady = 5)
entry_width = Entry()
entry_width.grid(row = 1, column = 1, padx = 5, pady = 5)
tooltip.bind_widget(entry_width, msg = "Enter the total width")

#Row 2 Widgets - Area (output)
label_area = Label(text = "Area: ")
label_area.grid (row = 2, column = 0, padx = 5, pady = 5)
label_area_output = Label(width = 15, bd = 2, relief = SUNKEN)
label_area_output.grid(row = 2, column = 1, padx = 5, pady = 5)

#Row 3 Widgets - Perimeter
label_perimeter = Label(text = "Perimeter: ")
label_perimeter.grid(row = 3, column = 0, padx = 5, pady = 5)
label_perimeter_output = Label(width = 15, bd = 2, relief = SUNKEN)
label_perimeter_output.grid(row = 3, column = 1, padx = 5, pady = 5)


# Row 4 Widgets - Buttons
button_calculate = Button(text = "Calculate", width = 15, command = calculate_value)
button_calculate.grid (row = 4, column = 0, padx = 5, pady = 5)
tooltip.bind_widget(button_calculate, msg = "the calculation button")
button_clear = Button(window,text="Reset <Alt-r>",command=ResetButtonfunc)
button_clear.grid(row = 4, column = 1, padx = 5, pady = 5)
tooltip.bind_widget(button_clear, msg = "This button clears all input")
button_exit= Button(text = "Exit", width = 15, command = close_window)
button_exit.grid(row = 4, column = 2, padx = 5, pady = 5)
tooltip.bind_widget(button_exit, msg = "Click to exit the program")

#runs the window
window.mainloop()