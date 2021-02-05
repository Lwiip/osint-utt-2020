#https://promptapi.com/marketplace/description/whois-api


def mainwhois(url):
    """
    mainwhois is asking whois api to have relevant informations on a domain. return a string in markdown style.
    :param url:url from user
    """
    ############# API config #############
    import validators
    from urllib.parse import urlparse
    import requests

    payload = {}
    headers= {
      "apikey": "is37APjFmekzxBScbSK1htp7SdeG8LHy"
    }

    ############# String title #############
    stringwhois = "##Whois lookup"
    
    ############# Domain extraction#############
    if validators.domain(url):
            domain = url
    else:
        domain = urlparse(url).netloc

    ############# API call#############
    apiurl = "https://api.promptapi.com/whois/query?domain={}".format(domain)
    response = requests.request("GET", apiurl, headers=headers, data = payload)
    status_code = response.status_code
    result = response.text

    ############# String building#############
    if response.status_code==200:
        res=response.json()

        stringwhois = '\n'.join([stringwhois, "* registrar: {}".format(res['result']['registrar'])])
        stringwhois = '\n'.join([stringwhois, "* creation date: {}".format(res['result']['creation_date'])])
        stringwhois = '\n'.join([stringwhois, "* expiration date: {}".format(res['result']['expiration_date'])])
        stringwhois = '\n'.join([stringwhois, "* updated date: {}".format(res['result']['updated_date'])])
        stringwhois = '\n'.join([stringwhois, "* name servers: {}".format(res['result']['name_servers'])])
        stringwhois = '\n'.join([stringwhois, "* [Whois source link](https://whois.domaintools.com/{})".format(domain)])

    else:
        stringwhois = '\n'.join([stringwhois, "* Whois failed"])
        stringwhois = '\n'.join([stringwhois, "* [Whois source link](https://whois.domaintools.com/{})".format(domain)])

    
    return stringwhois


