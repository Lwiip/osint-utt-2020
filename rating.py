def maingrade(biasgrade, dgrade):
    """
    maingrade is calculating the grade based on user bias grade and grades from plugins. Return a string in markdown style with a grade between 0 and 10.
    :param biasgrade:int, grade from user
    :param dgrade:dictionnary with grades from plugins
    """

    import math
    #print(dgrade)

    # weight based on confidance on plugins grades.
    dpoids = {'virustotal':8,'urlhaus':7, 'alienvault':5, 'whois':5, 'shodan':3, 'geoloc':2}
    grade = biasgrade

    # Go all over plugins grades and update the user bias grade with plugins grades
    for key, gradekey in dgrade.items():
        difference = ((gradekey - grade) * dpoids[key])/10
        grade = grade + difference
    grade = round(grade,2)

    # String building
    if grade <= 3:
        stringgrade = "## ===> Grade: {}, most likely malicious".format(grade)
    elif 3 < grade <4.5 :
        stringgrade = "## ===> Grade: {}, maybe malicious".format(grade)
    elif 4.5 <= grade <= 5.5 :
        stringgrade = "## ===> Grade: {}, we don't know".format(grade)
    elif 5.5 < grade < 7:
        stringgrade = "## ===> Grade: {}, maybe clean".format(grade)
    elif grade >= 7:
        stringgrade = "## ===> Grade: {}, most likely clean".format(grade)

    return stringgrade

