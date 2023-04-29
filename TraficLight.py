from tkinter import *
import serial
tk = Tk()
tk.geometry('300x250')
tk.title("TRAFIC LIGHT")

photo = PhotoImage(file = "trafic_light.png")
tk.iconphoto(False, photo)

comPort = "COM2"
countButton = 0

label = Label(tk, text='', font= ("Times New Roman", 12))
label.grid(column=0, row=0)

label_connect = Label(tk, text='')
label_connect.grid(column=0, row=5)

try:
    ser = serial.Serial(comPort, 9600)
    label_connect.config(text = comPort + " is OK")
except serial.SerialException:
    label_connect.config(text = 'COM port not found')

checkbox_state_red = BooleanVar()
checkbox_state_yellow = BooleanVar()
checkbox_state_green = BooleanVar()


def slavaUkraini():
    global countButton
    if countButton == 0:
        btnUKR.config(text = "Heroyam Slava", bg="blue", fg="yellow")
        countButton +=1
    else:
        btnUKR.config(text = "Slava Ukrayini", bg="black", fg="red")
        countButton = 0

def checkboxRED():
    checkbox_state_yellow.set(False)
    checkbox_state_green.set(False)
    if(checkbox_state_red.get()):
        data = '1'
    else:
        data = '0'
    byte_data = bytes(data, 'utf-8')
    ser.write(byte_data)
    read_serial()
    
def checkboxYELLOW():
    checkbox_state_red.set(False)
    checkbox_state_green.set(False)
    if(checkbox_state_yellow.get()):
        data = '3'
    else:
        data = '2'
    byte_data = bytes(data, 'utf-8')
    ser.write(byte_data)
    read_serial()
    
def checkboxGREEN():
    checkbox_state_yellow.set(False)
    checkbox_state_red.set(False)
    if(checkbox_state_green.get()):
        data = '5'
    else:
        data = '4'
    byte_data = bytes(data, 'utf-8')
    ser.write(byte_data)
    read_serial()
    
def read_serial():
    if ser.in_waiting > 0:
        data = ser.readline().decode('ascii').rstrip()
        label.config(text = data)
    tk.after(10, read_serial)

checkbox_red = Checkbutton(tk, text='RED LIGHT', width = "15", bg = "red", font= ("Times New Roman", 12), variable=checkbox_state_red, command=checkboxRED)
checkbox_red.grid(column=0, row=1)
checkbox_yellow = Checkbutton(tk, text='YELLOW LIGHT', width = "15", bg = "yellow", font= ("Times New Roman", 12), variable=checkbox_state_yellow, command=checkboxYELLOW)
checkbox_yellow.grid(column=0, row=2)
checkbox_green = Checkbutton(tk, text='GREEN LIGHT', width = "15", bg = "green", font= ("Times New Roman", 12), variable=checkbox_state_green, command=checkboxGREEN)
checkbox_green.grid(column=0, row=3, padx=50)

btnUKR = Button(tk, text="Slava Ukrayini", bg="black", fg="red", font= ("Times New Roman", 15), command=slavaUkraini)
btnUKR.grid(column=0, row=4, pady=20)


tk.mainloop()

ser.close()