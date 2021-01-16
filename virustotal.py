import vt

#https://virustotal.github.io/vt-py/overview.html
#https://developers.virustotal.com/v3.0/reference#overview



# API config
apikey = "2285799e398a78710bd7f2181cc971fbfca0dc59b6311f7b7f18924c87550df6"
client = vt.Client(apikey)




# example
url_id = vt.url_id("http://www.virustotal.com")
url = client.get_object("/urls/{}".format(url_id))


#print
print(url.last_analysis_stats)


#Close API
client.close()

