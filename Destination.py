class Destination:

    def __init__(self,city,country,start_date,end_date,budget,activities):
        self.city=city
        self.country=country
        self.start_date=start_date
        self.end_date=end_date
        self.budget=budget
        self.activities=activities

    
    def update_details(self,**kwargs):

        for key,value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key,value)

    
    def __str__(self):
        return f"City:{self.city}\nCountry:{self.country}\nStart Date:{self.start_date} to End Date:{self.end_date}\nBudget:{self.budget}\nActivities: {', '.join(self.activities)}"



