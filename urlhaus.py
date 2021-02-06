# ---------------------------------------------------------------------------------------
# URLhaus Documentation :
# https://urlhaus.abuse.ch/
# https://urlhaus.abuse.ch/api/
# https://urlhaus-api.abuse.ch/
# ---------------------------------------------------------------------------------------

############# API config #############
import json
import requests

def mainURLhaus(ip, url):
    '''
    mainURLhaus is managing URLhaus api configuration and call api for IP or api for url. return a string in markdown style.
    :param ip:ip from user
    :param url:url from user
    '''

    ############# String title #############
    stringURLhaus = "##URLhaus lookup"

    #### IP ####
    if ip != None:
        stringURLhaus = URLhaus_ip(ip, stringURLhaus)
    #### URL ####
    if url != None:
        stringURLhaus = URLhaus_url(url, stringURLhaus)

    return stringURLhaus



def URLhaus_ip(ip, stringURLhaus):
    '''
    :param ip:ip from user
    :param stringURLhaus:string to concatenate return 
    '''
    data_host = {"host":ip}
    # The host (IPv4 address, hostname or domain name) you want to query (case insensitive)
    response = requests.post('https://urlhaus-api.abuse.ch/v1/host/', data=data_host, timeout=15)
    if response.status_code==200:
        res=response.json()
        query_status = res['query_status']
        if query_status == "ok":
            stringURLhaus = '\n'.join([stringURLhaus, "* Host: {}".format(res['host'])])
            stringURLhaus = '\n'.join([stringURLhaus, "* Firstseen: {}".format(res['firstseen'])])
            stringURLhaus = '\n'.join([stringURLhaus, "* Malware URLs: {}".format(res['url_count'])])
            
            for obj in res['urls']: # List all objects of the "payloads" key 
                for key, value in obj.items():
                    if key == "url":
                        stringURLhaus = '\n'.join([stringURLhaus, "     * {}".format(value)])
            
            stringURLhaus = '\n'.join([stringURLhaus, "* [URLhaus source link](https://urlhaus.abuse.ch/host/{})".format(ip)])
        else:
            # Return message from URLhaus when the "query_status" equals "no_results" or "invalid_url"
            stringURLhaus = '\n'.join([stringURLhaus, "* URLhaus : ", query_status])
    else:
        stringURLhaus = '\n'.join([stringURLhaus, "* URLhaus failed"])
    return (stringURLhaus)


def URLhaus_url(url, stringURLhaus):
    '''
    :param url:url from user
    :param stringURLhaus:string to concatenate return 
    '''
    data_host = {"url":url}
    response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data=data_host, timeout=15)
    if response.status_code==200:
        res=response.json()
        query_status = res['query_status']
        if query_status == "ok":
            stringURLhaus = '\n'.join([stringURLhaus, "* Host: {}".format(res['host'])])
            stringURLhaus = '\n'.join([stringURLhaus, "* Date_added: {}".format(res['date_added'])])
            stringURLhaus = '\n'.join([stringURLhaus, "* Threat: {}".format(res['threat'])])

            for obj in res['payloads']: # List all objects of the "payloads" key 
                for key, value in obj.items():
                    if key == "firstseen" or key == "filename" or key == "file_type":
                        stringURLhaus = '\n'.join([stringURLhaus, "     * {}: {}".format(key,value)])

            stringURLhaus = '\n'.join([stringURLhaus, "* [URLhaus source link](https://urlhaus.abuse.ch/url/{})".format(res['id'])])
        else:
            # Return message from URLhaus when the "query_status" equals "no_results" or "invalid_url"
            stringURLhaus = '\n'.join([stringURLhaus, "* URLhaus : ", query_status])
    else:
        stringURLhaus = '\n'.join([stringURLhaus, "* URLhaus failed"])
    return (stringURLhaus)