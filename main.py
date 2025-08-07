from datetime import datetime
from destination import Destination
from itineraryManager import ItineraryManager


theme="""

 __    __     _                            _            _     _____    _____ _   _                                     ___ _                             
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___     /_\    \_   \   \_   \ |_(_)_ __   ___ _ __ __ _ _ __ _   _    / _ \ | __ _ _ __  _ __   ___ _ __ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   //_\\    / /\/    / /\/ __| | '_ \ / _ \ '__/ _` | '__| | | |  / /_)/ |/ _` | '_ \| '_ \ / _ \ '__|
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | /  _  \/\/ /_   /\/ /_ | |_| | | | |  __/ | | (_| | |  | |_| | / ___/| | (_| | | | | | | |  __/ |   
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \_/ \_/\____/   \____/  \__|_|_| |_|\___|_|  \__,_|_|   \__, | \/    |_|\__,_|_| |_|_| |_|\___|_|   
                                                                                                             |___/                                       

"""

print(theme)

def valid_Date(InputDate):
    try:
        datetime.strptime(InputDate,"%Y-%m-%d")
        return True
    except ValueError:
        return False
        

def main():

    manager=ItineraryManager()

  
    while True:

        print("\t\t[1] Add Destination\t\t [2] Remove Destination")
        print("\t\t[3] Update Destination\t\t [4] View All Destination")
        print("\t\t[5] Search Destination\t\t [6] AI Travel Assistance")
        print("\t\t[7] Save Itinerary\t\t [8] Load Itinerary")
        print("\t\t[9] Exit")

        try:
            choice=int(input("Enter Your Option:"))
        except ValueError:
            print("value must be a number")

        if choice==1:
            city=input("Destinated City : ")
            country=input("Destiated Country : ")
            while(True):
                startDate=input("Start Date(YYYY-MM-DD) :")

                if(valid_Date(startDate)):
                    break
                else:
                    print("Date must be in 'YYYY-MM-DD',Try Again")
            
            while(True):
                endDate=input("End Date(YYYY-MM-DD) :")

                if(valid_Date(endDate)):
                    break
                else:
                    print("Date must be in 'YYYY-MM-DD',Try Again")
            
            while(True):
                budget=float(input("Your Budget : "))
                if(budget>0):
                    break
                else:
                    print("Budget must be positive")

            activities=input("Enter Your planed activities seperated by using ','").split(",")

            newdestination=Destination(city,country,startDate,endDate,budget,activities)
            manager.add_destination(newdestination)

        elif choice==2:
            
            while(True):
                city=input("Enter city : ")

                cityDetails=manager.search_destination(city)
                
                if cityDetails:

                    for d in cityDetails:
                        print("\t| City : "+d.city)
                        print("\t| Country : "+d.country)
                        print("\t| Start Date : "+d.start_date)
                        print("\t| Country : "+d.end_date)
                        print("\t| Budget : "+str(d.budget))
                        print("\t| Activities :")
                        for i in d.activities:
                            print("\t\t"+i+"\n")
                    
                    option=input("Are you  sure you want to remove destination(Y-yes,N-No):").lower()

                    if option=='y':
                        manager.remove_destination(city)
                        selectOption=input("Remove Successfully.Do You want to remove another destination:").lower()
                        if selectOption=='y':
                            continue
                        else:
                            break

                    else:
                        continue

                else:
                    print("No Destination found")
                    selectOption=input("Do you need to continue?(Y-Yes N-No) : ").lower()
                    if selectOption=='n':
                        break

                    
                        
                



        elif choice==9:
            print("Thank You for join Us....Good Bye")
            break  

        else:
            print("Please Enter Valid Number")

            



if __name__=="__main__":
    main()



