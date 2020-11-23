import tkinter.ttk as tk
from tkMessageBox import showinfo, showerror
from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import random
import time
global Seat_No, P1_Name, P1_Age, P1_Gender, P1_Category
global email_id
global Ticket_id
global train_no
global Source
global destination
global Journey_Date
global Carriage
global Seat_No


dbfile = "TrainTicketBooking.db"
con = sqlite3.connect(dbfile)
cur = con.cursor()

def Control_Validation():
    def OK():
        window7.destroy()
        OptionDisplay()
    window7 = Tk()
    window7.title("Display Ticket Information")
    window7.config(bg="dark green")
    screen_width = window7.winfo_screenwidth()
    screen_height = window7.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window7.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window7.resizable(0, 0)


    cur.execute("SELECT ticket_ID from User_Tickets where Email_Address=(?)", (email_id,))
    result = cur.fetchall()
    for i in result:
        ticket = i
    print(ticket)
    cur.execute("SELECT * from Passengers_Info where ticket_id=(?)", ticket)
    ticket_details = cur.fetchall()
    tkt_details = str(ticket_details[0])
    tkt_details = tkt_details.split(',')
    tkt_details[0] = tkt_details[0].replace('(', '')
    tkt_details[2] = tkt_details[2].replace('u\'', '')
    tkt_details[2] = tkt_details[2].replace('\'', '')
    tkt_details[3] = tkt_details[3].replace('u\'', '')
    tkt_details[3] = tkt_details[3].replace('\'', '')
    tkt_details[4] = tkt_details[4].replace('u\'', '')
    tkt_details[4] = tkt_details[4].replace('\'', '')
    tkt_details[5] = tkt_details[5].replace('u\'', '')
    tkt_details[5] = tkt_details[5].replace('\'', '')
    tkt_details[8] = tkt_details[8].replace(')', '')
    tkt_details[8] = tkt_details[8].replace('u\'', '')
    tkt_details[8] = tkt_details[8].replace('\'', '')

    Label(window7, text="Ticket Booking Details", font=('Slab Serif', 17), bg='Orange').place(x=150,y=50)
    Label(window7, text="Ticket Number", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=100)
    Label(window7, text=tkt_details[0], font=('Slab Serif', 17), bg='Orange').place(x=350,y=100)
    Label(window7, text="Train Number", font=('Slab Serif', 17),fg="white", bg='dark green').place(x=150,y=150)
    Label(window7, text=tkt_details[1], font=('Slab Serif', 17), bg='Orange').place(x=350,y=150)
    Label(window7, text="Source", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=200)
    Label(window7, text=tkt_details[2], font=('Slab Serif', 17), bg='Orange').place(x=350,y=200)
    Label(window7, text="Destination", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=250)
    Label(window7, text=tkt_details[3], font=('Slab Serif', 17), bg='Orange').place(x=350,y=250)
    Label(window7, text="Date of journey", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=300)
    Label(window7, text=tkt_details[4], font=('Slab Serif', 17), bg='Orange').place(x=350,y=300)
    Label(window7, text="Passenger Name", font=('Slab Serif', 17),fg="white", bg='dark green').place(x=150,y=350)
    Label(window7, text=tkt_details[5], font=('Slab Serif', 17), bg='Orange').place(x=350,y=350)
    Label(window7, text="Age", font=('Slab Serif', 17),fg="white", bg='dark green').place(x=150,y=400)
    Label(window7, text=tkt_details[6], font=('Slab Serif', 17), bg='Orange').place(x=350,y=400)
    Label(window7, text="Gender", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=450)
    Label(window7, text=tkt_details[7], font=('Slab Serif', 17), bg='Orange').place(x=350,y=450)
    Label(window7, text="Category", font=('Slab Serif', 17), fg="white",bg='dark green').place(x=150,y=500)
    Label(window7, text=tkt_details[8], font=('Slab Serif', 17), bg='Orange').place(x=350,y=500)
    Button(window7, text="OK",font=('Slab Serif', 17), bg='grey',command=OK).place(x=150,y=550)
    Button(window7, text="Back", font=('Slab Serif', 17), bg='grey').place(x=250, y=550)
    window7.mainloop()


def Cancellation():
    def Cancel():
        def Back1():
            window9.destroy()
            Cancellation()

        def Confirm():
            #showinfo()
            showinfo('Ticket Cancellation', "Ticket is cancelled")
            #Label(window9, text="Ticket Reservation is cancelled", font=('Slab Serif', 17), bg='Orange').grid(row=3, column=0)

        window8.destroy()
        window9 = Tk()
        window9.config(bg="dark green")
        screen_width = window9.winfo_screenwidth()
        screen_height = window9.winfo_screenheight()
        width = 750
        height = 700
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window9.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window9.resizable(0, 0)
        Label(window9, text="Are you sure to cancel the reservation?", font=('Slab Serif', 17), bg='Orange').place(x=150,y=50)
        Button(window9, text="Confirm",font=('Slab Serif', 17), bg='grey', command=Confirm).place(x=250,y=100)
        Button(window9, text="Back", font=('Slab Serif', 17), bg='grey', command=Back1).grid(x=250,y=150)


    def Change():
        window8.destroy()

    def Back():
        window8.destroy()
        OptionDisplay()

    global email_id
    window8 = Tk()
    window8.title("Cancel/Change Ticket")
    screen_width = window8.winfo_screenwidth()
    screen_height = window8.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window8.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window8.resizable(0, 0)
    window8.config(bg='dark green')

    cur.execute("SELECT email_address from User_info where email_address=(?)", (email_id,))
    result = cur.fetchall()
    for i in result:
        email = i

    #print(email)
    email = str(email)
    email = email.replace('(','')
    email = email.replace(')', '')
    email = email.replace(',', '')
    email = email.replace('u\'', '')
    email = email.replace('\'', '')

    cur.execute("SELECT Ticket_Id from User_tickets where email_address=(?)", (email,))
    ticket = cur.fetchall()
    ticket = str(ticket)
    ticket = ticket.replace('(','')
    ticket = ticket.replace(')','')
    ticket = ticket.replace(',','')
    ticket = ticket.replace('[', '')
    ticket = ticket.replace(']', '')

    cur.execute("SELECT Train_No,Source,Destination,Journey_date,P1_Name,P1_Age,P1_Gender,P1_Category from Passengers_info where ticket_id=(?)",(ticket,))

    result = cur.fetchall()
    tkt_info = str(result[0])
    tkt_info = tkt_info.split(',')
    tkt_info[0] = tkt_info[0].replace('(', '')
    tkt_info[1] = tkt_info[1].replace('u\'', '')
    tkt_info[1] = tkt_info[1].replace('\'', '')
    tkt_info[2] = tkt_info[2].replace('u\'', '')
    tkt_info[2] = tkt_info[2].replace('\'', '')
    tkt_info[3] = tkt_info[3].replace('u\'', '')
    tkt_info[3] = tkt_info[3].replace('\'', '')
    tkt_info[4] = tkt_info[4].replace('u\'', '')
    tkt_info[4] = tkt_info[4].replace('\'', '')
    tkt_info[7] = tkt_info[7].replace('u\'', '')
    tkt_info[7] = tkt_info[7].replace('\'', '')

    print(tkt_info)

    Label(window8, text="Ticket Booking Details ", font=('Slab Serif', 17), bg='Orange').place(x=150,y=50)
    Label(window8, text="Train Number", font=('Slab Serif', 17), bg='Orange').place(x=150,y=100)
    Label(window8, text=tkt_info[0], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=100)
    Label(window8, text="Source", font=('Slab Serif', 17), bg='Orange').place(x=150,y=150)
    Label(window8, text=tkt_info[1], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=150)
    Label(window8, text="Destination", font=('Slab Serif', 17), bg='Orange').place(x=150,y=200)
    Label(window8, text=tkt_info[2], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=200)
    Label(window8, text="Date of journey", font=('Slab Serif', 17), bg='Orange').place(x=150,y=250)
    Label(window8, text=tkt_info[3], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=250)
    Label(window8, text="Passenger Name", font=('Slab Serif', 17), bg='Orange').place(x=150,y=300)
    Label(window8, text=tkt_info[4], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=300)
    Label(window8, text="Age", font=('Slab Serif', 17), bg='Orange').place(x=150,y=350)
    Label(window8, text=tkt_info[5], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=350)
    Label(window8, text="Gender", font=('Slab Serif', 17), bg='Orange').place(x=150,y=400)
    Label(window8, text=tkt_info[6], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=400)
    Label(window8, text="Category", font=('Slab Serif', 17), bg='Orange').place(x=150,y=450)
    Label(window8, text=tkt_info[7], font=('Slab Serif', 17), fg="white",bg='dark green').place(x=400,y=450)

    Button(window8, text="Cancel Reservation", font=('Slab Serif', 17), bg='grey', command=Cancel).place(x=200,y=500,height=30)
    Button(window8, text="Change Reservation", font=('Slab Serif', 17), bg='grey', command=Change).place(x=200,y=550,height=30)
    Button(window8, text="Back", font=('Slab Serif', 17), bg='grey', command=Back).place(x=270,y=600,height=30)
    window8.mainloop()


def Show_Ticket_Info():
    global Ticket_id, Source, destination, Journey_Date

    window6 = Tk()
    window6.title("Ticket Booking Confirmation")
    window6.config(bg="dark green")
    screen_width = window6.winfo_screenwidth()
    screen_height = window6.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window6.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window6.resizable(0, 0)

    print(Ticket_id, Source, destination,  Journey_Date)
    Label(window6, text="Ticket Booking Confirmation", font=('Slab Serif', 17), fg="white",bg='dark blue').place(x=170,y=30)
    Label(window6, text="Ticket ID", font=('Slab Serif', 17), fg="white", bg='dark green').place(x=150,y=80)
    Label(window6, text=Ticket_id, font=('Slab Serif', 17), fg="white",bg='dark blue').place(x=350,y=80)
    Label(window6, text="Source Station", font=('Slab Serif', 17), fg="white", bg='dark green').place(x=150, y=130)
    Label(window6, text=Source, font=('Slab Serif', 17),fg="white", bg='dark blue').place(x=350,y=130)
    Label(window6, text="Destination Station", font=('Slab Serif', 17), fg="white", bg='dark green').place(x=150, y=180)
    Label(window6, text=destination, font=('Slab Serif', 17), fg="white",bg='dark blue').place(x=350,y=180)
    Label(window6, text="Journey Date", font=('Slab Serif', 17), fg="white", bg='dark green').place(x=150, y=230)
    Label(window6, text=Journey_Date, font=('Slab Serif', 17), fg="white",bg='dark blue').place(x=350,y=230)
    window6.mainloop()

def Payment():
    def Method():

        def Ticket_Book_VIPPS():
            global train_no, Ticket_id, Source, destination, Journey_Date, P1_Name, P1_Gender, P1_Category, P1_Age
            global email_id
            print(email_id)
            if len(VIPPS_ID.get()) == 0:
                showerror('Error', "Enter VIPPS ID")
            else:
                showinfo('Ticket Confirmation', "Ticket is booked")
                #window5.destroy()

                n = random.randint(1000, 10000)
                #cur.execute("CREATE TABLE Passengers_Info(Ticket_ID INT(3) , Train_No ,Source , Destination , Journey_Date DATE, P1_Name , P1_Age INT(3), P1_Gender, P1_Category"
                Ticket_id = n
                global email_id
                cur.execute("INSERT INTO User_Tickets VALUES (?,?)", (email_id, Ticket_id,))
                cur.execute("INSERT INTO Passengers_Info VALUES(?,?,?,?,?,?,?,?,?)",(Ticket_id,train_no,Source,destination,Journey_Date,P1_Name,P1_Age,P1_Gender,P1_Category,))
                con.commit()
                Show_Ticket_Info()

        def Ticket_Book_Card():
                if len(Card_Number.get()) == 0:
                    showerror('Error', "Enter Card Number")
                else:
                    showinfo('Ticket Confirmation', "Ticket is booked")
                    #window5.destroy()
                    Show_Ticket_Info()

        def Cancel():
            window5.destroy()

        if (dropVar.get() == "VIPPS"):
            Label(window5, text="Provide the VIPPS details ", font=('Slab Serif', 17), bg='dark green',fg="white").place(x=150,y=220)
            Label(window5, text="VIPPS ID*", font=('Slab Serif', 17), fg="black", bg="dark orange").place(x=180,y=270)
            VIPPS_ID = Entry(window5)
            VIPPS_ID.place(x=320, y=270, height=30)
            Button(window5, text="OK",font=('Slab Serif', 15), command=Ticket_Book_VIPPS).place(x=230,y=320,height=30)

        elif(dropVar.get() == "Debit"):
            Label(window5, text="Please provide the Debit/Credit Card details ", font=('Slab Serif', 17), bg='dark green',fg="white").place(x=150,y=220)
            Label(window5, text="Card Number*", font=('Slab Serif', 17), fg="black", bg="dark orange").place(x=180, y=270)
            Label(window5, text="Card Expiry", font=('Slab Serif', 17), fg="black", bg="dark orange").place(x=180,y=320)
            Label(window5, text="Card CVV", font=('Slab Serif', 17), fg="black", bg="dark orange").place(x=180, y=370)
            Card_Number = Entry(window5)
            Card_Number.place(x=380, y=270,height=30)
            Card_expiry = Entry(window5)
            Card_expiry.place(x=380, y=320, height=30)
            Cvv = Entry(window5)
            Cvv.place(x=380, y=370, height=30)

            Button(window5, text="OK", font=('Slab Serif', 15),command=Ticket_Book_Card).place(x=180, y=420)
            Button(window5, text="Cancel",font=('Slab Serif', 15), command=Cancel).place(x=280, y=420)
        #window5.destroy()
    #showinfo('Seat Confirmed','SEAT IS RESERVED')

    #print(Seat_No,Carriage)
    global Ticket_id, Source, destination, Journey_Date
    window5 = Tk()

    window5.title("Payment Details")
    window5.config(bg="dark green")
    screen_width = window5.winfo_screenwidth()
    screen_height = window5.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window5.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window5.resizable(0, 0)

    Label(window5, text="How do you want to pay?", font=('Slab Serif', 17),fg="black", bg='dark orange').place(x=180,y=50)
    optionList = ["VIPPS", "Debit"]
    dropVar = StringVar(window5)
    dropVar.set("Select Payment Method")  # default choice
    dropMenu1 = OptionMenu(window5, dropVar, *optionList)
    dropMenu1.place(x=200,y=100,height=30)
    Button(window5, text="OK",font=('Slab Serif', 15),fg="black", command=Method).place(x=210,y=150,height=30)
    window5.mainloop()

def PassengerDetails():
    #window1.destroy()
    window2 = Tk()
    window2.title("Passenger Details")
    window2.config(bg="dark green")
    screen_width = window2.winfo_screenwidth()
    screen_height = window2.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window2.resizable(0, 0)


    for i in range(5):
        e = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="grey")
        e.grid(row=0, column=i)
        if i == 0:
            e.insert(10, "S.No")
        elif i == 1:
            e.insert(10, "Name")
        elif i == 2:
            e.insert(10, "Age")
        elif i == 3:
            e.insert(10, "Gender")
        elif i == 4:
            e.insert(10, "Category")

    j = 1
    for j in range(5):
        for k in range(5):
            if j == 1 and k == 0:
                s1 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                s1.grid(row=j, column=k)
                s1.insert(10, '1')

            elif j == 1 and k == 1:
                p1 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                p1.grid(row=j, column=k)

            elif j == 1 and k == 2:
                a1 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                a1.grid(row=j, column=k)

            elif j == 1 and k == 3:
                g1 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                g1.grid(row=j, column=k)

            elif j == 1 and k == 4:
                c1 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                c1.grid(row=j, column=k)

            elif j == 2 and k == 0:
                s2 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                s2.grid(row=j, column=k)
                s2.insert(10, '2')

            elif j == 2 and k == 1:
                p2 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                p2.grid(row=j, column=k)

            elif j == 2 and k == 2:
                a2 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                a2.grid(row=j, column=k)

            elif j == 2 and k == 3:
                g2 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                g2.grid(row=j, column=k)

            elif j == 2 and k == 4:
                c2 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                c2.grid(row=j, column=k)

            elif j == 3 and k == 0:
                s3 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                s3.grid(row=j, column=k)
                s3.insert(10, '3')

            elif j == 3 and k == 1:
                p3 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                p3.grid(row=j, column=k)

            elif j == 3 and k == 2:
                a3 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                a3.grid(row=j, column=k)

            elif j == 3 and k == 3:
                g3 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                g3.grid(row=j, column=k)

            elif j == 3 and k == 4:
                c3 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                c3.grid(row=j, column=k)

            elif j == 4 and k == 0:
                s4 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                s4.grid(row=j, column=k)
                s4.insert(10, '4')

            elif j == 4 and k == 1:
                p4 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                p4.grid(row=j, column=k)

            elif j == 4 and k == 2:
                a4 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                a4.grid(row=j, column=k)

            elif j == 4 and k == 3:
                g4 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                g4.grid(row=j, column=k)

            elif j == 4 and k == 4:
                c4 = Entry(window2, width=20, justify="center", font=('Slab Serif', 10), bg="white")
                c4.grid(row=j, column=k)

    #v2 = StringVar(window2)
    #gender = {'Male', 'Female'}
    #v2.set('Select')
    #popupMenu1 = OptionMenu(window2, v2, *gender)
    #popupMenu1.config(font=('Slab Serif', 7), bg="grey", fg='black')
    #popupMenu1.grid(row=1, column=3)

    def ReserveSeat():
        def ReserveYes():
            Label(window4, text="Choose a seat to reserve", font=('Slab Serif', 15),bg='dark green',fg="white").place(x=200,y=170)
            Label(window4, text="Select the Train Carriage", font=("Slab Serif", 15), fg="black",bg="dark orange").place(x=150,y=220)
            carriage_no = StringVar(window4)
            carriage_no.set("Select Carriage")  # default value
            w1 = OptionMenu(window4, carriage_no, "C1", "C2", "C3")
            w1.place(x=400, y=220,height=30)
            Label(window4, text="Select Seat Number", font=("Slab Serif", 15), fg="black",bg="dark orange").place(x=200, y=270)
            seat = StringVar(window4)
            seat.set("Select Seat")  # default value
            w2 = OptionMenu(window4, seat, "1", "2", "3")
            w2.place(x=400, y=270, height=30)

            def Seat_Selection():
                global Seat_No, train_no, Journey_Date, email_id
                Seat_No = seat.get()
                global Carriage
                Carriage = carriage_no.get()
                cur.execute("INSERT INTO Seats_Reserved VALUES (?,?,?,?,?,'YES')",(email_id, train_no, Journey_Date, Carriage, Seat_No,))
                con.commit()
                # Seats_Reserved(Train_No ), Journey_Date , Carriage_No , Seat_No , Reserved
                showinfo('Seat Reserved', "Seat is Reserved")

                Payment()

            def Back():
                window4.destroy()

            Button(window4, text='Confirm Reserve Seat', bg="grey", font=('Slab Serif', 15), command=Seat_Selection).place(x=170,y=330, height=30)
            Button(window4, text='Cancel', bg="grey", font=('Slab Serif', 15),command=Back).place(x=400, y=330, height=30)

        window2.destroy()
        window4 = Tk()

        window4.title("Seat Reservation")
        window4.config(bg="dark green")
        screen_width = window4.winfo_screenwidth()
        screen_height = window4.winfo_screenheight()
        width = 750
        height = 700
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window4.resizable(0, 0)

        Label(window4, text="Do you wish to reserve a seat for journey", font=('Slab Serif', 15), bg='dark orange',fg="black").place(x=150,y=70)
        Button(window4, text='Yes', bg="grey", font=('Slab Serif', 11), command=ReserveYes).place(x=250,y=120, height=30)
        Button(window4, text='No', bg="grey", font=('Slab Serif', 11), command=Payment).place(x=300,y=120,height=30)
        window4.mainloop()

    def Validate():
        global P1_Name, P1_Age, P1_Gender, P1_Category

        print(p1.get(), a1.get(), g1, c1.get())
        if len(p1.get()) == 0 or len(a1.get()) == 0 or g1.get() == 'Select' or len(c1.get()) == 0:
            showinfo('Error', 'enter all required fields!')
        else:
            P1_Name = p1.get()
            P1_Age = a1.get()
            P1_Gender = g1.get()
            P1_Category = c1.get()
            ReserveSeat()

    def Back():
        window2.destroy()
        #PassengerDetails()

    b = Button(window2, text='Proceed', bg="grey", font=('Slab Serif', 11), command=Validate)
    b.place(x=250, y=155, width=100)
    b = Button(window2, text='Back', bg="grey", font=('Slab Serif', 11), command=Back)
    b.place(x=350, y=155, width=100)

    window2.mainloop()


def OptionDisplay():
    def Cancel():
        window1.destroy()
        Cancellation()
    def Purchase():
        window1.destroy()
        PurchaseTicket()
    def Reserve():
        window1.destroy()
    def Control():
        window1.destroy()
        Control_Validation()
    #def callback():
    #    window1.destroy()
    #    Welcome_Page()

    global email_id
    window1 = Tk()
    window1.title("Choice ")
    window1.config(bg="dark green")
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window1.resizable(0, 0)

    #email_id = email_address.get()
    print("emailid" + str(email_id))
    Label(window1, text="What do you want to do? Choose an option", font=('Slab Serif', 17), fg="black",bg='dark orange').place(x=130,y=50)
    Button(window1, text="Purchase Ticket", bg="grey", font=('Slab Serif',11), command=Purchase).place(x=200,y=150,height=30)
    Button(window1, text="Reserve Seats", bg="grey", font=('Slab Serif', 11), command=Reserve).place(x=350,y=150,height=30)
    Button(window1, text="Cancel/Change Ticket", bg="grey", font=('Slab Serif', 11), command=Cancel).place(x=150,y=200,height=30)
    Button(window1, text="Show Ticket for Control/Validation", bg="grey", font=('Slab Serif', 11), command=Control).place(x=350,y=200,height=30)

    logout=Label(window1, text="Log Out", fg="dark blue",bg="grey",font=('Slab Serif', 13), cursor="hand2")
    logout.pack()
    logout.place(x=650,y=3)
    #logout.bind(callback)


def PurchaseTicket():
    def Back():
        root1.destroy()
        OptionDisplay()

    def Check():
        print(to_station.get(), from_station.get(), cal.get())
        if to_station.get()=='Select Destination' or from_station.get() == 'Select Source':
            showinfo('Error', 'enter all required fields!')
        else:
                cur.execute("SELECT * FROM train_details where source_station=(?) and destination_station=(?) and date_of_travel=(?)",(from_station.get(),to_station.get(),cal.get(),))

                if cur.fetchall()==[]:
                    showinfo('Error', 'Sorry Train Unavailable!')
                else:
                    # root1.destroy()
                    Search()

    def Search():
        global x1

        window1 = Tk()
        window1.title("RAILWAY SCHEDULE")
        window1.config(bg='dark green')
        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()
        width = 1350
        height = 700
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window1.resizable(0, 0)

        height = 5
        width = 7

        e1 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e2 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e3 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e4 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e5 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e6 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")
        e7 = Entry(window1, justify="center", font=('Slab Serif', 11), bg="grey", fg="black")

        e1.grid(row=0,column=0)
        e2.grid(row=0, column=1)
        e3.grid(row=0, column=2)
        e4.grid(row=0, column=3)
        e5.grid(row=0, column=4)
        e6.grid(row=0, column=5)
        e7.grid(row=0,column=6)

        e1.insert(10, "Train number")
        e2.insert(10, "Source")
        e3.insert(10, "Destination")
        e4.insert(10, "Date of Travel")
        e5.insert(10, "Departure Time")
        e6.insert(10, "Arrival Time")
        e7.insert(10, "Travel Time")

        cur.execute(
            "SELECT * FROM train_details where source_station=(?) and destination_station=(?) and date_of_travel=(?)", (from_station.get(), to_station.get(), cal.get(),))

        #cur.execute("SELECT * FROM train_details where ")
        i = 1
        for entry in cur:
            for j in range(len(entry)):
                e = Entry(window1, width=10, fg='black',bg="dark orange",font=('Slab Serif', 11))
                e.grid(row=i, column=j)
                e.insert(END, entry[j])
                if j == 0:
                    global train_no
                    train_no=entry[j]
                elif j == 1:
                    global Source
                    Source=entry[j]
                elif j == 2:
                    global destination
                    destination=entry[j]
                elif j == 3:
                    global Journey_Date
                    Journey_Date=entry[j]

            i = i + 1

        #train_no=cur[0]
        #Source=cur[1]

        print("Source" + str(train_no))

        button1 = Button(window1, text="Book", font=('Slab Serif', 11), width=10, bg="grey",command=PassengerDetails)
        button1.grid(row=1, column=7)
        #button2 = Button(window1, text="Book", font=('Slab Serif', 9), width=10, bg="grey")
        #button2.grid(row=2, column=7)


    #root.destroy()
    #window1.destroy()
    root1 = Tk()
    root1.title("Search Trains")
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    width = 750
    height = 700
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root1.resizable(0, 0)
    root1.config(bg='dark green')

    #Label(root1, text="Welcome to NorwegianRails Booking System", font=("Slab Serif", 17), fg="black", width=46).grid(row=0, column=0, columnspan=4)
    Label(root1, text="Where do you want to travel?", font=("Slab Serif", 17), fg="white",bg="dark green", width=46).place(x=100,y=50)
    Label(root1, text="Departure Station", font=("Slab Serif", 15), fg="black",bg="dark orange").place(x=100, y=100)
    from_station = StringVar(root1)
    from_station.set("Select Source")  # default value
    w = OptionMenu(root1, from_station, "Oslo", "Bergen", "Kristiansand", "Stavanger")
    w.place(x=300,y=100)
    Label(root1, text="Arrival Station", font=("Slab Serif", 15), fg="black",bg="dark orange").place(x=100, y=150)
    to_station = StringVar(root1)
    to_station.set("Select Destination")  # default value
    w = OptionMenu(root1, to_station, "Oslo", "Bergen", "Kristiansand", "Stavanger")
    w.place(x=300, y=150)
    Label(root1, text="Date of Travel", font=("Slab Serif", 14), fg="black",bg="dark orange").place(x=100, y=200)
    cal = DateEntry(root1, width=10, bg="dark blue", fg="white", year=2020, date_pattern = 'yyyy/mm/dd')
    cal.place(x=300,y=200)

    Button(root1, text="Search trains", font=('Slab Serif', 15), bg="grey", fg="black", command=Check).place(x=250,y=300,height=30)
    Button(root1, text="Back", font=('Slab Serif', 15), bg="grey", fg="black", command=Back).place(x=400,y=300,height=30)

def LoginCheck():
    global email_id
    cur.execute("SELECT email_address,password from User_Info where email_address=(?) and Password=(?)", (email_address.get(), password.get(),))
    a = cur.fetchall()
    if(a != []):
        #showinfo('login result', 'LOGIN SUCCESSFUL')
        email_id = email_address.get()
        root.destroy()
        OptionDisplay()
    else:
        showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

def SignUp():
    def Back():
        root1.destroy()
        Welcome_Page()

    def success():
        email = email_id.get()
        cur.execute("select email_address from User_Info where email_address=(?)", (email,))
        a = cur.fetchall()
        if a != []:
            showerror('Error', "User Already Exists")
        else:
            l = (email_id.get(), passw.get(), first_name.get(), last_name.get(), phone_number.get())
            cur.execute("insert into User_Info values(?,?,?,?,?)", l)
            showinfo('Signed Up', "Congratulations You are Successfully Signed Up")
            con.commit()
            email_id.delete(0, 20)
            first_name.delete(0, 20)
            last_name.delete(0, 20)
            phone_number.delete(0, 10)
            passw.delete(0, 20)
            root1.destroy()
            Welcome_Page()
    #root.destroy()
    root1 = Tk()
    root1.title("Sign Up")
    root1.configure(bg='dark green')

    root1.geometry('%dx%d+%d+%d' % (700, 750,333, 9))
    Label(root1, text="Welcome to NorwegianRails", font=("Slab Serif", 18), fg="white", width=46,bg="blue").place(x=40, y=20)
    Label(root1, text="Kindly provide the below details to Sign Up", font=("Slab Serif", 15), fg="white",bg="dark green", width=46).place(x=80,y=70)
    Label(root1, text="Email_Address*", font=("Slab Serif", 15), fg="black",bg="dark orange").place(x=150, y=120)
    email_id = Entry(root1, font=('Slab_Serif', 10))
    email_id.place(x=320, y=120, height=30)
    Label(root1, text="First Name", font=("Slab Serif", 15), fg="black", bg="dark orange").place(x=150, y=170)
    first_name = Entry(root1, font=('Slab_Serif', 10))
    first_name.place(x=320, y=170, height=30)
    Label(root1, text="Last Name", font=("Slab Serif", 15), fg="black", bg="dark orange").place(x=150, y=220)
    last_name = Entry(root1, font=('Slab_Serif', 10))
    last_name.place(x=320, y=220, height=30)
    Label(root1, text="Phone Number", font=("Slab Serif", 15), fg="black", bg="dark orange").place(x=150, y=270)
    phone_number = Entry(root1, font=('Slab_Serif', 10))
    phone_number.place(x=320, y=270, height=30)
    Label(root1, text="Password", font=("Slab Serif", 15), fg="black", bg="dark orange").place(x=150, y=320)
    passw = Entry(root1, show="*",font=('Slab_Serif', 10))
    passw.place(x=320, y=320, height=30)
    Button(root1, text="Sign Up", fg="black", bg="grey", font=("Slab Serif", 15), command=lambda: success()).place(x=250, y=370)
    Button(root1, text="Back", fg="black", bg="grey", font=("Slab Serif", 15), command=Back).place(x=350, y=370)
    root1.mainloop()

#Welcome Page Login and SignUp buttons

def Welcome_Page():
    def Register():
        root.destroy()
        SignUp()
    global root
    root = Tk()
    root.title("Railway reservation")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 700
    height = 750
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    print("screen width " + str(screen_height) +" "+str(screen_height)+" " + str(x) +" " +str(y))
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    canvas = Canvas(root, width=width, height=height)
    canvas.config(bg='dark green')
    canvas.pack()

    my_image = PhotoImage(file='Railways_Image1.gif')
    my_img = canvas.create_image(0, 0, anchor=NW, image=my_image)

    Label(root, text="NorwegianRails", font=('Slab Serif', 18), fg='white', bg='blue').place(x=250, y=80)
    Label(root, text="Email ID", font=('Slab Serif', 15), fg='black',bg='dark orange').place(x=160, y=500)
    Label(root, text="Password", font=('Slab Serif', 15), fg='black',bg='dark orange').place(x=160, y=550)
    global email_address, password
    email_address = Entry(root, font=('Slab Serif', 10))
    email_address.place(x=290, y=500, height=30)
    password = Entry(root, font=('Slab Serif', 10), show="*")
    password.place(x=290, y=550, height=30)

    Button(root, text="Login", font=('Slab Serif',15), bg='grey', fg='black', command=LoginCheck).place(x=220, y=600)
    Button(root, text="Register", font=('Slab Serif',15), bg='grey', fg='black', command=Register).place(x=320, y=600)
    root.mainloop()

Welcome_Page()
