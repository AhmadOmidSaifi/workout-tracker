import os

from dotenv import find_dotenv,load_dotenv
from datetime import datetime
import requests
sheety_url = "https://api.sheety.co/29807a8ddb780a86799937873194d7bc/copyOfMyWorkouts/workouts"

dotenv_path = find_dotenv()
print(load_dotenv(dotenv_path))

NUTRI_APP_ID = os.getenv("NUTRI_APP_ID")
NUTRI_API_KEY = os.getenv("NUTRI_API_KEY")

url= "https://trackapi.nutritionix.com/v2/natural/exercise"
headers= {
    "Content-Type": "application/json",
    "x-app-id":NUTRI_APP_ID ,
    "x-app-key":NUTRI_API_KEY
  }
data = {
    "query": str(input("Tell me which exercises you did: "))
}
response = requests.post(url,headers=headers,json=data)
json_result = response.json()
print(json_result)
print("\n\n")
body = {
    "workout":{
        "date" : datetime.today().strftime("%d/%m/%Y"),
        "time" : datetime.now().strftime("%H:%M:%S"),
        "exercise" : json_result["exercises"][0]["user_input"],
        "duration" : json_result["exercises"][0]["duration_min"],
        "calories" : json_result["exercises"][0]["nf_calories"]
    }
}
headers_sheety = {
    "Authorization": "Bearer jswWfjdksljsdsdsds"
}
response_sheety = requests.post(sheety_url,headers=headers_sheety, json=body)
print(response_sheety)
