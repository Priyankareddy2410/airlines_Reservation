import pymysql
import tkinter as tk
import administrator
import book_ticket
import reservations
import cancel_reservation
import create_tables

try:
    create_tables.tables()
except:
    pass

while True:
    #GUI 
    window = tk.Tk()

    entry_msg = tk.Label(window, text = 'Welcome To Online Airline Booking').grid(row=0,column=5)
    choice1 = tk.Label(window, text = '1 : Administrator').grid(row=1,column=0)
    choice2 = tk.Label(window, text = '2 : Book A Flight Ticket').grid(row=2,column=0)
    choice3 = tk.Label(window, text = '3 : Check Flight Reservation').grid(row=3,column=0)
    choice4 = tk.Label(window, text = '4 : Cancel Flight Reservation').grid(row=4,column=0)
    choice5 = tk.Label(window, text = '5 : Exit').grid(row=5,column=0)

    window.mainloop()
    
    
    choice= input('Enter your option : ')
    if choice=='1':
        administrator.admin()
    elif choice=='2':
        book_ticket.user()
    elif choice=='3':
        reservations.res()
    elif choice=='4':
        cancel_reservation.cancel_res()
    elif choice=='5':
        break
    else:
        print('**Please enter VALID input**')

#PLEASE NOTE TO EXECUTE THE PROGRAM MYSQL SERVER SHOULD BE LOGGED IN WITH PASSWORD
    
