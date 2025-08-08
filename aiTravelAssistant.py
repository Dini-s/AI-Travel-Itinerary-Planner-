from openai import OpenAI
import os
from dotenv import load_dotenv



load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AITravelAssistant:

    def generate_itinerary(self, destination):
        prompt = f"""Create a day-wise travel itinerary for {destination.city}, {destination.country}
                   from {destination.start_date} to {destination.end_date}.
                   Budget: LKR {destination.budget}.
                   Activities: {', '.join(destination.activities)}.
                """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    def generate_budget_tip(self,destination):
        prompt = f"""
                Provide budget-saving travel tips for a trip to {destination.city},{destination.country} with a budget of LKR {destination.budget}"""
        
        response=client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role":"user","content":prompt}]
        )

        return response.choices[0].message.content