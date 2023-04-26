# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
import os

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConversationStart(Action):

    def name(self) -> Text:
        return "action_conversation_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        URL = f"http://{os.environ['FLASK_SERVER']}:{os.environ['FLASK_PORT']}/users"
        DATA = { "cif" : "12345" }

        r = requests.post(url = URL, json = DATA)

        data = r.json()
        print(f"URL: {URL} data: {DATA} action result: {data}")

        dispatcher.utter_message(text=data['msg'])
        dispatcher.utter_message(template="utter_conversation_start")
        
        return []
    
#https://github.com/RasaHQ/conversational-ai-course-3.x/blob/main/video-09-2-custom-forms/actions/actions.py
class ActionReclamation(Action):

    def name(self) -> Text:
        return "action_reclamation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_reclamation")
