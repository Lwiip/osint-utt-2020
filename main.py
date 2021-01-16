import argparse
import virustotal


###################################################
#options
###################################################
parser = argparse.ArgumentParser()
parser.add_argument("-vt", "--virustotal", help="", action="store_true")  
args = parser.parse_args()

print(args.virustotal)

if args.virustotal:
    #function to do in virustotal
    virustotal


# option pour activer les modules. 
# mettre dans un dictionnaire une ip ou une url.
# faire passer ce dictionnaire aux différents scripts
# script retourne au main les résultats sous forme de tableau pandas ?


#Bonus detection automatique des noms des fichiers pour juste ajouter les modules de manières indépendantes ??

