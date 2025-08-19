from tkinter import *

def miles_to_kilometers():
    miles = miles_input.get()
    try:
        km = float(miles) * 1.609344
        calculated_km_label.config(text=km)
    except ValueError:
        pass


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1, padx=5, pady=3)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2, padx=5, pady=3)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0, padx=5, pady=3)

calculated_km_label = Label(text="0")
calculated_km_label.grid(row=1, column=1, padx=5, pady=3)

km_label = Label(text="Km")
km_label.grid(row=1, column=2, padx=5, pady=3)

calculate_button=Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(row=2, column=1, padx=5, pady=3)

window.mainloop()