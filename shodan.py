
# https://www.shodan.io/
# https://shodan.readthedocs.io/en/latest/tutorial.html#connect-to-the-api

def mainshodan(ip, url):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
    """

############# API config #############
    import requests
    import time
    URL ='https://api.shodan.io/shodan/host/'
    API_KEY='pVR5NuSP5B9D3ay1En3p4MxizKqC3EuZ'
    
    IP = ip

############# Request  #############
    #r = requests.get(URL+IP, params={'key':API_KEY})
    isp = []
    r = requests.get(URL+IP.strip(), params={'key':API_KEY})
    if r.status_code==200:
        res=r.json()
        if 'isp' in res:
            isp.append(res['isp'])
            isp.append(res['domains'])
            isp.append(res['country_name'])
            isp.append(res['last_update'])            
        else:
            isp.append('Unknown')
    else:
        isp.append('Unknown')
    time.sleep(1)
    print (" =======> IPS:",isp)
    return (isp)