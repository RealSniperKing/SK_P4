# SK_P4

#### This program has been written in Python 3.6

#### Only if necessary, set the drive letter 
`cd /d d:`

#### Define the directory path that contains the application
`cd D:\DOCUMENTS\FORMATION_PYTHON\PROJETS\PROJET_4\SK_P4`

#### Create virtual environment
`python -m venv env`

Warning, if you use linux system:  
`python3 -m venv env`  

If the virtual environment was not created successfully, you need install this package:  
`sudo apt-get install python3-venv`

#### Run virtual environment
`call  env/Scripts/activate.bat`

Warning, if you use linux system:  
`source env/bin/activate`  

#### If necessary, you can upgrade pip with this command
`python -m pip install --upgrade pip`  

Warning, if you use linux system:  
`python3 -m pip install --upgrade pip` 

#### Install all packages from requirements.txt
`pip install -r requirements.txt`

#### Create flake8 report
`flake8 --format=html --htmldir=flake-report`  

#### Start application
`cd views`  

If you use Windows:  
`main.py`

If you use Mac OS:  
`python main.py`

If you use Linux:  
`python3 main.py`
#### Après la fin du traitement. Désactiver l'environnement à l'aide de la commande
`deactivate`

--------------------------------------------------------------------------------
#### Generate file requirements.txt
`pip freeze > requirements.txt`

