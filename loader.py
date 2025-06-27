    """
    Author: Humayoun Khan
    File Name: loader.py
    Purpose: loader file to enforce schema rules
    """
    #imports 
    from datetime import datetime
   #Creating the function that makes the loader work:
   def load_reminders(data: dict) -> List[reminder]:
    #need to have a run time assertion of the data type I want
    try:
     assert isinstance(data, dict)

    except:

        print("This is not the correct data type")

    else:
        #Dict is a hash table
        #check if reminders are in data
        if "reminders" not in data:
            raise ValueError("reminders is not in data")
        else: 
            if type(data["reminders"])!= list:
                raise ValueError("This is not a list")
            else:
                for i, value in enumerate(data["reminders"]):
                    #need to check if everything here is a dict 
                    #why tf do I need so much error checking??
                    if not isintance(value,dict):
                        raise ValueError(f"reminder at index {i} is not a dict")
                    #now I need to check the individual segments of this
                if value["id"] == "":
                    raise ValueError("The Id field is blank")
                elif value["message"] == "":
                    raise ValueError("The message field is blank")
                elif "time" in value and "cron"in value:
                    raise ValueError("You can't have both")
                elif value["time"] == "":
                    raise ValueError("No time, are you nuts")
                else:
                    if "enabled" not in value:
                        value.update({"enabled": true})
                    else:
                        assert(type(value["enabled"])== bool & value["enabled"] == true | value["enabled"]== false)

                    #parsing the iso
                    date_time_obj = datetime.fromisoformat(value["time"])

 

        
