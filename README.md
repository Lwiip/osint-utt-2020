# osint-utt-2020
Repo for the osint project - utt 2020


Virtualbox - osint VM

## Install
- python -m venv /path/to/project/env_name_of_the_project
- cd env_name_of_the_project
- source bin/activate
- git clone https://github.com/Lwiip/osint-utt-2020.git
- pip install jupyter 
- pip install -U selenium 
- wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
- tar -xzvf geckodriver-v0.28.0-linux64.tar.gz 
- sudo mv geckodriver /usr/bin  
- export PATH=$PATH:/usr/bin
- jupyter notebook 

## Run 
- source env_name_of_the_project/bin/activate
- jupyter notebook 


## TODO
Programme python permettant de récupérer des informations sur une IP (puis dans un second temps sur plusieurs IP, par exemple en lui donnant une ip en entrée ou un fichier avec plusieurs IP).
Calcul d'un score de malveillance sur une IP
Notes: IP ou domain name. Fonctionnement par module. 

Sources à utiliser:
- bing v host dork: OK
- VirusTotal
- shodan 
- Alienvault
- URLhaus
- Twitter
- RADB 
- geoloc 
- alexa ranking


    

