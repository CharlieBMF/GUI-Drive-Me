from tkinter import *
from tkcalendar import Calendar
from datetime import date
import base64
from PIL import ImageTk, Image
import backend


def confirm_calendar_day():
    result = backend.check_calendar_day(cal.selection_get())
    show_day_info(result['car_karol'], result['car_pioter'])


def show_day_info(car_karol='No info', car_pioter='No info'):
    choosen_date_text.config(text=cal.selection_get())
    car_karol_text.config(text=car_karol)
    car_pioter_text.config(text=car_pioter)


def karol_ride_info_insert():
    backend.insert_ride_info(cal.selection_get(), var1.get(), driver='Karol')


def pioter_ride_info_insert():
    backend.insert_ride_info(cal.selection_get(), var2.get(), driver='Pioter')


def calculate_statistic():
    rides_calculation = backend.calculate_drives()
    update_drive_next_info(rides_calculation)


def update_drive_next_info(rides_calculation):
    all_rides_karol = rides_calculation['all_rides_karol']
    all_rides_pioter = rides_calculation['all_rides_pioter']
    month_rides_karol = rides_calculation['month_rides_karol']
    month_rides_pioter = rides_calculation['month_rides_pioter']
    rides_gap = abs(all_rides_karol-all_rides_pioter)

    who_drive_next_karol_month_text.config(text=month_rides_karol)
    who_drive_next_pioter_month_text.config(text=month_rides_pioter)
    who_drive_next_karol_all_text.config(text=all_rides_karol)
    who_drive_next_pioter_all_text.config(text=all_rides_pioter)
    if all_rides_karol > all_rides_pioter:
        who_drive_next_final_label.config(text=f'Karol is {rides_gap} rides ahead\n\n\n NEXT DRIVE FOR PIOTER')
    elif all_rides_karol < all_rides_pioter:
        who_drive_next_final_label.config(text=f'Pioter is {rides_gap} rides ahead\n\n\n NEXT DRIVE FOR KAROL')
    else:
        who_drive_next_final_label.config(text='SAME RIDES AMOUNT')


root = Tk()
root.title('DriveMe')
root.geometry("1800x800")

cal = Calendar(root,
               selectmode='day',
               year=int(date.today().strftime('%Y %m %y').split()[0]),
               month=int(date.today().strftime('%d %m %y').split()[1]),
               day=int(date.today().strftime('%d %m %y').split()[1])
               )
cal.grid(row=0, column=0, padx=20, pady=20, columnspan=4, rowspan=5)

get_date_button = Button(root, text="GET THIS DATE INFO", command=confirm_calendar_day)
get_date_button.grid(row=5, column=1, padx=0, pady=0)

choosen_date_label = Label(root, text='Chosen Date:')
choosen_date_label.grid(row=6, column=0, padx=2, pady=10)
choosen_date_text = Label(root, text='No data')
choosen_date_text.grid(row=6, column=1, padx=2, pady=10)
car_karol_label = Label(root, text='Karol Drove by:')
car_karol_label.grid(row=7, column=0, padx=2, pady=10)
car_karol_text = Label(root, text='No data')
car_karol_text.grid(row=7, column=1, padx=2, pady=10)
car_pioter_label = Label(root, text='Pioter Drove by:')
car_pioter_label.grid(row=8, column=0, padx=2, pady=10)
car_pioter_text = Label(root, text='No data')
car_pioter_text.grid(row=8, column=1, padx=2, pady=10)

karol_label = Label(root, text='Pan Karol')
karol_label.grid(row=1, column=5, padx=50, pady=10)

var1 = IntVar()
clio_img_karol = Image.open("clio.png")
clio_img_karol = clio_img_karol.resize((int(clio_img_karol.size[0]/5), int(clio_img_karol.size[1]/5)))
clio_img_karol = ImageTk.PhotoImage(clio_img_karol)
car_clio_button_karol = Radiobutton(root, image=clio_img_karol, variable=var1, value=1)
car_clio_button_karol.grid(row=1, column=6)
mercedes_img_karol = Image.open("mercedes.png")
mercedes_img_karol = mercedes_img_karol.resize((int(mercedes_img_karol.size[0]/5), int(mercedes_img_karol.size[1]/5)))
mercedes_img_karol = ImageTk.PhotoImage(mercedes_img_karol)
car_mercedes_button_karol = Radiobutton(root, image=mercedes_img_karol, variable=var1, value=2)
car_mercedes_button_karol.grid(row=1, column=7)
seat_img_karol = Image.open("seat.png")
seat_img_karol = seat_img_karol.resize((int(seat_img_karol.size[0]/5), int(seat_img_karol.size[1]/5)))
seat_img_karol = ImageTk.PhotoImage(seat_img_karol)
car_seat_button_karol = Radiobutton(root, image=seat_img_karol, variable=var1, value=3)
car_seat_button_karol.grid(row=1, column=8)
toyota_img_karol = Image.open("toyota.png")
toyota_img_karol = toyota_img_karol.resize((int(toyota_img_karol.size[0]/5), int(toyota_img_karol.size[1]/5)))
toyota_img_karol = ImageTk.PhotoImage(toyota_img_karol)
car_toyota_button_karol = Radiobutton(root, image=toyota_img_karol, variable=var1, value=4)
car_toyota_button_karol.grid(row=1, column=9)
yamaha_img_karol = Image.open("yamaha.png")
yamaha_img_karol = yamaha_img_karol.resize((int(yamaha_img_karol.size[0]/5), int(yamaha_img_karol.size[1]/5)))
yamaha_img_karol = ImageTk.PhotoImage(yamaha_img_karol)
car_yamaha_button_karol = Radiobutton(root, image=yamaha_img_karol, variable=var1, value=5)
car_yamaha_button_karol.grid(row=1, column=10)

karol_car_chose_button = Button(root, text="UPDATE INFO FOR KAROL", width=200, command=karol_ride_info_insert)
karol_car_chose_button.grid(row=2, column=5, padx=0, pady=0,  columnspan=6)

pioter_label = Label(root, text='Pan Pioter')
pioter_label.grid(row=3, column=5, padx=50, pady=10)

var2 = IntVar()
clio_img_pioter = Image.open("clio.png")
clio_img_pioter = clio_img_pioter.resize((int(clio_img_pioter.size[0]/5), int(clio_img_pioter.size[1]/5)))
clio_img_pioter = ImageTk.PhotoImage(clio_img_pioter)
car_clio_button_pioter = Radiobutton(root, image=clio_img_pioter, variable=var2, value=1)
car_clio_button_pioter.grid(row=3, column=6)
mercedes_img_pioter = Image.open("mercedes.png")
mercedes_img_pioter = mercedes_img_pioter.resize((int(mercedes_img_pioter.size[0]/5), int(mercedes_img_pioter.size[1]/5)))
mercedes_img_pioter = ImageTk.PhotoImage(mercedes_img_pioter)
car_mercedes_button_pioter = Radiobutton(root, image=mercedes_img_pioter, variable=var2, value=2)
car_mercedes_button_pioter.grid(row=3, column=7)
seat_img_pioter = Image.open("seat.png")
seat_img_pioter = seat_img_pioter.resize((int(seat_img_pioter.size[0]/5), int(seat_img_pioter.size[1]/5)))
seat_img_pioter = ImageTk.PhotoImage(seat_img_pioter)
car_seat_button_pioter = Radiobutton(root, image=seat_img_pioter, variable=var2, value=3)
car_seat_button_pioter.grid(row=3, column=8)
toyota_img_pioter = Image.open("toyota.png")
toyota_img_pioter = toyota_img_pioter.resize((int(toyota_img_pioter.size[0]/5), int(toyota_img_pioter.size[1]/5)))
toyota_img_pioter = ImageTk.PhotoImage(toyota_img_pioter)
car_toyota_button_pioter = Radiobutton(root, image=toyota_img_pioter, variable=var2, value=4)
car_toyota_button_pioter.grid(row=3, column=9)
yamaha_img_pioter = Image.open("yamaha.png")
yamaha_img_pioter = yamaha_img_pioter.resize((int(yamaha_img_pioter.size[0]/5), int(yamaha_img_pioter.size[1]/5)))
yamaha_img_pioter = ImageTk.PhotoImage(yamaha_img_pioter)
car_yamaha_button_pioter = Radiobutton(root, image=yamaha_img_pioter, variable=var2, value=5)
car_yamaha_button_pioter.grid(row=3, column=10)

pioter_car_chose_button = Button(root, text="UPDATE INFO FOR PIOTER", width=200, command=pioter_ride_info_insert)
pioter_car_chose_button.grid(row=4, column=5, padx=0, pady=0,  columnspan=6)

who_drive_next = Button(root, text="Who Drive NEXT?", command=calculate_statistic,
                        fg="red", font="Verdana 14 underline",
                        bd=2, bg="light blue", relief="groove",
                        width=100)

who_drive_next.grid(row=5, column=5, padx=0, pady=20,  columnspan=6)
who_drive_next_month_label = Label(root, text='This Month')
who_drive_next_month_label.grid(row=6, column=7)
who_drive_next_all_label = Label(root, text='All Rides')
who_drive_next_all_label.grid(row=6, column=8)
who_drive_next_karol_label = Label(root, text='Pan Karol')
who_drive_next_karol_label.grid(row=7, column=6)
who_drive_next_pioter_label = Label(root, text='Pan Pioter')
who_drive_next_pioter_label.grid(row=8, column=6)

who_drive_next_karol_month_text = Label(root, text='No data')
who_drive_next_karol_month_text.grid(row=7, column=7)
who_drive_next_pioter_month_text = Label(root, text='No data')
who_drive_next_pioter_month_text.grid(row=8, column=7)
who_drive_next_karol_all_text = Label(root, text='No data')
who_drive_next_karol_all_text.grid(row=7, column=8)
who_drive_next_pioter_all_text = Label(root, text='No data')
who_drive_next_pioter_all_text.grid(row=8, column=8)

who_drive_next_final_label = Button(root, text='Final result', fg="red",
                                    font="Verdana 14 underline", bd=2,
                                    bg="light blue", relief="groove",
                                    width=20, height=10)
who_drive_next_final_label.grid(row=6, column=8, rowspan=3, columnspan=3)

root.mainloop()
