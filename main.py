import tkinter as tk

def convert_function():
    


    temp = float (temp_entry.get())

    if(var.get()==1):
        # F to C
        temp = ((temp - 32)-32*5)/9 # The Formula for converting from Fahrenheit to Celsius

    elif(var.get()==2):
        # C to F
        temp = ((temp*9/5)+32)

    result.configure (text = "Result: {}".format(temp))

def key_pressed(event):

    if(event.char == "\r"):
        convert_function()


root = tk.Tk()
root.title ("Temperture Converter")
root.geometry ("300x200") # Width x Height
root.iconbitmap ("temperture.ico")
root.minsize(width = 300, height = 200)
root.maxsize(width = 300, height = 200)

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)

root.grid_columnconfigure(0 , weight = 1)
root.grid_columnconfigure(1 , weight = 1)

root.configure(bg = "#EEA698")


root.bind('<KeyPress>', key_pressed) # When A Key is pressed, Call the key_pressed Function

var = tk.IntVar()
var.set(1)

temp_entry = tk.Entry (root)
temp_entry.grid (row = 0, column = 0, columnspan = 2)

# F to C Radio Button
f_to_c = tk.Radiobutton (root, text = "F to C", variable = var, value = 1, bg = "#EEA698")
f_to_c.grid (row = 1, column = 0)

c_to_f = tk.Radiobutton (root, text = "C to F", variable = var, value = 2, bg = "#EEA698")
c_to_f.grid (row = 1, column = 1)

# Convert Button
convert_button = tk.Button (root, text = "CONVERT", command = convert_function, bg = "#FF0000", fg = "#FFFFFF")
convert_button.grid (row = 2, column = 0, columnspan = 2)

result = tk.Label (root, text = "Result: - ", bg = "#EEA698")
result.grid (row = 3, column = 0, columnspan = 2 )



root.mainloop()