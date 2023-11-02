import pymysql
import reservations

def res():
    while True:
        try:
            name = input('Enter name of passenger : ')
            mob = input('Enter mobile number  : ')
            from1 = input('Enter source of travel : ')
            to1 = input('Enter destination : ')
            break
        except:
            print('**Enter valid input**')

    try:
        #Open Database connection
        conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')

        #Prepare a cursor object using the cursor() method
        crsr=conn.cursor()

        #Prepare sql query
        sql = "SELECT * FROM PASSENGER_DETAILS WHERE NAME='"+name+"' AND MOBILE='"+mob+"' AND SOURCE='"+from1+"'AND DESTINATION='"+to1+"'"
        
        try:
            #execute cursor command
            crsr.execute(sql)
            #Commit changes in database
            conn.commit()
        except:
            #rollback in case of any error
            conn.rollback()
        else:
            print()

        d=crsr.fetchall()
        
        #display baggage options to the user.
        if (len(d) !=  0):
            for i in d:
                #while True:
                a = []
                flight_num =''
                depart_time=''
                
                depart_date = i[5]
                psgr_fare = i[6]
                a = conf(from1,to1,flight_num,depart_time)
                flight_num1 =a[0]
                depart_time1= a[1]
                
                print("                                                                     ")
                print("                                                                     ")
                print("                                                                     ")
                print("                                                                     ")
                print("*******************F L I G H T   I T I N E R A R Y*******************")
                print("Flight No:          ",flight_num1.upper(), "                          ")
                print("                                                                     ")    
                print("Passenger:          ",name,"                                         ")  
                print("                                                                     ")    
                print("From:               ",from1.upper(),"                                ")
                print("                                                                     ")    
                print("To:                 ",to1.upper(),"                                  ")
                print("                                                                     ")
                print("Departure Time:     ",depart_time1,"                                  ")
                print("                                                                     ")
                print("Date of Departure:  ",depart_date,"                                  ")
                print("                                                                     ")
                print("Total Fare:         ",psgr_fare,"                                    ")
                print("*********************************************************************")
                print("                                                                     ")
                print("                                                                     ")
        else:
            print("No record found, Please enter the details again : ")
    except:
        print('No Passenger With The Above Credentials Exists')
           
                

        
       
    #Close cursor
    crsr.close()

    #disconnect Databases
    conn.close()

    #return to book_ticket module
    return



def conf(from1,to1,flight_num,depart_time):
    #Open Database connection
    conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')

    #Prepare a cursor object using the cursor() method
    crsr=conn.cursor()

    #Prepare sql query
    sql = "SELECT * FROM FLIGHT_CHART WHERE DEPARTURE_FROM='"+from1+"' AND ARRIVAL_TO='"+to1+"'"
    try:
        #execute cursor command
        crsr.execute(sql)

        #Commit changes in database
        conn.commit()
    except:
        #rollback in case of any error
        conn.rollback()
    else:
        print()

    d=crsr.fetchall()

    for j in d:
        flight_num = j[1]
        depart_time = j[4]
    return (flight_num,depart_time)
    
