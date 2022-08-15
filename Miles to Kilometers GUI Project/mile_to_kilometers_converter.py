from tkinter import*

#conversion when button is clicked
def button_clicked():
    m = float(convert.get())
    k = m * 1.609344
    result_label.config(text=f"{k}")

window = Tk() 
window.title("Miles to Kilometers Converter")
window.config(padx=20,pady=20)

#Miles Entry
convert = Entry(width=7)
convert.grid(column=1, row=0)

#Miles Text
miles = Label(text="Miles")
miles.grid(column=3, row=0)

#Equals Text
equal = Label(text=" is equal to ")
equal.grid(column=0, row=1)

#Output
result_label = Label(text="0")
result_label.grid(column=1, row=1)

#Km Text
kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)

#Complete Entry
button_convert = Button(text="Calculate", command=button_clicked)
button_convert.grid(column=1,row=2)

window.mainloop()