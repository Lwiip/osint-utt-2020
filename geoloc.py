#https://ip-api.com/docs/api:json

import requests
import validators
from urllib.parse import urlparse
url = "https://mabanque.bnpparibas"


############# Domain extraction#############
if validators.domain(url):
        domain = url
else:
    domain = urlparse(url).netloc


apiurl = "http://ip-api.com/json/{}".format(domain)
response = requests.request("GET", apiurl)
status_code = response.status_code
result = response.text

############# String building#############
if response.status_code==200:
    res=response.json()

    print(res)

    print( "* registrar: {}".format(res['status']))

    #stringwhois = '\n'.join([stringwhois, "* registrar: {}".format(res['result']['registrar'])])
    #stringwhois = '\n'.join([stringwhois, "* creation date: {}".format(res['result']['creation_date'])])
    #stringwhois = '\n'.join([stringwhois, "* expiration date: {}".format(res['result']['expiration_date'])])
    #stringwhois = '\n'.join([stringwhois, "* updated date: {}".format(res['result']['updated_date'])])
    #stringwhois = '\n'.join([stringwhois, "* name servers: {}".format(res['result']['name_servers'])])
    #stringwhois = '\n'.join([stringwhois, "* [Whois source link](https://whois.domaintools.com/{})".format(domain)])

else:
    print("oops")
    #stringwhois = '\n'.join([stringwhois, "* Whois failed"])
    #stringwhois = '\n'.join([stringwhois, "* [Whois source link](https://whois.domaintools.com/{})".format(domain)])