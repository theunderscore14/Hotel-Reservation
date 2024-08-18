import random 
import datetime 
   
 
name = [] 
add = [] 
mno = [] 
checkin = [] 
checkout = [] 
rc = [] 
p = [] 
room = [] 
price = [] 
roomno = [] 
cuid = [] 
day = [] 
   

   
i = 0
   

def Home(): 
      
    print("\t\t\t\t WELCOME TO HOTEL HIGHBURY\n") 
    print("\t\t\t 1 Booking\n") 
    print("\t\t\t 2 Rooms Info\n") 
    print("\t\t\t 3 Restaurant Menu Card\n") 
    print("\t\t\t 4 Payment\n") 
    print("\t\t\t 0 Exit\n") 
   
    ch=int(input("->")) 
      
    if ch == 1: 
        print(" ") 
        Booking() 
      
    elif ch == 2: 
        print(" ") 
        Rooms_Info() 
      
    elif ch == 3: 
        print(" ") 
        Restaurant() 
      
    elif ch == 4: 
        print(" ") 
        Payment() 
      
    else: 
        exit() 
   
   
def date(c): 
      
    if c[2] >= 2020 and c[2] <= 2021: 
          
        if c[1] != 0 and c[1] <= 12: 
              
            if c[1] == 2 and c[0] != 0 and c[0] <= 31: 
                  
                if c[2]%4 == 0 and c[0] <= 29: 
                    pass
                  
                elif c[0]<29: 
                    pass
                  
                else: 
                    print("Invalid date\n") 
                    name.pop(i) 
                    mno.pop(i) 
                    add.pop(i) 
                    checkin.pop(i) 
                    checkout.pop(i) 
                    Booking() 
              
              
           
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31: 
                pass
              
            
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2: 
                pass
              
            
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31: 
                pass
              
             
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:   
                pass
              
            else:  
                print("Invalid date\n") 
                name.pop(i) 
                mno.pop(i) 
                add.pop(i) 
                checkin.pop(i) 
                checkout.pop(i) 
                Booking() 
                  
        else: 
            print("Invalid date\n") 
            name.pop(i) 
            mno.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
              
    else: 
        print("Invalid date\n") 
        name.pop(i) 
        mno.pop(i) 
        add.pop(i) 
        checkin.pop(i) 
        checkout.pop(i) 
        Booking() 
   
   

def Booking(): 
      
        
        global i 
        print(" BOOKING ROOMS") 
        print(" ") 
          
        while 1: 
            n = str(input("Name: ")) 
            p1 = str(input("Mobile No.: ")) 
            a = str(input("Address: ")) 
              
            
            if n!="" and p1!="" and a!="": 
                name.append(n) 
                add.append(a) 
                break
                  
            else: 
                 print("\tName, Mobile No. & Address cannot be empty...!!") 
               
        cii=str(input("Check-In: ")) 
        checkin.append(cii) 
        cii=cii.split('/') 
        ci=cii 
        ci[0]=int(ci[0]) 
        ci[1]=int(ci[1]) 
        ci[2]=int(ci[2]) 
        date(ci) 
           
        coo=str(input("Check-Out: ")) 
        checkout.append(coo) 
        coo=coo.split('/') 
        co=coo 
        co[0]=int(co[0]) 
        co[1]=int(co[1]) 
        co[2]=int(co[2]) 
          
      
        if co[1]<ci[1] and co[2]<ci[2]: 
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]: 
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        else: 
            pass
          
        date(co) 
        d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
        d2 = datetime.datetime(co[2],co[1],co[0]) 
        d = (d2-d1).days 
        day.append(d) 
           
        print("----SELECT ROOM TYPE----") 
        print(" 1. Standard Non-AC") 
        print(" 2. Standard AC") 
        print(" 3. 3-Bed Non-AC") 
        print(" 4. 3-Bed AC") 
        print(("\t\tPress 0 for Room Prices")) 
          
        ch=int(input("->")) 
          
      
        if ch==0: 
            print(" 1. Standard Non-AC - Rs. 4000") 
            print(" 2. Standard AC - Rs. 5000") 
            print(" 3. 3-Bed Non-AC - Rs. 5500") 
            print(" 4. 3-Bed AC - Rs. 7000") 
            ch=int(input("->")) 
        if ch==1: 
            room.append('Standard Non-AC') 
            print("Room Type- Standard Non-AC")   
            price.append(4000) 
            print("Price- 4000") 
        elif ch==2: 
            room.append('Standard AC') 
            print("Room Type- Standard AC") 
            price.append(5000) 
            print("Price- 5000") 
        elif ch==3: 
            room.append('3-Bed Non-AC') 
            print("Room Type- 3-Bed Non-AC") 
            price.append(5500) 
            print("Price- 5500") 
        elif ch==4: 
            room.append('3-Bed AC') 
            print("Room Type- 3-Bed AC") 
            price.append(7000) 
            print("Price- 7000") 
        else: 
            print(" Wrong choice..!!") 
   
  
       
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
          
          
        
        while rn in roomno or cid in cuid: 
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
              
        rc.append(0) 
        p.append(0) 
                
        if p1 not in mno: 
            mno.append(p1) 
        elif p1 in mno: 
            for n in range(0,i): 
                if p1== mno[n]: 
                    if p[n]==1: 
                        mno.append(p1) 
        elif p1 in mno: 
            for n in range(0,i): 
                if p1== mno[n]: 
                    if p[n]==0: 
                        print("\tPhone no. already exists and payment yet not done..!!") 
                        name.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking() 
        print("") 
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
        print("Room No. - ",rn) 
        print("Customer Id - ",cid) 
        roomno.append(rn) 
        cuid.append(cid) 
        i=i+1
        n=int(input("0-BACK\n ->")) 
        if n==0: 
            Home() 
        else: 
            exit() 
  

def Rooms_Info(): 
    print("         ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("STANDARD NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed, Telephone, Television, ") 
    print("Double-Door Cupboard, 1 Coffee table and a sofa, Balcony and") 
    print("an attached washroom with hot/cold water available.\n") 
    print("STANDARD NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed, Telephone, Television,") 
    print("Double-Door Cupboard, 1 Coffee table and a sofa, Balcony and") 
    print("an attached washroom with hot/cold water available + Split AC.\n") 
    print("3-Bed NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Telephone,") 
    print("Televison, a Triple-Door Cupboard, 1 Coffee table with 2 sofas, 1") 
    print("Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water available.\n") 
    print("3-Bed AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Telephone,") 
    print("Television, a Triple-Door Cupboard, 1 Coffee table with 2 sofas, ") 
    print("1 Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water available + Split AC.\n\n") 
    print() 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
  

def Restaurant(): 
    ph=int(input("Customer Id: ")) 
    global i 
    f=0
    r=0
    for n in range(0,i): 
        if cuid[n]==ph and p[n]==0: 
            f=1
            print("-------------------------------------------------------------------------") 
            print("                           Hotel Highbury") 
            print("-------------------------------------------------------------------------") 
            print("                            Menu Card") 
            print("-------------------------------------------------------------------------") 
            print("\n BEVARAGES & SANDWICHES                 26 Palak Paneer......... 230.00") 
            print("----------------------------------      27 Chilli Paneer.......... 250.00") 
            print(" 1  Packaged Drinking Water. 20.00      28 Matar Mushroom......... 250.00") 
            print(" 2  Hot Milk................ 25.00") 
            print(" 3  Masala Tea.............. 30.00      ROTI") 
            print(" 4  Bread Jam............... 30.00     ----------------------------------") 
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 20.00") 
            print(" 6  Coffee.................. 50.00      30 Butter Roti............. 25.00") 
            print(" 7  Veg. Toast Sandwich..... 100.00     31 Plain Naan.............. 40.00") 
            print(" 8  Veg. Sandwich........... 120.00     32 Butter Naan............. 50.00") 
            print(" 9  Cheese Toast Sandwich... 130.00     33 Stuffed Paratha......... 70.00") 
            print(" 10 Grilled Sandwich........ 130.00")  
            print("                                        RICE")
            print(" SOUPS                                 ----------------------------------") 
            print("----------------------------------      34 Steamed Rice............120.00") 
            print(" 11 Veg. Munchow........... 110.00      35 Jeera Rice............. 140.00") 
            print(" 12 Hot & Sour............. 110.00      36 Veg Pulao.............. 170.00") 
            print(" 13 Veg. Noodle Soup....... 110.00") 
            print(" 14 Sweet Corn............. 120.00      SOUTH INDIAN") 
            print(" 15 Tomato Soup............ 120.00     ----------------------------------") 
            print("                                        37 Idli Sambhar........... 110.00") 
            print(" MAIN COURSE                            38 Vada Sambhar........... 110.00") 
            print("----------------------------------      39 Plain Dosa............. 120.00") 
            print(" 16 Jeera Aloo............. 160.00      40 Paper Dosa............. 120.00") 
            print(" 17 Dal Fry................ 160.00      41 Masala Dosa............ 130.00") 
            print(" 18 Dal Tadka.............. 160.00      42 Paneer Dosa............ 150.00") 
            print(" 19 Dal Makhani............ 170.00") 
            print(" 20 Aloo Matar............. 190.00      RAITA") 
            print(" 21 Mix Veg................ 200.00     ----------------------------------") 
            print(" 22 Shahi Paneer........... 220.00      43 Plain Curd.............. 80.00") 
            print(" 23 Kadai Paneer........... 220.00      44 Veg. Raita.............. 100.00") 
            print(" 24 Handi Paneer........... 220.00      45 Bundi Raita............. 100.00") 
            print(" 25 Malai Kofta............ 220.00      46 Pineapple Raita......... 160.00") 
            print("Press 0 -to end ") 
            ch=1
            while(ch!=0): 
                  
                ch=int(input(" -> ")) 
                  
             
                if ch==1 or ch==29: 
                    rs=20
                    r=r+rs 
                elif ch==2 or ch==30: 
                    rs=25
                    r=r+rs 
                elif ch==3 or ch==4 or ch==5: 
                    rs=30
                    r=r+rs
                elif ch==31:
                    rs=40
                    r=r+rs
                elif ch==6 or ch==32: 
                    rs=50
                    r=r+rs
                elif ch==33: 
                    rs=70
                    r=r+rs
                elif ch==43:
                    rs=80
                    r=r+rs
                elif ch==7 or ch==44 or ch==45:
                    rs=100
                    r=r+rs
                elif ch==11 or ch==12 or ch==13 or ch==37 or ch==38:
                    rs=110
                    r=r+rs
                elif ch==8 or ch==14 or ch==15 or ch==34 or ch==39 or ch==40:
                    rs=120
                    r=r+rs
                elif ch==9 or ch==10 or ch==41:
                    rs=130
                    r=r+rs
                elif ch==35:
                    rs=140
                    r=r+rs
                elif ch==42:
                    rs=150
                    r=r+rs
                elif ch==16 or ch==17 or ch==18 or ch==46:
                    rs=160
                    r=r+rs
                elif ch==19 or ch==36:
                    rs=170
                    r=r+rs
                elif ch==20:
                    rs=190
                    r=r+rs
                elif ch==21:
                    rs=200
                    r=r+rs
                elif ch==22 or ch==23 or ch==24 or ch==25:
                    rs=220
                    r=r+rs
                elif ch==26:
                    rs=230
                    r=r+rs
                elif ch==27 or ch==28:
                    rs=250
                    r=r+rs
                elif ch==0: 
                    pass
                else: 
                    print("Wrong Choice..!!") 
            print("Total Bill: ",r) 
              
           
            r=r+rc.pop(n) 
            rc.append(r)     
        else: 
            pass
    if f == 0: 
        print("Invalid Customer Id") 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
       
                   
           
def Payment(): 
      
    ph=str(input("Mobile Number: ")) 
    global i 
    f=0
      
    for n in range(0,i): 
        if ph==mno[n] : 
              
            
             if p[n]==0: 
                f=1
                print(" Payment") 
                print(" --------------------------------") 
                print("  MODE OF PAYMENT") 
                   
                print("  1- Credit/Debit Card") 
                print("  2- Paytm/PhonePe") 
                print("  3- Using UPI") 
                print("  4- Cash") 
                x=int(input("-> ")) 
                print("\n  Amount: ",(price[n]*day[n])+rc[n]) 
                print("\n            Pay For Highbury") 
                print("  (y/n)") 
                ch=str(input("->")) 
                  
                if ch=='y' or ch=='Y': 
                    print("\n\n --------------------------------") 
                    print("           Hotel Highbury") 
                    print(" --------------------------------") 
                    print("              Bill") 
                    print(" --------------------------------") 
                    print(" Name: ",name[n],"\t\n Mobile No.: ",mno[n],"\t\n Address: ",add[n],"\t") 
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t") 
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t") 
                    print(" Restaurant Charges: \t",rc[n]) 
                    print(" --------------------------------") 
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t") 
                    print(" --------------------------------") 
                    print("          Thank You") 
                    print("        Visit Again :)") 
                    print(" --------------------------------\n") 
                    p.pop(n) 
                    p.insert(n,1) 
                      
                   
                    roomno.pop(n) 
                    cuid.pop(n) 
                    roomno.insert(n,0) 
                    cuid.insert(n,0) 
                      
             else: 
                  
                for j in range(n+1,i): 
                    if ph==mno[j] : 
                        if p[j]==0: 
                            pass
                          
                        else: 
                            f=1
                            print("\n\tPayment has been Made :)\n\n")  
    if f==0:     
        print("Invalid Customer ID") 
          
    n = int(input("0-BACK\n ->")) 
    if n == 0: 
        Home() 
    else: 
        exit() 
    if n == 0: 
        Home() 
          
    else: 
        exit() 
  
 
Home() 

