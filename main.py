import argparse
import sys
import virustotal


###################################################
#options and inputs from user
###################################################
parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="Indicate the IP address to look for")   
parser.add_argument("-url", help="Indicate the url to look for")   
parser.add_argument("-vt", "--virustotal", help="virustotal check", action="store_true")  
args = parser.parse_args()

#if there is no ip or url specified by the user
if not args.ip and not args.url:
    print("you must specify an ip or an url, please retry")
    sys.exit()

#Get inputs from user
datauserip = {}
if args.ip:
    counter = 0
    for ip in args.ip.split(','):
        datauserip["ip_{0}".format(counter)] = ip
        counter = counter +1

datauserurl = {}
if args.url:
    counter = 0
    for url in args.url.split(','):
        datauserurl["url_{0}".format(counter)] = url
        counter = counter +1

###################################################
#launch options
###################################################
if args.virustotal:
    virustotal.mainvt(datauserip, datauserurl)





# option pour activer les modules. 
# mettre dans un dictionnaire une ip ou une url.
# faire passer ce dictionnaire aux différents scripts
# script retourne au main les résultats sous forme de tableau pandas ?


#Bonus detection automatique des noms des fichiers pour juste ajouter les modules de manières indépendantes ??

