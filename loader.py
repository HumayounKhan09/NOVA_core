"""
Author: Humayoun Khan
File Name: loader.py
Purpose: loader file to enforce schema rules
"""
    #imports 
from datetime import datetime 
from apscheduler.triggers.cron import CronTrigger
from reminders_obj import reminders_obj
from apscheduler.triggers.date import DateTrigger
#Creating the function that makes the loader work:
def load_reminders(data: dict) -> list[reminders_obj]:
#need to have a run time assertion of the data type I want

    if not isinstance(data, dict):
        raise TypeError("This is not the right type for config.")

    else:
        #Dict is a hash table
        #check if reminders are in data
        if "reminders" not in data:
            raise ValueError("reminders is not in data")
        else: 
            if type(data["reminders"])!= list:
                raise ValueError("This is not a list")
            else:
                #Turns out that I only need to loop through this once
                #extract the list of dict
                reminder = data["reminders"]
                loaded_reminders =[]
                for i, reminders in enumerate(reminder):
                    #need to check if everything here is a dict 
                    #why tf do I need so much error checking??
                    if not isinstance(reminders,dict):
                        raise ValueError(f"reminder at index {i} is not a dict")

                    #now I need to check the individual segments of this
                    elif "id" not in reminders or not isinstance(reminders["id"],str):
                        raise ValueError("id is not in reminders or it is not a string")

                    elif not reminders["id"].strip(): #empty or all space string
                        raise ValueError("The id is empty")

                    elif "message" not in reminders or not isinstance(reminders["message"],str):
                        raise ValueError("Not in reminder or not a string")

                    elif not reminders["message"].strip():
                        raise ValueError("Why is the message empty?")

                    elif "time" in reminders and "cron" in reminders:
                        raise ValueError("Not supposed to have both")

                    elif "time" not in reminders and "cron" not in reminders:
                        raise ValueError("You need to have atleast one time or cron obj")
                    #The user will be selecting a time, not inputting it.

                    if "enabled" not in reminders:
                        reminders.setdefault("enabled", True)

                    if "time" in reminders:
                        try:
                            temp = datetime.fromisoformat(reminders["time"])
                            trigger = DateTrigger(run_date=temp)
                        except ValueError:
                            raise ValueError(f"Invalid ISO-8601 timestamp for reminder '{reminders['id']}': {reminders['time']}")

                    else: 
                        try: 
                            trigger = CronTrigger.from_crontab(reminders["cron"])
                            
                        except Exception as e:
                            raise ValueError(f"Invalid cron expression for reminder '{reminders['id']}': {e}")

                    remindersObject = reminders_obj(reminders["id"], reminders["message"],reminders["enabled"],trigger)

                    loaded_reminders.append(remindersObject)

    return loaded_reminders


        
