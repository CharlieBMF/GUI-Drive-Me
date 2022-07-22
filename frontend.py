from tkinter import *
from tkcalendar import Calendar
from datetime import date
import base64
from PIL import ImageTk, Image
import backend


def confirm_calendar_day():
    result = backend.check_calendar_day(cal.selection_get())
    choosen_date_text.config(text=cal.selection_get())

def sel():
    selection = "You selected the option " + str(var.get())
    print(selection)


root = Tk()
root.geometry("1800x800")

cal = Calendar(root,
               selectmode='day',
               year=int(date.today().strftime('%Y %m %y').split()[0]),
               month=int(date.today().strftime('%d %m %y').split()[1]),
               day=int(date.today().strftime('%d %m %y').split()[1])
               )
cal.grid(row=0, column=0, padx=20, pady=20, columnspan=4, rowspan=5)

get_date_button = Button(root, text="GET THIS DATE INFO", command=confirm_calendar_day)
get_date_button.grid(row=7, column=0, padx=0, pady=0)

choosen_date_label = Label(root, text='Chosen Date:')
choosen_date_label.grid(row=8, column=0, padx=2, pady=10)

choosen_date_text = Label(root, text='Variable')
choosen_date_text.grid(row=8, column=1, padx=2, pady=10)

karol_label = Label(root, text='Pan Karol')
karol_label.grid(row=1, column=5, padx=50, pady=10)

var1 = IntVar()
clio_img_karol = Image.open("clio.png")
clio_img_karol = clio_img_karol.resize((int(clio_img_karol.size[0]/5), int(clio_img_karol.size[1]/5)))
clio_img_karol = ImageTk.PhotoImage(clio_img_karol)
car_clio_button_karol = Radiobutton(root, image=clio_img_karol, variable=var1, value=1, command=sel)
car_clio_button_karol.grid(row=1, column=6, padx=20, pady=10)

mercedes_img_karol = Image.open("mercedes.png")
mercedes_img_karol = mercedes_img_karol.resize((int(mercedes_img_karol.size[0]/5), int(mercedes_img_karol.size[1]/5)))
mercedes_img_karol = ImageTk.PhotoImage(mercedes_img_karol)
car_mercedes_button_karol = Radiobutton(root, image=mercedes_img_karol, variable=var1, value=2, command=sel)
car_mercedes_button_karol.grid(row=1, column=7, padx=20, pady=10)

seat_img_karol = Image.open("seat.png")
seat_img_karol = seat_img_karol.resize((int(seat_img_karol.size[0]/5), int(seat_img_karol.size[1]/5)))
seat_img_karol = ImageTk.PhotoImage(seat_img_karol)
car_seat_button_karol = Radiobutton(root, image=seat_img_karol, variable=var1, value=3, command=sel)
car_seat_button_karol.grid(row=1, column=8, padx=20, pady=10)

toyota_img_karol = Image.open("toyota.png")
toyota_img_karol = toyota_img_karol.resize((int(toyota_img_karol.size[0]/5), int(toyota_img_karol.size[1]/5)))
toyota_img_karol = ImageTk.PhotoImage(toyota_img_karol)
car_toyota_button_karol = Radiobutton(root, image=toyota_img_karol, variable=var1, value=4, command=sel)
car_toyota_button_karol.grid(row=1, column=9, padx=20, pady=10)

yamaha_img_karol = Image.open("yamaha.png")
yamaha_img_karol = yamaha_img_karol.resize((int(yamaha_img_karol.size[0]/5), int(yamaha_img_karol.size[1]/5)))
yamaha_img_karol = ImageTk.PhotoImage(yamaha_img_karol)
car_yamaha_button_karol = Radiobutton(root, image=yamaha_img_karol, variable=var1, value=5, command=sel)
car_yamaha_button_karol.grid(row=1, column=10, padx=20, pady=10)

karol_car_chose_button = Button(root, text="I DROVE THIS CAR!", width=200)
karol_car_chose_button.grid(row=2, column=5, padx=0, pady=0,  columnspan=6)




pioter_label = Label(root, text='Pan Pioter')
pioter_label.grid(row=3, column=5, padx=50, pady=10)

var2 = IntVar()
clio_img_pioter = Image.open("clio.png")
clio_img_pioter = clio_img_pioter.resize((int(clio_img_pioter.size[0]/5), int(clio_img_pioter.size[1]/5)))
clio_img_pioter = ImageTk.PhotoImage(clio_img_pioter)
car_clio_button_pioter = Radiobutton(root, image=clio_img_pioter, variable=var2, value=1, command=sel)
car_clio_button_pioter.grid(row=3, column=6, padx=20, pady=10)

mercedes_img_pioter = Image.open("mercedes.png")
mercedes_img_pioter = mercedes_img_pioter.resize((int(mercedes_img_pioter.size[0]/5), int(mercedes_img_pioter.size[1]/5)))
mercedes_img_pioter = ImageTk.PhotoImage(mercedes_img_pioter)
car_mercedes_button_pioter = Radiobutton(root, image=mercedes_img_pioter, variable=var2, value=2, command=sel)
car_mercedes_button_pioter.grid(row=3, column=7, padx=20, pady=10)

seat_img_pioter = Image.open("seat.png")
seat_img_pioter = seat_img_pioter.resize((int(seat_img_pioter.size[0]/5), int(seat_img_pioter.size[1]/5)))
seat_img_pioter = ImageTk.PhotoImage(seat_img_pioter)
car_seat_button_pioter = Radiobutton(root, image=seat_img_pioter, variable=var2, value=3, command=sel)
car_seat_button_pioter.grid(row=3, column=8, padx=20, pady=10)

toyota_img_pioter = Image.open("toyota.png")
toyota_img_pioter = toyota_img_pioter.resize((int(toyota_img_pioter.size[0]/5), int(toyota_img_pioter.size[1]/5)))
toyota_img_pioter = ImageTk.PhotoImage(toyota_img_pioter)
car_toyota_button_pioter = Radiobutton(root, image=toyota_img_pioter, variable=var2, value=4, command=sel)
car_toyota_button_pioter.grid(row=3, column=9, padx=20, pady=10)

yamaha_img_pioter = Image.open("yamaha.png")
yamaha_img_pioter = yamaha_img_pioter.resize((int(yamaha_img_pioter.size[0]/5), int(yamaha_img_pioter.size[1]/5)))
yamaha_img_pioter = ImageTk.PhotoImage(yamaha_img_pioter)
car_yamaha_button_pioter = Radiobutton(root, image=yamaha_img_pioter, variable=var2, value=5, command=sel)
car_yamaha_button_pioter.grid(row=3, column=10, padx=20, pady=10)

pioter_car_chose_button = Button(root, text="I DROVE THIS CAR!", width=200)
pioter_car_chose_button.grid(row=4, column=5, padx=0, pady=0,  columnspan=6)


next_drive = Button(root, text="Who Drive NEXT?", command=set,
                fg="red", font = "Verdana 14 underline",
                bd=2, bg="light blue", relief="groove",
                    width=100)
next_drive.grid(row=5, column=5, padx=0, pady=20,  columnspan=6)


root.mainloop()