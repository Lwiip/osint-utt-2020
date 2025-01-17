import argparse
import sys
import virustotal
import bing
import whois
import alienvault
import markdown
import webbrowser
import os
import shodan
import urlhaus
import geoloc
import rating

###################################################
#options and inputs from user
###################################################
parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="Indicate the IP address to look for")   
parser.add_argument("-url", help="Indicate the url to look for")
parser.add_argument("-g", "--grade", help="Indicate your bias grade")  
parser.add_argument("-vt", "--virustotal", help="virustotal check (URL/IP)", action="store_true")  
parser.add_argument("-sh", "--shodan", help="Shodan check (IP)",action="store_true") 
parser.add_argument("-bing", "--bing", help="bing domains check (IP)", action="store_true") 
parser.add_argument("-whois", "--whois", help="whois lookup (URL)", action="store_true") 
parser.add_argument("-alv", "--alienvault", help="alienvault check (URL/IP)", action="store_true")
parser.add_argument("-urlh", "--urlhaus", help="urlhaus check (URL/IP)",action="store_true")  
parser.add_argument("-geo", "--geoloc", help="geoloc check (URL/IP)",action="store_true")
parser.add_argument("-ALL", help="Launch of all options", action="store_true")   
args = parser.parse_args()

#if there is no ip or url specified by the user
if not args.ip and not args.url:
    print("you must specify an ip or an url, please retry")
    sys.exit()

# ----- Get inputs from user ----- 
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

# ----- Retrieving API Keys -----  
if (args.ALL or args.shodan or args.virustotal or args.alienvault or args.whois == True):
    if not os.path.isfile("api_keys.txt"): 
        print ("ERROR :", "The file 'api_keys.txt' containing the API keys does not exist.")
        sys.exit()

# ----- grade -----
dgrade = {}
if args.grade:
    biasgrade = int(args.grade)
else:
    biasgrade = 5

string = "#OSINT"
###################################################
#IP
###################################################
if datauserip != {}:
    for _, ip in datauserip.items():

        stringip = '''-----------------
# *{}*\n'''.format(ip)
        string = '\n'.join([string, stringip])

        ############### Shodan ###############
        if args.shodan or args.ALL:
            stringshodan, dgrade["shodan"] = shodan.mainshodan(ip)
            string = '\n'.join([string, stringshodan])

        ############# Geolocalisation #############
        if args.geoloc or args.ALL:
            stringgeo, dgrade["geoloc"] = geoloc.maingeoloc(ip, None)
            string = '\n'.join([string, stringgeo])

        ############# Bing domains lookup#############
        if args.bing  or args.ALL:
            stringbing = bing.mainbing(ip)
            string = '\n'.join([string, stringbing])
        
        ############# VirusTotal #############
        if args.virustotal or args.ALL:
            stringvt, dgrade["virustotal"] = virustotal.mainvt(ip, None)
            string = '\n'.join([string, stringvt])

        ############# AlienVault #############
        if args.alienvault  or args.ALL:
            stringalv, dgrade["alienvault"] = alienvault.mainalv(ip, None)
            string = '\n'.join([string, stringalv])
        
        ############# URLhaus #############
        if args.urlhaus or args.ALL:
            stringurlh, dgrade["urlhaus"] = urlhaus.mainURLhaus(ip, None)
            string = '\n'.join([string, stringurlh])

        ############# Rating #############
        stringgrade = rating.maingrade(biasgrade, dgrade)
        string = '\n'.join([string, stringgrade])

        
###################################################
#URL
###################################################
if datauserurl!= {}:
    for _, url in datauserurl.items():

        stringurl = '''-----------------
# *{}*\n'''.format(url)
        string = '\n'.join([string, stringurl])

        
        ############# whois lookup#############
        if args.whois or args.ALL:
            stringwhois, dgrade["whois"] = whois.mainwhois(url)
            string = '\n'.join([string, stringwhois])

        ############# Geolocalisation #############
        if args.geoloc or args.ALL:
            stringgeo, dgrade["geoloc"] = geoloc.maingeoloc(None, url)
            string = '\n'.join([string, stringgeo])
        
        ############# Virus Total #############
        if args.virustotal or args.ALL:
            stringvt, dgrade["virustotal"]  = virustotal.mainvt(None, url)
            string = '\n'.join([string, stringvt])

        ############# AlienVault #############
        if args.alienvault or args.ALL:
            stringalv, dgrade["alienvault"] = alienvault.mainalv(None, url)
            string = '\n'.join([string, stringalv])
        
        ############# URLhaus #############
        if args.urlhaus or args.ALL:
            stringurlh, dgrade["urlhaus"] = urlhaus.mainURLhaus(None, url)
            string = '\n'.join([string, stringurlh])

        ############# Rating #############
        stringgrade = rating.maingrade(biasgrade, dgrade)
        string = '\n'.join([string, stringgrade])

        
###################################################
#Web browser output
###################################################
html = markdown.markdown(string)

f = open('output.html','w')
f.write(html)
f.close()

#Change path to reflect file location
filename = 'file:///'+os.getcwd()+'/' + 'output.html'
webbrowser.open_new_tab(filename)

