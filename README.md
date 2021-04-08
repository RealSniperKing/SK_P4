# SK_P4

#### This program have written in Python 3.6

#### Only if necessary, set the drive letter 
`cd /d d:`

#### Define the directory path that contains the application
`cd D:\DOCUMENTS\FORMATION_PYTHON\PROJETS\PROJET_4\SK_P4`

#### Create virtual environment
`python -m venv env`

#### Run virtual environment
`call  env/Scripts/activate.bat`

#### Upgrade pip and install all packages from requirements.txt
`python -m pip install --upgrade pip`  
`pip install -r requirements.txt`

#### Create flake8 report
`flake8 --format=html --htmldir=flake-report`  

#### Start application
`cd views`
`main.py`

#### Après la fin du traitement. Désactiver l'environnement à l'aide de la commande
`deactivate`





####--------------------------------------------------------------------------------
#### Generate file requirements.txt
`pip freeze > requirements.txt`

