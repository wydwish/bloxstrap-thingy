import json
import os
from time import sleep
from colored import Fore

purple, red, green, white, gray = [Fore.rgb(*c) for c in [(211, 115, 212), (255, 56, 56), (36, 116, 255), (255, 255, 255), (87, 87, 87)]]

settingsPath = os.path.expanduser('~') + "\\AppData\\Local\\Bloxstrap\\Settings.json"

def currentSettings():
    try:
        with open(settingsPath, "r") as f:
            data = json.load(f)
        channel = data.get("Channel", "Not Set")

        channelChangeMode = data.get("ChannelChangeMode", 0)
        if channelChangeMode == 0:
            channelChangeMode = "Change Automatically"
        elif channelChangeMode == 1:
            channelChangeMode = "Always Prompt"
        elif channelChangeMode == 2:
            channelChangeMode = "Never Change"

        behaviorTabEnabled = data.get("OhHeyYouFoundMe", False)
        behaviorTabEnabled = "Yes" if behaviorTabEnabled else "No"

        return channel, channelChangeMode, behaviorTabEnabled
    except Exception as e:
        print("Error loading settings:", e)
        return None


def updateSettings():
    with open(settingsPath, 'r+') as file:
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

def main():
    os.system('cls'); os.system('title ' + "Bloxstrap Channel Switcher")
    if not os.path.exists(settingsPath):
        print(f"{red}You do not have Bloxstrap installed, install it at https://github.com/pizzaboxer/bloxstrap")
        input("Click enter to exit")

    channel, ChannelChangeMode, behaviorTabEnabled = currentSettings()

    def blahblah():
        print(f"{white}If you have any issues or suggestions, make an issue thingy on the github repo!")
        print(f"{white}https://github.com/wydwish/bloxstrap-thingy")
        print(f"\n{white}[{red}REMINDER{white}]{red} Make sure you have ROBLOX closed before using this!\n")

        print(f"{white}[{green}Current Settings{white}]")
        print(f"{gray}- {white}[{green}ROBLOX Channel{white}] {green}{channel}")
        print(f"{gray}- {white}[{green}Channel Change Action{white}] {green}{ChannelChangeMode}")
        print(f"{gray}- {white}[{green}Behavior Tab Enabled{white}] {green}{behaviorTabEnabled}\n")

    blahblah()
    inp = input(f"{white}Are you sure you'd like to switch your channel to Live? (y/n) ")

    if inp == "n":
        os._exit(1)
    
    elif inp == "y":
        updateSettings()
        os.system('cls')
        blahblah()
        print(f"{white}Your channel has now been set to 'Live', Bloxstrap will prompt you a popup if ROBLOX attempts to change it.")
        input("Click enter to exit")
    
    else:
        main()

if __name__ == "__main__":
    main()
