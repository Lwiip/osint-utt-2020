def maingrade(biasgrade, dgrade):
    dpoids = {'virustotal':8,'urlhaus':7, 'alienvault':5, 'whois':5, 'shodan':3, 'geoloc':2}
    grade = biasgrade

    for key, gradekey in dgrade.items():

        #print("biasgrade {}".format(grade))
        #print("key {}".format(key))
        #print("note key {}".format(gradekey))
        #print(dpoids[key])

        difference = ((gradekey - biasgrade) * dpoids[key])/20

        grade = grade + difference

    #print(grade)
    return grade

