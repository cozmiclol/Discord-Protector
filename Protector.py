# Imports
import os
import time
import sys
import ctypes

# Does it forever
while True:
    discpathuwu = os.path.join(os.getenv('LOCALAPPDATA'), 'Discord') # Opens the discord folder in localappdata
    for folder in os.listdir(discpathuwu): # Lists all of the folders in the discord folder
        if folder.startswith("app-"): # Opens the app {version} folder
            pathuwu = os.path.join(discpathuwu, folder, 'modules', 'discord_desktop_core-1', 'discord_desktop_core', 'index.js') # Gets to the index.js file (where injection is stored)
            with open(pathuwu, 'r', encoding='utf-8') as f: # opens the index.js file as read only
                code = f.read() # reads it
            if code != "module.exports = require('./core.asar');": # if the code is not the usual code
                with open(pathuwu, 'w', encoding='utf-8') as f: # opens it as write only
                    f.write("module.exports = require('./core.asar');") # writes the usual code
                    ctypes.windll.user32.MessageBoxW(0, "Your discord Index.js file was found to be injected with malware. (CLEANED)", "Error", 0x10) # gives u a message box that tells u if u had malware
    time.sleep(5) # zzz
