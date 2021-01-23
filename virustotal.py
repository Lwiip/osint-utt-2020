
#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview


# Main vt
def mainvt(ip, url):
    """
    mainvt is managing virustotal api configuration and call api for IP or api for url. return a string in markdown style.
    :param ip:ip from user
    :param url:url from user
    """
    ############# API config #############
    import vt
    apikey = "2285799e398a78710bd7f2181cc971fbfca0dc59b6311f7b7f18924c87550df6"
    client = vt.Client(apikey)
    ############# String title #############
    stringvt = "##VirusTotal"
    
    ############# IP #############
    if ip != None:
        stringvt = vtip(vt, client, ip, stringvt)
    ############# URL#############
    if url != None:
        stringvt = vturl(vt, client, url, stringvt)
    
    ############# API close #############
    client.close()
    
    return stringvt

    
def vturl(vt, client, urlstring, stringvt):
    """
    vturl request vt api for url and return mardown string with informations from vt.
    :param vt:virus total import
    :param client:virustotal client api
    :param urlstring:string with the url to request
    :param stringvt:string to concatenate return 
    """
    url_id = vt.url_id(urlstring)
    url = client.get_object("/urls/{}".format(url_id))

    stringvt = '\n'.join([stringvt, "* [link](https://www.virustotal.com/gui/url/{}/detection)".format(url_id)])
    stringvt = '\n'.join([stringvt, "* first_submission_date: {}".format(url.first_submission_date)])
    stringvt = '\n'.join([stringvt, "* last_analysis_date: {}".format(url.last_analysis_date)])
    stringvt = '\n'.join([stringvt, "* categories: {}".format(url.categories)])
    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(url.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(url.total_votes)])

    return stringvt
    

def vtip(vt, client, ipstring, stringvt):
    """
    vtip request vt api for ip and return mardown string with informations from vt.
    :param vt:virus total import
    :param client:virustotal client api
    :param ipstring:string with the ip to request
    :param stringvt:string to concatenate return 
    """

    ip = client.get_object("/ip_addresses/{}".format(ipstring))

    stringvt = '\n'.join([stringvt, "* [link](https://www.virustotal.com/gui/ip-address/{}/detection)".format(ipstring)])
    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(ip.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(ip.total_votes)])

    return stringvt



