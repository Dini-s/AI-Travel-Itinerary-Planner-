
from destination import Destination
import json


class ItineraryManager:

    def __init__(self):
        self.destinations=[]

    def add_destination(self,destination):
        self.destinations.append(destination)
    
    def remove_destination(self,city):
        temp=[]
        for d in self.destinations:
            if d.city.lower() != city.lower():
                temp.append(d)
        
        self.destinations=temp
        
    def update_destination(self,city,updateDetails):
        for x in self.destinations:
            if x.city.lower() == city.lower():
                x.update_details(updateDetails)

                return True
        return False
    
    def search_destination(self,searchCity):
        for cities in self.destinations:
            if cities.city.lower()==searchCity.lower():
                return self.cities
            
    
    def view_all_file(self):
        return self.destinations
    

    def save_Itinerary(self):
        try:
            data=[itinary.__dict__ for itinary in self.destinations]
            with open("Itinerary.json","w") as f:
                json.dump(data,f)
                return True
        except :
            return False
        
    
    def load_from_file(self):
        try:
            with open("Itinerary.json","r")as file:
                data=json.load(file)
                for details in data:
                    self.destinations.append(Destination(**details))
        except FileNotFoundError:
            print("File Not Found")
            self.destinations=[]
            


            
    

    
