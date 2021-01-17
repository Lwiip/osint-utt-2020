
#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview


# Main vt
def mainvt(datauserip, datauserurl):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
    """
    ############# API config #############
    import vt
    apikey = "2285799e398a78710bd7f2181cc971fbfca0dc59b6311f7b7f18924c87550df6"
    client = vt.Client(apikey)
    
    ############# IP #############
    if datauserip != {}:
        for _, ip in datauserip.items():
            vtip(vt, client, ip)
    ############# URL#############
    if datauserurl != {}:
        for _, url in datauserurl.items():
            vturl(vt, client, url)
    
    ############# API close #############
    client.close()

    
def vturl(vt, client, urlstring):
    url_id = vt.url_id(urlstring)
    url = client.get_object("/urls/{}".format(url_id))


    print(url.first_submission_date)
    print(url.last_analysis_date)
    print(url.categories)
    #print(url.last_analysis_results)
    print(url.last_analysis_stats)
    print(url.total_votes)
    


def vtip(vt, client, ipstring):
    ip = client.get_object("/ip_addresses/{}".format(ipstring))

    #print(ip.last_analysis_results)
    print(ip.last_analysis_stats)
    print(ip.total_votes)



