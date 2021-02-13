# osint-utt-2020
Repo for the osint project - utt 2020

## Install
- python3 -m venv /path/to/project/env_name_of_the_project
- cd env_name_of_the_project
- source bin/activate
- git clone https://github.com/Lwiip/osint-utt-2020.git
- pip3 install -r osint-utt-2020/requirements.txt  
- wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
- tar -xzvf geckodriver-v0.28.0-linux64.tar.gz 
- sudo mv geckodriver /usr/bin  
- export PATH=$PATH:/usr/bin

## Run 
- source env_name_of_the_project/bin/activate
- python3 main.py -g 7 -url http://google.fr -ALL

## Sources
- bing v host dork
- VirusTotal
- shodan
- whois/host
- Alienvault
- URLhaus
- geoloc