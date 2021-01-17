
#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview




# Main vt
def mainvt(datauserip, datauserurl):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
    """
    # API config
    import vt
    apikey = "2285799e398a78710bd7f2181cc971fbfca0dc59b6311f7b7f18924c87550df6"
    client = vt.Client(apikey)
        
    
    #IP
    if datauserip != {}:
        for _, ip in datauserip.items():
            vtip(vt, client, ip)
    #URL
    if datauserurl != {}:
        for _, url in datauserurl.items():
            vturl(vt, client, url)
    

    #Close API
    client.close()

    
def vturl(vt, client, url):
    url_id = vt.url_id(url)
    url = client.get_object("/urls/{}".format(url_id))
    print(url.last_analysis_stats)


#def vtip(vt, ip):



