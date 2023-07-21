
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict
from weather import Weather
from datetime import datetime

import json, requests, tempfile

from location import search


class ActionWeatherAPI(Action):
    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        resp = Weather(city) 
        temp=resp["temp"]
        hum=resp["hum"]
        
        
        

        if temp  is None:
            dispatcher.utter_template("utter_city_not_found")  #
        else:
            dispatcher.utter_message(response="utter_temp", temp=temp, city=city, hum=hum)
        #dispatcher.utter_template("utter_temp", tracker, temp=temp)
        return []
class ActionAllReply(Action):
    def name(self)-> Text:
        return "bard_action"
    
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker, 
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message=tracker.latest_message['text']
        response=search.get_answer(message)
        response_content=response['content']

        images = response.get('images', [])
        print(response_content)
        dispatcher.utter_message(response_content)
        #for image_url in images:
        for image_url in images:
              
              dispatcher.utter_message(image=image_url, dims={"width": 40, "height": 30}, scale=0.5)  
           
        return []


        # for i, image_url in enumerate(images):
        #     if i < len(response_content):
        #         # Send the content
        #         dispatcher.utter_message(response_content[i])

        #     # Send the image
        #     dispatcher.utter_message(image=image_url, dims={"width": 50, "height": 50}, scale=0.5)



# greeting according to time of the day

class ActionGreetTimeBased(Action):
    def name(self) -> Text:
        return "time_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #     current_time = datetime.now()
            current_time = datetime.now()
            if current_time.hour <12:
                greeting="Good Morning!"
                message="I am here to guide you in Goa."
                #dispatcher.utter_message(text=greeting)
            elif current_time.hour >=12 and current_time.hour <18:
                greeting="Good AfterNoon!"
                message="I am here to guide you in Goa."
                #dispatcher.utter_message(text=greeting)
            else:
                greeting="Good Evening!"
                message= "I am here to guide you in Goa"
                #message=" Let me know your name first."
                #dispatcher.utter_message(text=greeting)
            #greeting = "Good morning" if current_time.hour < 12 else "Good afternoon"
            message = f"**{greeting}!**" + message
            
            dispatcher.utter_message(text=message,parse_mode="markdown")

 
            return []


# class ActionYourName(Action):
#      def name(self) -> Text:
#          return "utter_name"
#      def run(self, dispatcher: CollectingDispatcher, 
#              tracker: Tracker, 
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#              name=tracker.latest_message['text']
#              print(name)
             
#              dispatcher.utter_message(response = "utter_name", name = "Aimee")
#              return [] 
# class ActionCarousel(Action):
#      def name(self) -> Text:
#         return "action_carousels"
    
#      def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
#         message = {
#             "type": "template",
#             "payload": {
#                 "template_type": "generic",
#                 "elements": [
#                     {
#                         "title": "Raj Hotel",
#                         "subtitle": "Rs1000 per night",
#                         "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqhmyBRCngkU_OKSL6gBQxCSH-cufgmZwb2w&usqp=CAU",
#                         "buttons": [ 
#                             {
#                             "title": "Happy",
#                             "payload": "Happy",
#                             "type": "postback"
#                             },
#                             {
#                             "title": "sad",
#                             "payload": "sad",
#                             "type": "postback"
#                             }
#                         ]
#                     },
#                     {
#                         "title": "Carousel 2",
#                         "subtitle": "$12",
#                         "image_url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
#                         "buttons": [ 
#                             {
#                             "title": "Click here",
#                             "url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
#                             "type": "web_url"
#                             }
#                         ]
#                     }
#                 ]
#                 }
#         }
#         dispatcher.utter_message(attachment=message)
#         return []