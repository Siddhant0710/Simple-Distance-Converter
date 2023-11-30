import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.title("Distance Converter")

root.geometry("600x250")
root.resizable(width=False, height=False)

# Title Label
title_label=tk.Label(root)
title_label.place(x=0,y=0,width=600,height=46)

# Input Unit Label
label_1=tk.Label(root)
label_1.place(x=10,y=60,width=273,height=31)

# Input Unit Dropdown
input_combo=ttk.Combobox(root)
input_combo["values"] = ["Kilometer", "Meter", "Centimeter","Miles", "Yard", "Foot"]
input_combo.place(x=10,y=100,width=273,height=30)
input_combo.current(0)

# Output Unit Label
label_2=tk.Label(root)
label_2.place(x=320,y=60,width=268,height=30)

# Output Unit Dropdown
output_combo=ttk.Combobox(root)
output_combo["values"] = ["Kilometer", "Meter", "Centimeter","Miles", "Yard", "Foot"]
output_combo.place(x=320,y=100,width=268,height=30)
output_combo.current(0)
      
# Input Weight Label
input_entry=tk.Entry(root)
input_entry.place(x=10,y=140,width=274,height=36)

# placing the cursor in the input_entry
input_entry.focus()

# Output Weight Label
output_entry=tk.Entry(root)
output_entry.place(x=320,y=140,width=268,height=36)

def convert():
    input_unit = input_combo.get()
    output_unit = output_combo.get()
    try:
        input_dist = float(input_entry.get())
    except ValueError:
        input_dist = 0
        input_entry.delete(0, 'end')
        input_entry.insert(0, "Invalid Input")
        return
    
    if input_unit == "Kilometer":
        kilometer = input_dist
    elif input_unit == "Meter   ":
        kilometer = input_dist / 1000
    elif input_unit == "Centimeter":
        kilometer = input_dist / 100000
    elif input_unit == "Miles":
        kilometer = input_dist / 0.621371
    elif input_unit == "Yard":
        kilometer = input_dist * 0.0009144
    elif input_unit == "Foot":
        kilometer = input_dist / 3280.84
    else:
        kilometer = 0
        
    if output_unit == "Kilometer":
        output_dist = kilometer
    elif output_unit == "Meter":
        output_dist = kilometer * 1000
    elif output_unit == "Centimeter":
       output_dist = kilometer * 100000
    elif output_unit == "Miles":
       output_dist = kilometer * 0.621371
    elif output_unit == "Yard":
        output_dist = kilometer / 0.0009144
    elif output_unit == "Foot":
        output_dist = kilometer * 3280.84
    else:
       output_dist = 0
       
    output_entry.configure(state='normal')
    output_entry.delete(0, 'end')
    output_entry.insert(0, str(output_dist))

convert_button=tk.Button(root)
convert_button.configure(text="Convert", command=convert)
convert_button.place(x=230,y=200,width=147,height=36)

root.mainloop()