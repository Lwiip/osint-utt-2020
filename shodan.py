
# https://www.shodan.io/
# https://shodan.readthedocs.io/en/latest/tutorial.html#connect-to-the-api

def mainshodan(ip):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
    """

############# API config #############
    import shodan
    import requests
    URL ='https://api.shodan.io/shodan/host/'
    API_KEY='pVR5NuSP5B9D3ay1En3p4MxizKqC3EuZ'
    
    ############# String title #############
    stringshodan = "##Shodan"

############# Request  #############
    response = requests.get(URL+ip.strip(), params={'key':API_KEY})
    if response.status_code==200:
        res=response.json()
        stringshodan = '\n'.join([stringshodan, "* ISP: {}".format(res['isp'])])
        stringshodan = '\n'.join([stringshodan, "* domains: {}".format(res['domains'])])
        stringshodan = '\n'.join([stringshodan, "* Hostnames: {}".format(res['hostnames'])])
        stringshodan = '\n'.join([stringshodan, "* country name: {}".format(res['country_name'])])
        stringshodan = '\n'.join([stringshodan, "* last update: {}".format(res['last_update'])])
        stringshodan = '\n'.join([stringshodan, "* ports: {}".format(res['ports'])])
        stringshodan = '\n'.join([stringshodan, "* [Shodan source link](https://www.shodan.io/host/{})".format(ip)])
    else:
        stringshodan = '\n'.join([stringshodan, "* Shodan failed"])
    return (stringshodan)