import sys
import pymysql

def tables():
    #Open Database connection
    conn=pymysql.connect(host='localhost',user='root',password='summer7')

    #Prepare a cursor object using the cursor() method
    crsr=conn.cursor()

    crsr.execute('create database airlines')

    crsr.execute('use airlines')            

    #Create FLIGHT_CHART Table
    crsr.execute("CREATE TABLE FLIGHT_CHART (S_NO INT(5) NOT NULL AUTO_INCREMENT, Flight_Number VARCHAR(10) NOT NULL, Departure_From VARCHAR(20) NOT NULL, Arrival_To VARCHAR(20) NOT NULL, Departure_Time TIME NOT NULL, Arrival_Time TIME NOT NULL, Business_Seats INT(5) NOT NULL, Business_Fare FLOAT(10,2) NOT NULL, Economy_Seats INT(5) NOT NULL, Economy_Fare FLOAT(10,2) NOT NULL, PRIMARY KEY (S_NO))")

    #Insert Records in FLIGHT_CHART Table
    crsr.execute("INSERT INTO Flight_Chart (Flight_Number,Departure_From,Arrival_To,Departure_Time,Arrival_Time,Business_Seats,Business_Fare,Economy_Seats,Economy_Fare) VALUES ('AL01BC','BANGALORE','CHENNAI','05:00','06:00',0,5000.00,0,2750.00),('AL01BC','CHENNAI','BANGALORE','07:30','08:30',10,5000.00,50,2750.00),('AL02BD','BANGALORE','DELHI','09:00','11:45',0,11000.00,50,6000.00),('AL02BD','DELHI','BANGALORE','12:00','14:45',10,11000.00,50,6000.00),('AL03BH','BANGALORE','HYDERABAD','15:30','16:50',10,8000.00,0,4500.00),('AL03BH','HYDERABAD','BANGALORE','17:30','18:50',10,8000.00,50,4500.00),('AL04BM','BANGALORE','MUMBAI','19:00','21:00',10,6500.00,50,3500.00),('AL04BM','MUMBAI','BANGALORE','21:30','23:30',10,6500.00,50,3500.00),('AL05CD','CHENNAI','DELHI','00:00','03:00',10,10500.00,50,6500.00),('AL05CD','DELHI','CHENNAI','03:30','06:30',10,10500.00,50,6500.00),('AL06CH','CHENNAI','HYDERABAD','07:00','18:50',10,7000.00,50,4000.00),('AL06CH','HYDERABAD','CHENNAI','08:30','09:45',10,7000.00,50,4000.00),('AL07CM','CHENNAI','MUMBAI','10:00','12:00',10,8000.00,50,4500.00),('AL07CM','MUMBAI','CHENNAI','12:30','14:30',10,8000.00,50,4500.00),('AL08DH','DELHI','HYDERABAD','14:50','17:00',10,10000.00,50,5500.00),('AL08DH','HYDERABAD','DELHI','17:20','19:30',10,10000.00,50,5500.00),('AL09DM','DELHI','MUMBAI','19:45','22:00',10,6500.00,50,3800.00),('AL09DM','MUMBAI','DELHI','22:15','00:30',10,6500.00,50,3800.00),('AL10HM','HYDERABAD','MUMBAI','00:00','01:40',10,7500.00,50,4200.00),('AL10HM','MUMBAI','HYDERABAD','02:00','03:40',10,7500.00,50,4200.00)")

    #Create BAGGAGE Table
    crsr.execute("CREATE TABLE BAGGAGE (S_No INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, Weight VARCHAR(20) NOT NULL, Rate FLOAT(7,2) NOT NULL)")

    #Insert Records in BAGGAGE Table
    crsr.execute("INSERT INTO baggage (Weight,Rate) VALUES ('10 to 20',1000), ('21 to 30',2000), ('31 to 40',3000), ('41 to 50',4000)")

    #Create AVAILABLE_DESTINATIONS Table
    crsr.execute("CREATE TABLE AVAILABLE_DESTINATIONS (S_No INT(2) NOT NULL, City VARCHAR(20) NOT NULL PRIMARY KEY)")

    #Insert Records in AVAILABLE_DESTINATIONS Table
    crsr.execute("INSERT INTO available_destinations (S_No,City) VALUES (1,'Bangalore'),(2,'Chennai'),(3,'Delhi'),(4,'Hyderabad'), (5,'Mumbai')")

    #Create ADMIN_DETAILS Table
    crsr.execute("CREATE TABLE ADMIN_DETAILS (Name VARCHAR(20) NOT NULL PRIMARY KEY,Pass_Word VARCHAR(20) NOT NULL)")

    #Insert Records in ADMIN_DETAILS Table
    crsr.execute("INSERT INTO admin_details (Name,Pass_Word) VALUES ('Karthik','asdfgh'), ('Jane','qwerty'), ('Harshini','poiuyt'), ('Zain','mnbvcx')")

    #Create PASSENGER_DETAILS Table
    crsr.execute("CREATE TABLE PASSENGER_DETAILS (Ticket_Number INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(20) NOT NULL, Mobile BIGINT(11) NOT NULL, Source VARCHAR(20) NOT NULL, Destination VARCHAR(20) NOT NULL, Date_Of_Journey DATE NOT NULL, Total_Charges FLOAT(10,2) NOT NULL)")

    #Commit changes in database
    conn.commit()
       
    #Close cursor
    crsr.close()

    #disconnect Databases
    conn.close()
