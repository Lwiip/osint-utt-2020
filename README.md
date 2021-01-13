# osint-utt-2020
Repo for the osint project - utt 2020

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
Récupérations d'informations IP/hostname via l'utilisation de différents services.
Command line tool modulaire.
- Input: IP, hostname, file with IP or hostname. 
- Output: affichage dans l'invite de commande ou export dans un fichier. 
Calcul d'un score de malveillance ??


Sources à utiliser:

- whois/host: todo
- VirusTotal: todo
- shodan : todo
- URLhaus: todo
- bing v host dork: OK
- Alienvault: todo
- geoloc 
- alexa ranking
- Twitter

    

