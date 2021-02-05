# osint-utt-2020
Repo for the osint project - utt 2020

## Install
- python -m venv /path/to/project/env_name_of_the_project
- cd env_name_of_the_project
- source bin/activate
- git clone https://github.com/Lwiip/osint-utt-2020.git
- pip install vt-py
- pip install markdown
- pip install requests
- pip install OTXv2
- pip install jupyter 
- pip install -U selenium 
- wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
- tar -xzvf geckodriver-v0.28.0-linux64.tar.gz 
- sudo mv geckodriver /usr/bin  
- export PATH=$PATH:/usr/bin

## Run 
- source env_name_of_the_project/bin/activate
- python3 main.py

## Récupération d'informations
Récupérations d'informations IP/hostname via l'utilisation de différents services.
Command line tool modulaire.
- Input: IP, hostname (file with IP or hostname). 
- Output: affichage dans l'invite de commande ou export dans un fichier. 

Sources à utiliser:

- bing v host dork: En cours
- VirusTotal: En cours
- shodan : En cours
  
- whois/host: En cours
- Alienvault: En cours
- URLhaus: todo
- geoloc todo

## Score de malveillance bayésien
Utilisation d'une échelle bayésienne avec mise à jour des crédences en fonction des données.
Demander un préjugé entre 0 et 10 à l'utilisateur (ou prendre une valeur par défault).
En fonction des retours des modules, mettre à jour la crédence puis afficher le résultat sur une échelle entre 0 et 10.
Chaque module doit donner une note entre 0 et 10, une fonction fera l'incrémentation/décrémentation de l'échelle.
    

