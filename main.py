import requests 
import json
from datetime import datetime 
import pyttsx3
import time
from dotenv import load_dotenv
import os
from notifypy import  Notify


load = load_dotenv()

API_KEY = os.getenv("API_KEY")
robot = pyttsx3.init()

URL = "https://newsapi.org/v2/everything"

date = datetime.now().strftime("%Y-%m-%d")
date_refract = datetime.now().strftime("%d")
date_reduce = ""
print(date_reduce)

if date_refract == "1" :
    date_reduce =  int(date_refract)
else :
    date_reduce =  int(date_refract)-1 
    
dateFrom = datetime.now().strftime(f"%Y-%m-{date_reduce}")
print(date)

PARAMS = {
    "apiKey" : API_KEY,
    "q" : "technologie",
    "from" : dateFrom,
    "to":date,
    "language":"fr",
    "sortBy" : "popularity"
}

try : 
   response = requests.get(URL ,params=PARAMS)
   result = response.status_code
   datas = response.json()["articles"]
   
   for data  in datas:
        with open("data.json","w") as  file :
            json.dump(data,file)
            
   robot.getProperty("rate")      
   robot.setProperty("rate",120)   
   robot.getProperty("volume")      
   robot.setProperty("volume",5.0)  
   voices = robot.getProperty("voices")      
   robot.setProperty("voice",voices[1].id)  
   robot.say("Vous avez une nouvelle notifications")
       
except :
    print("une erreur est survenue")

robot.runAndWait()






Notifications = Notify()
with open("data.json","r") as  file :
     file_load  = json.load(file)
     Notifications.title = file_load["title"]
     Notifications.application_name ="Notify App"
     Notifications.message = file_load["content"]
     Notifications.icon = 'frame.png'
     Notifications.send()

