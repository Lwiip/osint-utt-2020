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
        grade = rating(res['result']['creation_date'])
        

    else:
        stringwhois = '\n'.join([stringwhois, "* Whois failed"])
        stringwhois = '\n'.join([stringwhois, "* [Whois source link](https://whois.domaintools.com/{})".format(domain)])
        grade = 5

    
    return stringwhois, grade



def rating(creation_date):
    """
    rating calculate and return a grade based on the creation date of the domain.
    :param creation_date: str
    """
    import datetime

    date_time_obj = datetime.datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S')
    daysfromcreation = datetime.datetime.now() - date_time_obj

    if daysfromcreation.days <= 31:
        grade = 2
    elif 32 <= daysfromcreation.days<= 353:
        grade = 5
    elif daysfromcreation.days >= 353:
        grade = 8

    return grade
