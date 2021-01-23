def mainbing(ip):
    """
    Description of the function
    :param datauser:dictionnary, ip and url from user 
    """

    from selenium import webdriver
    from selenium.webdriver.common import keys, action_chains
    #used for sleep
    import time
    #used for extracting domains from url
    from urllib.parse import urlparse
    #used to check if it's a valide domain
    # pip install validators
    import validators


    browser=webdriver.Firefox()
    browser.get('https://www.bing.com')
    element = browser.find_element_by_id('sb_form_q')
    element.send_keys('ip: {}'.format(ip))
    element.send_keys(keys.Keys.ENTER)


    #sleep to wait the rendering and download of the page
    time.sleep(1)
    elements = browser.find_elements_by_class_name('b_attribution')

    #Get domains
    domains = []
    for link in elements:
        if validators.domain(link.text):
            domains.append(link.text)
        else:
            domain = urlparse(link.text).netloc
            if validators.domain(domain):
                domains.append(domain)
            else:
                continue
                
    uniqdomains = set(domains)
    domains = list(uniqdomains)

    stringbing = "##Bing domains lookup"

    for domain in domains:
        stringbing = '\n'.join([stringbing, "* {}".format(domain)])

    browser.close()
    return stringbing
