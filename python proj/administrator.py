import passenger_statistics
import sys
import pymysql
import administrator

def admin():
    while  True:
        try:
            #admin screen
            print()
            print('1 : Existing Administrator ')
            print('2 : New Administrator ')
            print('Enter any other integer value to Exit ')
            print()

            opt = int(input('Enter your option : '))

            if opt == 1:
                admin_functions()
                return
            elif opt == 2:
                new_admin()
            else:
                return
                print()
        except:
            print()
            print('**Please enter valid input**')
            


#####################################################################################################
#Create New ADMIN
def new_admin():
    print()
    name = input("Enter Name: ")
    pwd1 = input("Select Password: ")
    pwd2 = input("Confirm Password: ")
    print()
    ctr = 0
    while(True):
        if pwd1 != pwd2:
            pwd2 = input("Password mismatch, Confirm Password again: ")
            ctr += 1
            if ctr == 4:
                print("Maximum attempts reached, Exiting ")
                sys.exit()
        else:
            #Open Database connection
            conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
            
            #Prepare a cursor object using the cursor() method
            crsr=conn.cursor()

            #Prepare sql query
            arg = (name,pwd1)
            sql = "INSERT INTO ADMIN_DETAILS (NAME,PASS_WORD) VALUES (%s,%s)"
            crsr.execute(sql,arg)
            
            #Commit changes in database
            conn.commit()
               
            #Close cursor
            crsr.close()

            #disconnect Databases
            conn.close()

            print('**New Administrator',name,'Created**')
            print('Re-enter name and password for administrative access')
            
            admin_functions()




#####################################################################################################
#Validate Password
def validate_pwd():
    while True:
        try:
            print()
            name = input("Enter Name: ")
            val_pwd1 = input("Enter Password: ")
            #Open Database connection
            conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
            
            #Prepare a cursor object using the cursor() method
            crsr=conn.cursor()

            sql = "SELECT PASS_WORD FROM ADMIN_DETAILS WHERE name='"+name+"'"
            
            crsr.execute(sql)
            
            d = crsr.fetchone()
            i = d[0]
            
            if val_pwd1 == i:
                return
            else:
                print('**Incorrect password, try again**')
            #Commit changes in database
            conn.commit()
                 
            #Close cursor
            crsr.close()

            #disconnect Databases
            conn.close()
        except:
            print('**This administrator does not exist, try again**')



#####################################################################################################
#Admin Functions
def admin_functions():
    while True:
        validate_pwd()

        print()
        print('1 : Show Flight Schedule')
        print('2 : Revise Flight Fares')
        print('3 : Delete Flight Route')
        print('4 : Display Passenger Statistics')
        print('5 : Display Passenger Details')
        print('6 : Add New Adminstrator')
        print('7 : Exit')
        print()

        func_option = int(input('Enter your option : '))
        print()
        if func_option == 1:
            #Open Database connection
            conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
            
            #Prepare a cursor object using the cursor() method
            crsr=conn.cursor()

            #Prepare sql query
            sql = "SELECT * FROM FLIGHT_CHART"
            crsr.execute(sql)
            a = crsr.fetchall()

            #Commit changes in database
            conn.commit()       

            print('COLUMNS: 1-S_NO., 2-FLIGHT_NO., 3-FROM, 4-DESTINATION, 5-DEPARTURE_TIME, 6-ARRIVAL_TIME, 7-BSN_SEATS, 8-BSN_FARE, 9-EC_SEATS, 10-EC_SEATS')

            for i in a:
                print(f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]} {i[9]}')
                print()

            #Close cursor
            crsr.close()

            #disconnect Databases
            conn.close()
            print('Returning to main menu')
            print()
            return 
            
        elif func_option == 2:
            while True:
                #using try if fare entered is not float
                try:
                    while True:
                        from1 = input('Enter departure source (name): ')
                        to1 = input('Enter destination (name): ')
                        

                        #Validate Source & Destination combination from FLIGHT_CHART table
                        valid_input = 'n'
                        inp = validate_src_dest(from1,to1,valid_input)

                        if inp == 'n':
                            continue
                        else:
                            break
                                                
                    bsns_fare = input("Enter new business class fare: ")
                    ec_fare = input('Enter new economy class fare: ')

                    #Open Database connection
                    conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
          
                    #Prepare a cursor object using the cursor() method
                    crsr=conn.cursor()

                    #Prepare sql query                   
                    sql = "UPDATE FLIGHT_CHART SET BUSINESS_FARE='"+bsns_fare+"',ECONOMY_FARE='"+ec_fare+"' WHERE DEPARTURE_FROM='"+from1+"' AND ARRIVAL_TO='"+to1+"'"

                    crsr.execute(sql)

                    #Commit changes in database
                    conn.commit()       

                    #Close cursor
                    crsr.close()

                    #disconnect Databases
                    conn.close()

                    print('**Update Successful**')
                    print('Returning to main menu')
                    print()
                    return

                except:
                    print('Enter VALID Details')
                    print()
                              
        elif func_option == 3:
            while True:
                try:
                    dept_from = input("Enter departure source: ")
                    arr_to = input("Enter destination: ")
                    
                    #Open Database connection
                    conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
                    
                    #Prepare a cursor object using the cursor() method
                    crsr=conn.cursor()

                    #Prepare sql query
                    sql = "DELETE FROM FLIGHT_CHART WHERE DEPARTURE_FROM='"+dept_from+"' AND ARRIVAL_TO='"+arr_to+"'"
                    #delete from flight chart                    
                    crsr.execute(sql)

                    #Commit changes in database
                    conn.commit()       

                    #Close cursor
                    crsr.close()

                    #disconnect Databases
                    conn.close()

                    print('**Successfully Deleted Data**')
                    print('Returning to main menu')
                    print()
                    return

                except:
                    print('**Please enter valid input**')
            
        elif func_option == 4:
            passenger_statistics.passengers_travelled_year()
            print()
            print()
            print()
            passenger_statistics.passengers_travelled_class()
            print('Returning to main menu')
            print()
            return
        elif func_option == 5:
            #Open Database connection
            conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
            
            #Prepare a cursor object using the cursor() method
            crsr=conn.cursor()

            #Prepare sql query
            sql = "SELECT * FROM PASSENGER_DETAILS"
            crsr.execute(sql)
            a = crsr.fetchall()

            #Commit changes in database
            conn.commit()       

            print('COLUMNS: 1-TICKET_NUMBER, 2-PASSENGER_NAME, 3-MOBILE_NUMBER, 4-SOURCE, 5-DESTINATION, 6-DATE_OF_JOURNEY, 7-TOTAL_CHARGES')

            for i in a:
                print(f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]}')
                print()

            #Close cursor
            crsr.close()

            #disconnect Databases
            conn.close()
            print('Returning to main menu')
            print()
            return 
            
        elif func_option == 6:
            try:
                name = input("Enter Name: ")
                pwd = input("Select Password: ")
                #Open Database connection
                conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')
                
                #Prepare a cursor object using the cursor() method
                crsr=conn.cursor()

                #Prepare sql query
                arg = (name,pwd)
                sql = "INSERT INTO ADMIN_DETAILS (NAME,PASS_WORD) VALUES (%s,%s)"
                crsr.execute(sql,arg)
                
                #Commit changes in database
                conn.commit()
                   
                #Close cursor
                crsr.close()

                #disconnect Databases
                conn.close()
                print("**New Administrator ", name, " Created**")
                print('Returning to main menu')
                print()
                return
            except:
                print('**Administrator already exists**')

        elif func_option == 7:
            return
        
        else:
            print('**Please enter valid input**')
        
#####################################################################################################
#Validate Source and Destination from FLIGHT_CHART table
def validate_src_dest(from1,to1,valid_input):

    #Open Database connection
    conn=pymysql.connect(host='localhost',user='root',password='summer7',db='airlines')

    #Prepare a cursor object using the cursor() method
    crsr=conn.cursor()

    #Prepare sql query
    sql = "SELECT * FROM FLIGHT_CHART WHERE DEPARTURE_FROM ='"+from1+"' AND ARRIVAL_TO ='"+to1+"'"

    #execute cursor command
    crsr.execute(sql)
   
    d=crsr.fetchall()
        
    if (len(d) == 0):
        print('**Invalid Entry, Re-enter Source and Destination**')
    else:
        valid_input = 'y'
            
    #Close cursor
    crsr.close()

    #disconnect Databases
    conn.close()

    #return to book_ticket module
    return valid_input
