    """
    Driver for scheduler
    """
import json
from loader import load_reminders
from sheduler import schedule_reminders
#parse json file
with open('config.json','r') as file:
    data = json.load(file)
    loaded_reminders = load_reminders(data)
    schedule_reminders(loaded_reminders)
    
file.close()

