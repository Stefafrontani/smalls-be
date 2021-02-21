# Smalls - The API guide


## Main techs used:
`django`: as the main tech to build the rest api


## Description:
The project works as an api, letting a web user:
- save the posts the user likes the most 
- retrieve all posts saved
- deleting a post saved previously 


## Project structure:
  ./smalls-exercise\
  ./posts\
  -- db.sqlite3\
  -- manage.py\
  -- Pipfile\
  -- Pipfile.lock\
  -- readme.md\
  -- requirements.txt

- *./smalls-exercise*\
This is the where all the project-level settings live.
Every app (i.e.: posts) should be connected to this main directory.
If others apps are start being used, then, a folder `./apps` should be created to organize them 

- *./posts*\
The only domain the project required.
Every piece of source code writen is here. Except for some settings. *(i.e.: Models, Serializers, Views, etc.)*

- *db.sqlite3*\
--

- *manage.py*\
File where every command is executed from. *(i.e.: py manage.py script)*

- *Pipfile*
- *Pipfile.lock*\
Both created while pipenv was started. They mantain the status of the virtual environment created for the project

- *requirements.txt*\
The dependencies the projects need to run. The list writen there is the same that you could get while running *pipenv freeze* while on the virtual environment, after installing the dependencies.

- *readme.md*\
Here we are...


## Requirements and Installation:

1) Download and install python and pip:\
[python](https://www.python.org/downloads/)\
[pip](https://pip.pypa.io/en/stable/installing/)\
*Note: **pip** is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4*

2) Install pipenv
`pipenv` : For windows would be: *$ pip install pipenv*

3) Initialize virtual environment with pipenv while in the root of the repo
*$ pipenv shell*

4) Install the dependencies
*$ pipenv install* : Will install what is in the pipfiles


## Running the server

On the root of the project and after having started the virtual environment, run: *$py manage.py runserver* and visit *http://localhost:8000/posts/*
