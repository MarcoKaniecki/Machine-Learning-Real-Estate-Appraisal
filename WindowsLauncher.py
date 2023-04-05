#WindowsLauncher.py

#To run this, you must have python3, pip, and yarn installed. For help on this please view the Readme.

#Clone the github repository and run this script from the Deep-Learning-Real-Estate-Appraisal folder.

import subprocess
import webbrowser
import os

from backend.CompDatabase import CreateDatabase 
from backend.CompDatabase import InsertDataFromCSV

print( os.getcwd() )

# Define the command line arguments
root_commands = [
    'py -m venv env',
    '.\\env\\Scripts\\activate'
]

backend_commands = [
    'pip install -r ..\\requirements.txt',
    'python manage.py makemigrations',
    'python manage.py migrate',
    'python manage.py runserver 8000'
]

# Execute each command using subprocess
for command in root_commands:
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        exit(1)

# Open a new terminal for the frontend commands
subprocess.Popen('start cmd /k "cd frontend && yarn install && yarn start"', shell=True)

webbrowser.open("http://127.0.0.1:8000/api/posts/")
#You will need to refresh this page after the script finishes running. 

os.chdir("backend")

#Create and populate data in comps database
CreateDatabase()
InsertDataFromCSV("backend/ML_components/format_and_train_model/ames.csv")

for command in backend_commands:
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        exit(1)



