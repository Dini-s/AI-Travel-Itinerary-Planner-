from datetime import datetime
from destination import Destination
from itineraryManager import ItineraryManager
from aiTravelAssistant import AITravelAssistant
from tabulate import tabulate


theme="""

 __    __     _                            _            _     _____    _____ _   _                                     ___ _                             
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___     /_\    \_   \   \_   \ |_(_)_ __   ___ _ __ __ _ _ __ _   _    / _ \ | __ _ _ __  _ __   ___ _ __ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   //_\\    / /\/    / /\/ __| | '_ \ / _ \ '__/ _` | '__| | | |  / /_)/ |/ _` | '_ \| '_ \ / _ \ '__|
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | /  _  \/\/ /_   /\/ /_ | |_| | | | |  __/ | | (_| | |  | |_| | / ___/| | (_| | | | | | | |  __/ |   
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \_/ \_/\____/   \____/  \__|_|_| |_|\___|_|  \__,_|_|   \__, | \/    |_|\__,_|_| |_|_| |_|\___|_|   
                                                                                                             |___/                                       

"""

print(theme)

#validate usere entered date "YYYY-MM-DD" format
def valid_Date(InputDate):
    try:
        datetime.strptime(InputDate,"%Y-%m-%d")
        return True
    except ValueError:
        return 
    
#validate budget    
def valid_Budget(budget):
    try:
        if budget>0:
            return True
    except ValueError:
        return False
    
#sort date in ascending order    
def sortByDate(data):
    
    n=len(data)
    for i in range(len(data)):
        for j in range(0,n-i-1):
            if data[j].start_date>data[j+1].start_date:
                data[j],data[j+1]=data[j+1],data[j]
    return data

#sort budget in ascending order   
def sortByBudget(data):
    n=len(data)
    for i in range(len(data)):
        for j in range(0,n-i-1):
            if data[j].budget>data[j+1].budget:
                data[j],data[j+1]=data[j+1],data[j]
    return data

def main():

    #create object for Itinerary Manager and ai Assistance
    manager=ItineraryManager()
    assistance=AITravelAssistant()

    #load saved file details.when the program load
    manager.load_from_file()
    

  
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
                if(valid_Budget(budget)):
                    break
                else:
                    print("Budget must be positive.Try Again...")

            activities=input("Enter Your planed activities seperated by using ','").split(",")

            #add new data to object  
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

                    
                        
                

        elif choice==3:
            
                while(True):
                    city=input("Input City That you want to Update:").lower()
                    option1=input("Do you need find existing details? Y-yes N-no").lower()

                    if option1=='y':
                        existDetails=manager.search_destination(city)

                        if existDetails:

                            for i in existDetails:
                                print("\t| City : "+i.city)
                                print("\t| Country : "+i.country)
                                print("\t| Start Date : "+i.start_date)
                                print("\t| End Date : "+i.end_date)
                                print("\t| Budget : "+str(i.budget))
                                print("\t| Activities :")
                                for j in i.activities:
                                    print("\t\t"+j+"\n")

                        else:
                            print("Something Went to wrong.Try Again...")
                            continue

                    updates={}
                    while(True):

                        print("=== [1]Country [2]Start Date [3]End Date [4]Budget [5]Activities ===")
                        attribute=input("Enter Field Number That You want to upadte or Type 'Done' for finished:")

                        if attribute=="Done":
                            break
                        value=input("Enter Updated Value : ")
                        field=""

                        if attribute=="1":
                            field="country"
                        elif attribute=="2":
                            field="start_date"

                            if(valid_Date(value)):
                                value=value
                            else:
                                print("Date Must be format in 'YYYY-MM-DD'")
                                continue
                        elif attribute=="3":
                            field="end_date"

                            if(valid_Date(value)):
                                value=value
                            else:
                                print("Date Must be format in 'YYYY-MM-DD'")
                                continue
                        elif attribute=="4":
                            field="budget"
                            value=float(value)
                            if(valid_Budget(value)):
                                value=value
                            else:
                                print("Budget Must be Positive.")
                                continue
                        elif attribute=="5":
                            field="activities"
                            value=[value.strip() for i in value.split(",")]

                       
                        
                        else:
                            print("Invalid Number Try Again...")
                            continue

                        updates[field]=value


                    if(manager.update_destination(city,updates)):
                            print("Your Data Updated Successfully.")
                            option3=input("Do you need to update other destination:").lower()
                            if option3=="no":
                                break
                    else:
                        print("something went to wrong.Try Again....")
                        continue

        elif choice==4:
            data=[]
            for i in manager.view_all_file():
                #print("\n")
               
                data.append({
                    "City":i.city,
                    "Country":i.country,
                    "Start":i.start_date,
                    "End Date":i.end_date,
                    "Budget":i.budget
                })
               #print out put as a table      
            print(tabulate(data,headers="keys",tablefmt="grid"))

            option=input("Do You need to Sort Data? ").lower()
            if(option=="yes"):
                selection=input("[1]Sort By Date [2]Sort By Budget: ")
                if selection=="1":
                    sortedDestination=sortByDate(manager.view_all_file())
                    table=[]
                    for i in sortedDestination:
                        table.append({
                            "City":i.city,
                            "Country":i.country,
                            "Start":i.start_date,
                            "End Date":i.end_date,
                            "Budget":i.budget
                        })
                    print(tabulate(table,headers="keys",tablefmt="grid"))
                elif selection=="2":
                    sortedDestination=sortByBudget(manager.view_all_file())
                    table=[]
                    for i in sortedDestination:
                        table.append({
                            "City":i.city,
                            "Country":i.country,
                            "Start":i.start_date,
                            "End Date":i.end_date,
                            "Budget":i.budget
                        })
                    print(tabulate(table,headers="keys",tablefmt="grid"))
                else:
                    print("Invalid Number")
                    

        
        elif choice==5:
            while(True):

                city=input("Enter City Of Search Destination : ").lower()
                searchDeastination=manager.search_destination(city)

                if(searchDeastination):
                    for i in searchDeastination:
                        print("\n")
                        print(i)
                        print("\n")
                else:
                    print("City Not Found")
                    
                option=input("Do You Need to Continue?").lower()
                if option != "yes":
                    break

        elif choice==6:
            while(True):

                city=input("Enter city for AI plan: ")

                for i in manager.destinations:
                    if i.city.lower()== city.lower():
                        print("\n====AI Travel Itinerary====")
                        print(assistance.generate_itinerary(i))
                        print("\n ====Travel Budget Plan===")
                        print(assistance.generate_budget_tip(i))
                option=input("Do You Want To continue?(Y-Yes N-No)")  
                if option != 'y':
                    break 

        
        elif choice==7:
            manager.save_Itinerary()
            print("Save Itinerary")
            

        elif choice==8:
            manager.load_from_file()
            print("Itinerary Loaded...")
            
        

        elif choice==9:
            manager.save_Itinerary()
            print("Thank You for join Us....Good Bye")
            break  

        else:
            print("Please Enter Valid Number")

            



if __name__=="__main__":
    main()



