# SK_P4
# Administration documentation

#### This program has been written in Python 3.6

* #### Only if necessary, set the drive letter 
    `cd /d d:`

* #### Define the directory path that contains the application
    `cd D:\DOCUMENTS\FORMATION_PYTHON\PROJETS\PROJET_4\SK_P4`

* #### Create virtual environment
    `python -m venv env`
    
    Warning, if you use linux system:  
    `python3 -m venv env`  

    If the virtual environment was not created successfully, you need install this package:  
    `sudo apt-get install python3-venv`

* #### Run virtual environment
    `call  env/Scripts/activate.bat`
    
    Warning, if you use linux system or Mac OS:  
    `source env/bin/activate`  
    
    "(env)" is displayed if the environment have been activated

* #### If necessary, you can upgrade pip with this command
    `python -m pip install --upgrade pip`  

    Warning, if you use linux system:  
    `python3 -m pip install --upgrade pip` 

* #### Install all packages from requirements.txt
    `pip install -r requirements.txt`

* #### Create flake8 report
    `flake8 --format=html --htmldir=flake-report`  

* #### Start application
    `cd views`  

    If you use Windows:  
    `main.py`
    
    If you use Mac OS:  
    `python main.py`
    
    If you use Linux:  
    `python3 main.py`

* #### To exit environment
    `deactivate`

--------------------------------------------------------------------------------
If you need generate file requirements.txt  
`pip freeze > requirements.txt`

--------------------------------------------------------------------------------
# How to use this application

#### The main menu is divide by three parts :
* Enter 1 to acces Players Menu 
* Enter 2 to acces Tournaments Menu
* Enter 3 to access a Game Menu  

You need use numpad to navigate through them.

1. #### Players Menu :
    This menu contain alls options about players. You can :
    * add player
    * edit player ranking
    * print all players by alphabetical order
    * print all players by ranking  
    
    Warning, before start a game, you need absolutely add players to database.

2. #### Tournament Menu :
    With this menu, you can :
    * add a new tournament
    * print all tournaments
    * remove a tournament
    
    Warning, before start a game, you need absolutely add a tournament todatabase.
    
3. #### Game Menu :  
    You can do start a new game, but it's also possible resume a tournament.
    The "show game result" option you allow him to print all rapport about games
    * start a game
    * continue a game
    * show game results

    Happy enjoy !

    

