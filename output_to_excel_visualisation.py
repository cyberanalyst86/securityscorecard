import os
import requests
import sys
import time
import datetime
import pandas as pd

def output_to_excel_visualisation(scorecard):

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

    output_filepath = filepath + str(dt_string) + '_scorecard_visualisation.xlsx'

    print("output excel to " + str(output_filepath));

    scorecard.to_excel(output_filepath)

    return