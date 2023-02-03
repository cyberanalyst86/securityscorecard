import os
import requests
import sys
import time
import datetime
import pandas as pd

def colour_score(series):
    A_colour = 'background-color: #4ABA00;'
    B_colour = 'background-color: #E5BD00;'
    C_colour = 'background-color: #F08F00'
    D_colour = 'background-color: #F1431C'
    F_colour = 'background-color: #B40000'
    default = ''

    return [A_colour if (e >= 90 and e <= 100)
            else B_colour if (e >= 80 and e <= 89)
    else C_colour if (e >= 70 and e <= 79)
    else D_colour if (e >= 60 and e <= 69)
    else F_colour if (e >= 0 and e < 60)
    else default for e in series]


def colour_grade(series):
    A_colour    = 'background-color: #4ABA00;'
    B_colour = 'background-color: #E5BD00;'
    C_colour = 'background-color: #F08F00'
    D_colour = 'background-color: #F1431C'
    F_colour = 'background-color: #B40000'
    default = ''

    return [A_colour if e == "A"
            else B_colour if e == "B"
    else C_colour if e == "C"
    else D_colour if e == "D"
    else F_colour if e == "F"
    else default for e in series]


def output_to_excel(scorecard):

    now = datetime.datetime.now()
    dt_string=now.strftime("%d-%m-%Y")

    dt = datetime.datetime.today()
    month_number = dt.month
    year = dt.year

    month_dict = {1: 'January', 2: 'Febuary', 3: 'March',
                  4: 'April', 5: 'May', 6: 'June',
                  7: 'July', 8: 'August', 9: 'September',
                  10: 'October', 11: 'November', 12: 'December'}

    for key in month_dict:
        if month_number == key:
            month = month_dict[key]
        else:
            msg = "error"

    filepath = "C:\\Users\\Admin\\Downloads\\securityscorecard" + "\\" + month + "_" + str(year) + "\\"

    isExist = os.path.exists(filepath)

    if isExist == False:

        os.mkdir(filepath)

    else:

        error = "error"

    output_filepath = filepath + str(dt_string) + '_scorecard.xlsx'

    print("output excel to " + str(output_filepath));

    # -----------------------------------Sort Data Frame by Name -----------------------------------

    scorecard_sort = scorecard.sort_index(ascending=True)

    # -----------------------------------Apply Color By Rule Conditioning-----------------------------------

    #scorecard_colour = scorecard_sort.style.apply(colour_score, axis=0, subset=['Grade',
                                                                              #  'Application Security', 'Cubit Score',
                                                                              #  'Dns Health',
                                                                              #  'Endpoint Security', 'Hacker Chatter',
                                                                              #  'Ip Reputation',
                                                                              #  'Information Leak', 'Network Security',
                                                                              #  'Patching Cadence',
                                                                              #  'Social Engineering'])

    scorecard_colour = scorecard_sort.style.apply(colour_grade,  axis=0, subset=[
    'summary grade', 'application security grade',
                     'cubit grade', 'dns health grade', 'endpoint security grade'
                    , 'hacker chatter grade', 'ip reputation grade',
                    'leaked information grade', 'network security grade', 'patching cadence grade'
                    , 'social engineering grade']).apply(colour_score, axis=0, subset=['summary score', 'application security score',
                     'cubit score', 'dns health score', 'endpoint security score'
                    , 'hacker chatter score', 'ip reputation score',
                    'leaked information score', 'network security score', 'patching cadence score'
                    , 'social engineering score']).set_properties(**{"border": "1px solid black"}).set_properties(**{'text-align': 'center'})

    scorecard_colour.to_excel(output_filepath)

    return