#https://ip-api.com/docs/api:json


def maingeoloc(ip,url):
    """
    maingeoloc is requesting geolocation api to have relevant geolocation on a domain or IP. return a string in markdown style.
    :param ip:ip from user
    :param url:url from user
    """

    ############# Import #############
    import requests
    import validators
    from urllib.parse import urlparse

    ############# String title #############
    stringgeo = "##geolocation lookup"


    ############# Input selection #############
    if ip:
        inputuser = ip
    if url:
        if validators.domain(url):
                inputuser = url
        else:
            inputuser = urlparse(url).netloc

    ############# API call#############
    apiurl = "http://ip-api.com/json/{}".format(inputuser)
    response = requests.request("GET", apiurl)

    ############# String building#############
    if response.status_code==200:
        res=response.json()
        stringgeo = '\n'.join([stringgeo, "* country: {}".format(res['country'])])
        stringgeo = '\n'.join([stringgeo, "* city: {}".format(res['city'])])
        stringgeo = '\n'.join([stringgeo, "* [geolocation source link](https://ip-api.com/#{})".format(inputuser)])

    else:
        stringgeo = '\n'.join([stringgeo, "* geolocation failed"])
        stringgeo = '\n'.join([stringgeo, "* [geolocation source link](https://ip-api.com/#{})".format(inputuser)])
    
    return stringgeo