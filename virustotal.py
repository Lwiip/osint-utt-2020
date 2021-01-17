
#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview


# Main vt
def mainvt(ip, url):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
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
    url_id = vt.url_id(urlstring)
    url = client.get_object("/urls/{}".format(url_id))

    stringvt = '\n'.join([stringvt, "* first_submission_date: {}".format(url.first_submission_date)])
    stringvt = '\n'.join([stringvt, "* last_analysis_date: {}".format(url.last_analysis_date)])
    stringvt = '\n'.join([stringvt, "* categories: {}".format(url.categories)])
    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(url.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(url.total_votes)])

    return stringvt
    

def vtip(vt, client, ipstring, stringvt):
    ip = client.get_object("/ip_addresses/{}".format(ipstring))

    stringvt = '\n'.join([stringvt, "* last_analysis_stats: {}".format(ip.last_analysis_stats)])
    stringvt = '\n'.join([stringvt, "* total_votes: {}".format(ip.total_votes)])

    return stringvt



