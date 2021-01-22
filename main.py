import argparse
import sys
import virustotal
import markdown
import webbrowser
import os
import shodan


###################################################
#options and inputs from user
###################################################
parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="Indicate the IP address to look for")   
parser.add_argument("-url", help="Indicate the url to look for")   
parser.add_argument("-vt", "--virustotal", help="virustotal check", action="store_true")  
parser.add_argument("-shodan", help="Shodan check",action="store_true") 
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
#IP
###################################################
string = "#OSINT PROJECT UTT 2020-2021"


if datauserip != {}:
    for _, ip in datauserip.items():

        stringip = '''-----------------
# {}\n'''.format(ip)
        string = '\n'.join([string, stringip])

        ############# VirusTotal #############
        if args.virustotal:
            stringvt = virustotal.mainvt(ip, None)
            string = '\n'.join([string, stringvt])

        ############### Shodan ###############
        if args.shodan:
            stringshodan = shodan.mainshodan(ip, None)
            print ("stringshodan =======> ", stringshodan)
            string = '\n'.join(["".join(x) for x in stringshodan])
            
   
###################################################
#URL
###################################################
if datauserurl!= {}:
    for _, url in datauserurl.items():

        stringurl = '''-----------------
# {}\n'''.format(url)
        string = '\n'.join([string, stringurl])

        ############# Virus Total #############
        if args.virustotal:
            stringvt = virustotal.mainvt(None, url)
            string = '\n'.join([string, stringvt])

      
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

