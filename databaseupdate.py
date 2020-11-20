import sqlite3
import datetime
from sqlite3 import Error
dbfile="C:\Users\KCP\PycharmProjects\Python-Airline-Booking-System-master\TrainTicketBooking.db"
con = sqlite3.connect(dbfile)
cur = con.cursor()

#Create Tables
#cur.execute("drop Table Passengers_Info")

#cur.execute("CREATE TABLE User_Info(Email_Address VARCHAR(20) PRIMARY KEY UNIQUE, Password VARCHAR(20),First_Name VARCHAR(20),Last_Name VARCHAR(20), Mobile_No INT(10))")

#cur.execute("CREATE TABLE Train_Details(Train_No INT(3) PRIMARY KEY UNIQUE, Source_Station VARCHAR,Destination_Station VARCHAR,Date_of_Travel DATE, Departure_Time TIME, Arrival_Time TIME, Total_Travel_Time VARCHAR)")

#cur.execute("CREATE TABLE User_Tickets(Email_Address VARCHAR(20), Ticket_id INT(3))")

#cur.execute("CREATE TABLE Passengers_Info(Ticket_ID INT(3) PRIMARY KEY REFERENCES User_Tickets(Ticket_id), Train_No INT(3),Source VARCHAR, Destination VARCHAR, Journey_Date DATE, P1_Name VARCHAR(20), P1_Age INT(3), P1_Gender VARCHAR, P1_Category VARCHAR(10),"
             #"P2_Name VARCHAR(20), P2_Age INT(3), P2_Gender VARCHAR, P2_Category VARCHAR(10),"
             #"P3_Name VARCHAR(20), P3_Age INT(3), P3_Gender VARCHAR, P3_Category VARCHAR(10),"
             #"P4_Name VARCHAR(20), P4_Age INT(3), P4_Gender VARCHAR, P4_Category VARCHAR(10))")

#cur.execute("DROP Table User_Tickets")
#cur.execute("CREATE TABLE Passengers_Info(Ticket_ID INT(3) PRIMARY KEY REFERENCES User_Tickets(Ticket_id), Train_No INT(3),Source VARCHAR, Destination VARCHAR, Journey_Date DATE, P1_Name VARCHAR(20), P1_Age INT(3), P1_Gender VARCHAR, P1_Category VARCHAR(10))")



#cur.execute("CREATE TABLE Seats_Reserved(Email_Address VARCHAR(20), Train_No , Journey_Date DATE, Carriage_No VARCHAR(3), Seat_No INT(3), Reserved VARCHAR(3))")
#cur.execute("CREATE TABLE Ticket_Info(Ticket_id INT(3) PRIMARY KEY REFERENCES Passengers_Info(Ticket_id),Amount_Paid INT, Ticket_Valid VARCHAR(3))")

#cur.execute("CREATE TABLE Travel_Addons(Ticket_id INT(3) PRIMARY KEY REFERENCES Ticket_Info(Ticket_id), Dog_Onboard VARCHAR(3),Preorder_Food VARCHAR(3),Reserve_Seat VARCHAR(3), Reserve_Sleeping_Cart VARCHAR(3))")

cur.execute("INSERT INTO Train_Details(train_no,source_station,destination_station,date_of_travel, departure_time, arrival_time, total_travel_time) VALUES('124','Oslo','Bergen','2020/11/20','11:30:00','21:30:00','10 Hrs')")
con.commit()
cur.execute("SELEct * from Train_Details")
print(cur.fetchall())

cur.execute("SELEct * from Passengers_Info")
print(cur.fetchall())
cur.execute("SELEct * from User_Tickets")
print(cur.fetchall())

table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
print(table_list)
con.close()