
#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview


# Main vt
def mainvt(ip, url):
    """
    mainvt is managing virustotal api configuration and call api for IP or api for url. return a string in markdown style.
    :param ip:string, ip from user
    :param url:string, url from user
    """
    ############# API config #############
    import vt
    
    # ---- Retrieving API Key ----    
    file = open('api_keys.txt', "r")
    for line in file:
        line=line.strip() #Removal of empty lines  
        if (line.find('api_key_virustotal') != -1):
            api_key_virustotal=line.partition('=')[2]
    file.close()
    client = vt.Client(api_key_virustotal)

    ############# String title #############
    stringvt = "##VirusTotal"
    
    ############# IP #############
    if ip != None:
        stringvt, last_analysis_stats = vtip(vt, client, ip, stringvt)
    ############# URL #############
    if url != None:
        stringvt, last_analysis_stats = vturl(vt, client, url, stringvt)
    
    ############# Rating #############
    grade = rating(last_analysis_stats)

    ############# API close #############
    client.close()
    
    return stringvt, grade

    
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

    stringvt = '\n'.join([stringvt, "* first_submission_date: {}".format(url.first_submission_date)])
    stringvt = '\n'.join([stringvt, "* last_analysis_date: {}".format(url.last_analysis_date)])
    stringvt = '\n'.join([stringvt, "* categories: {}".format(url.categories)])
    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(url.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(url.total_votes)])
    stringvt = '\n'.join([stringvt, "* [VirusTotal source link](https://www.virustotal.com/gui/url/{}/detection)".format(url_id)])

    return stringvt, url.last_analysis_stats
    

def vtip(vt, client, ipstring, stringvt):
    """
    vtip request vt api for ip and return mardown string with informations from vt.
    :param vt:virus total import
    :param client:virustotal client api
    :param ipstring:string with the ip to request
    :param stringvt:string to concatenate return 
    """

    ip = client.get_object("/ip_addresses/{}".format(ipstring))

    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(ip.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(ip.total_votes)])
    stringvt = '\n'.join([stringvt, "* [VirusTotal source link](https://www.virustotal.com/gui/ip-address/{}/detection)".format(ipstring)])

    return stringvt, ip.last_analysis_stats


def rating(last_analysis_stats):
    """
    rating calculate and return a grade based on virus total malicious and suspicious detection.
    :param last_analysis_stats:virus total stats
    """
    nbnotclean = last_analysis_stats['malicious'] + last_analysis_stats['suspicious']
    if nbnotclean == 0:
        grade = 8
    elif 1 <= nbnotclean <= 2:
        grade = 5
    elif 3 <= nbnotclean <= 5:
        grade = 3
    elif 6 <= nbnotclean <= 10:
        grade = 2
    elif nbnotclean > 10:
        grade = 1

    return grade





