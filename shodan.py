# ------------------------------------------------------------------------
# SHODAN Reference : 
# https://www.shodan.io/
# https://shodan.readthedocs.io/en/latest/tutorial.html#connect-to-the-api
# ------------------------------------------------------------------------


def mainshodan(ip):
    """
    mainshodan is managing Shodan api configuration and call api for IP. return a string in markdown style.
    :param ip:ip from user
    """

############# API config #############
    #import shodan
    import requests
    URL ='https://api.shodan.io/shodan/host/'

    # ---- Retrieving API Key ----    
    file = open('api_keys.txt', "r")
    for line in file:
        line=line.strip() #Removal of empty lines  
        if (line.find('api_key_shodan') != -1):
            api_key_shodan=line.partition('=')[2]
    file.close()

    ############# String title #############
    stringshodan = "##Shodan"
   
    ############# Request #############
    response = requests.get(URL+ip.strip(), params={'key':api_key_shodan})
    if response.status_code==200:
        res=response.json()
        stringshodan = '\n'.join([stringshodan, "* ISP: {}".format(res['isp'])])
        stringshodan = '\n'.join([stringshodan, "* domains: {}".format(res['domains'])])
        stringshodan = '\n'.join([stringshodan, "* Hostnames: {}".format(res['hostnames'])])
        stringshodan = '\n'.join([stringshodan, "* country name: {}".format(res['country_name'])])
        stringshodan = '\n'.join([stringshodan, "* last update: {}".format(res['last_update'])])
        stringshodan = '\n'.join([stringshodan, "* ports: {}".format(res['ports'])])

        if ( 'vulns' in res ): # Check if the "vulns" key exists in the "res" dictionary 
            stringshodan = '\n'.join([stringshodan, "* vulns: {}".format(res['vulns'])])
        stringshodan = '\n'.join([stringshodan, "* [Shodan source link](https://www.shodan.io/host/{})".format(ip)])

        #------- Rating -------
        grade = rating(res['ports'], res['country_name'], res['vulns'])

    else:
        stringshodan = '\n'.join([stringshodan, "* Shodan failed"])
    return (stringshodan, grade)


def rating(ports,country_name,vulns):
    """
    rating calculate and return a grade based on the country, ports and vulnerability 
    :param ports,country_name,vulns
    """
    #---- country ----
    if "China" or "Turkey" or "Russia" or "Taiwan" or "Brazil" or "Romania" or "India" or "Italy" or "Hungary" or "North korea" in country_name:
        grade_country = 4
    else:
        grade_country = 6
    
    #---- vulnerability ----
    if len(vulns) > 0 :
        grade_vulns = 4
    else:
        grade_vulns = 6
    
    #---- ports ----
    if "80" or "22" or "443" in ports:
        grade_ports = 7
    else:
        grade_ports = 4
    
    #---- average ----
    grade = (grade_country + grade_vulns + grade_ports)/3 
    
    return grade