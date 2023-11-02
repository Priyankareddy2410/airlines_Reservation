import pymysql
import reservations
import book_ticket
import cancel_reservation

ticket_num = 0

def cancel_res():
    while True:
        try:
            name = input('Enter name of passenger : ')
            mob = input('Enter mobile number  : ')
            from1 = input('Enter source of travel : ')
            to1 = input('Enter destination : ')
            ticket_num = int(input('Enter ticket number : '))
            break
        except:
            print('**Enter valid input**')

    try:
        #Open Database connection
        conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')

        #Prepare a cursor object using the cursor() method
        crsr=conn.cursor()

        #Prepare sql query
        arg = (ticket_num)
        sql = "SELECT * FROM PASSENGER_DETAILS WHERE TICKET_NUMBER = %s"

        #execute cursor command
        crsr.execute(sql,arg)

        #Commit changes in database
        conn.commit()
        d=crsr.fetchall()

        for i in d:
            b = []
            flight_num =''
            depart_time=''
            
            depart_date = i[5]
            psgr_fare = i[6]
            b = reservations.conf(from1,to1,flight_num,depart_time)
            flight_num1 =b[0]
            depart_time1= b[1]
            
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
        #book_ticket.display_itinerary(flight_num,psgr_name,depart_from,arrive_to,fare,depart_time,depart_date,psgr_fare)

        conf = input('Type "CONFIRM" to confirm cancellation of reservation. Type "EXIT" to revert from cancellation of reservation : ')

        while True:
            if conf == 'CONFIRM':
                cancel_reservation.conf_cncl(ticket_num)
                break
            elif conf == 'EXIT':
                print('No cancellation of ticket')
                break
                
            else:
                print('***Enter Valid Input***')
        
    #else:
        #print("No record found, Please enter the details again : ")
    except:
        print('No Passenger With The Above Credentials Exists')
           
                

        
       
        #Close cursor
        crsr.close()

        #disconnect Databases
        conn.close()

        #return to book_ticket module
        return


def conf_cncl(ticket_num):
    #Open Database connection
    conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
    
    #Prepare a cursor object using the cursor() method
    crsr=conn.cursor()

    #Prepare sql query
    arg = (ticket_num)
    sql = "DELETE FROM PASSENGER_DETAILS WHERE TICKET_NUMBER=%s"
    
    #delete from passenger details                    
    crsr.execute(sql,arg)

    #Commit changes in database
    conn.commit()       

    #Close cursor
    crsr.close()

    #disconnect Databases
    conn.close()

    print('**Reservation Cancelled Successfully**')
    print('Returning to main menu')
    print()
    return











