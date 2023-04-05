# Using Machine Learning for Real Estate Appraisal
Before starting, make sure you have [python3](https://www.python.org/downloads/), pip (comes with python3), and [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable) installed.

## Local Installation
Find or create a directory where you want to store the repo

```console
git clone https://github.com/MarcoKaniecki/Machine-Learning-Real-Estate-Appraisal
```

```console
cd Machine-Learning-Real-Estate-Appraisal
```
## Running with Launcher (Windows Only)
Running 'WindowsLauncher.py' within the top level of the repository will run all necessary steps to run the server, open data in Django database, and frontend webpage.
Please note that you will have to refresh http://127.0.0.1:8000 after the script runs in order to see the data.
If you run into issues using this or you are using a different OS, see the manual steps below.

## Steps for Manual Setup
### Setup the virtual environment for backend
#### MacOS
```console
python3 -m venv env
```
```console
source env/bin/activate
```

#### Windows
```console
py -m venv env
```
```console
.\env\Scripts\activate
```

### Create comps database
```console
python backend/CompDatabase/CreateDatabase.py
```
## Import data from CSV (Using ames.csv as a test dataset)
```console
python backend/CompDatabase/InsertDataFromCSV.py backend/ML_components/format_and_train_model/ames.csv
```

### Install backend dependencies
```console
cd backend
```
```console
pip install -r ../requirements.txt
```

Setup database
```console
python manage.py makemigrations
```
```console
python manage.py migrate
```

**Optional**: Setup superuser to add data from backend into database. Enter a username, a random email and a password to access the admin panel
```console
python manage.py createsuperuser
```

Run backend server
```console
python manage.py runserver 8000
```

Go to
http://127.0.0.1:8000/api/posts/
to see data in database


**Optional** (need to have created a superuser): Go to the following url to add sample data which will be displayed in http://127.0.0.1:8000/api/posts/ URL.

### Setup frontend
Open a new terminal
```console
cd frontend
```
```console
yarn install
```
```console
yarn start
```
