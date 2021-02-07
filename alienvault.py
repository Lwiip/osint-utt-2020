#https://otx.alienvault.com/api
#https://github.com/AlienVault-OTX/OTX-Python-SDK

def mainalv(ip,url):
    """
    mainalv is managing alienvault api configuration and call api for IP or api for url. return a string in markdown style.
    :param ip:ip from user
    :param url:url from user
    """

    from OTXv2 import OTXv2
    import IndicatorTypes


    ############# API config #############
    API_KEY = 'ce0994aee9cfb6f8a4bcf2d5d7ba6b2e4bcb10efc125b508b1ee051f66b7e8fa'
    OTX_SERVER = 'https://otx.alienvault.com/'
    otx = OTXv2(API_KEY, server=OTX_SERVER)
    ############# String title #############
    stringalv = "##AlienVault"

    ############# IP #############
    if ip != None:
        alerts = ipalv(otx, ip, IndicatorTypes)
        if len(alerts) > 0:
            stringalv = '\n'.join([stringalv, "* {} is identified as potentially malicious".format(ip)])
            stringalv = '\n'.join([stringalv, "* {} is in {} AlienVault alerts".format(ip,len(alerts))])
            stringalv = '\n'.join([stringalv, "* [AlienVault source link](https://otx.alienvault.io/indicator/ip/{})".format(ip)])
        else:
            stringalv = '\n'.join([stringalv, "* {} is not identified as malicious".format(ip)])
            stringalv = '\n'.join([stringalv, "* [AlienVault source link](https://otx.alienvault.io/indicator/ip/{})".format(ip)])

    ############# URL#############
    if url != None:
        alerts = urlalv(otx, url, IndicatorTypes)
        if len(alerts) > 0:
            stringalv = '\n'.join([stringalv, "* {} is identified as potentially malicious".format(url)])
            stringalv = '\n'.join([stringalv, "* {} is in {} AlienVault alerts".format(url,len(alerts))])
            stringalv = '\n'.join([stringalv, "* [AlienVault source link](https://otx.alienvault.io/indicator/url/{})".format(url)])
        else:
            stringalv = '\n'.join([stringalv, "* {} is not identified".format(url)])
            stringalv = '\n'.join([stringalv, "* [AlienVault source link](https://otx.alienvault.io/indicator/url/{})".format(url)])
        
    ############# Rating#############
    grade = rating(len(alerts))


    return stringalv, grade


def rating(alerts):
    """
    rating calculate and return a grade based on alienvault pulse detection.
    :param alerts:int (number of pulse)
    """
    if alerts == 0:
        grade = 8
    elif 1 <= alerts <= 2:
        grade = 5
    elif 3 <= alerts <= 5:
        grade = 3
    elif 6 <= alerts <= 10:
        grade = 2
    elif alerts > 10:
        grade = 1

    return grade


# Get a nested key from a dict
def getValue(results, keys):
    if type(keys) is list and len(keys) > 0:

        if type(results) is dict:
            key = keys.pop(0)
            if key in results:
                return getValue(results[key], keys)
            else:
                return None
        else:
            if type(results) is list and len(results) > 0:
                return getValue(results[0], keys)
            else:
                return results
    else:
        return results


def ipalv(otx, ip, IndicatorTypes):
    alerts = []
    result = otx.get_indicator_details_by_section(IndicatorTypes.IPv4, ip, 'general')

    # Return nothing if it's in the whitelist
    validation = getValue(result, ['validation'])
    if not validation:
        pulses = getValue(result, ['pulse_info', 'pulses'])
        if pulses:
            for pulse in pulses:
                if 'name' in pulse:
                    alerts.append('In pulse: ' + pulse['name'])

    return alerts



def urlalv(otx, url, IndicatorTypes):
    alerts = []
    result = otx.get_indicator_details_full(IndicatorTypes.URL, url)

    google = getValue( result, ['url_list', 'url_list', 'result', 'safebrowsing'])
    if google and 'response_code' in str(google):
        alerts.append({'google_safebrowsing': 'malicious'})


    clamav = getValue( result, ['url_list', 'url_list', 'result', 'multiav','matches','clamav'])
    if clamav:
            alerts.append({'clamav': clamav})

    avast = getValue( result, ['url_list', 'url_list', 'result', 'multiav','matches','avast'])
    if avast:
        alerts.append({'avast': avast})

    # Get the file analysis too, if it exists
    has_analysis = getValue( result,  ['url_list','url_list', 'result', 'urlworker', 'has_file_analysis'])
    if has_analysis:
        hash = getValue( result,  ['url_list','url_list', 'result', 'urlworker', 'sha256'])
        file_alerts = file(otx, hash)
        if file_alerts:
            for alert in file_alerts:
                alerts.append(alert)

    return alerts



