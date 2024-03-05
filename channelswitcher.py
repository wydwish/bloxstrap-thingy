import os
import json

settings_file_path = os.path.expanduser('~') + "\\AppData\\Local\\Bloxstrap\\Settings.json"

if os.path.isfile(settings_file_path):
    with open(settings_file_path, 'r+') as file:
        settings = json.load(file)
        
        updates = {
            "Channel": "Live",
            "ChannelChangeMode": 1,
            "OhHeyYouFoundMe": True
        }
        
        for key, value in updates.items():
            if key not in settings or settings[key] != value:
                settings[key] = value
                
        file.seek(0)
        json.dump(settings, file, indent=4)
        file.truncate()
        
    print("Your channel has now been set to 'Live' and Bloxstrap will prompt you if it attempts to be changed.")
else:
    print("Cannot find settings.json file for Bloxstrap. Make sure you have Bloxstrap installed!")
