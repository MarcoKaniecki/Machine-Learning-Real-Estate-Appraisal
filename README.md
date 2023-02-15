# Using Deep Learning for Real Estate Appraisal

## Local Installation
Find or create a directory where you want to store the repo

```console
git clone https://github.com/MarcoKaniecki/Deep-Learning-Real-Estate-Appraisal
```

```console
cd Deep-Learning-Real-Estate-Appraisal
```

### Setup the virtual environment for backend
#### MacOS
```console
python3 -m venv env
source env/bin/activate
```

#### Windows
```console
py -m venv env
```

`.\env\Scripts\activate`

Install backend dependencies
```console
cd backend
pip install -r ../requirements.txt
```

Setup database
```console
python manage.py makemigrations
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
yarn install
yarn start
```
