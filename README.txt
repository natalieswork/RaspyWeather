1) theWeather by Natalie Lee

"theWeather" is a Flask web application that allows users to add/delete/view current weather data for multiple locations.

Additionally, users can add a nickname to each location. 

github repo: https://github.com/natalieswork/theWeather 


2) The contents of the ZIP file
This zip file contains...
Outermost Directory:
|-- main.py (run application here)
|-- requirements.txt
|-- .env (environment variables)

Website Directory:
|-- views.py (Flask Blueprint for rendering templates)
|-- models.py (scheme for db table)
|-- weather.py (backend for API connection)
|-- __init__.py (initalize Flask app and DB)

    Templates Directory:
    |-- base.html
    |-- index.html (home page)


3) The tech stack used was Flask, ultilizing Flask-SQLAlchemy for the database.


4) 
Set up:
- Ensure the existance of a `.env` file containing API_KEY, DB_NAME, and SECRET_KEY.
- From a terminal opened at this project's directory, create a virtual environment: `python -m venv .venv`
- Activate the virtual environment.
  macOS: `source .venv/bin/activate`
  PowerShell: `.venv\Scripts\Activate.ps1`
- Install requirements: `pip install -r requirements.txt`

Running The App:
- Using configured virtual environment, run the code in `main.py`
- After running, view app on local host link that appears in console. `http://127.0.0.1:5000`
