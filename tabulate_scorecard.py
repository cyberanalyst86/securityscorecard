import os
import requests
import sys
import pandas as pd
import json
from create_dataframe import *
from create_dataframe_visualisation import *
from output_to_excel import *
from output_to_excel_visualisation import *


def tabulate_scorecard(headers, org_domain, api_url):

    # Declaration

    dataframe_list = [] #empty dataframe list
    dataframe_list_visualisation = []

    # Iterate Dataframe Creation

    for i in range(len(org_domain)):

        print("Generating Dataframe #[" + str(i) + "]")

        # API call (URL) - Get Organization Summary Score

        url_summary = api_url + '/companies/' + org_domain[i]

        # API call (URL) - Get Organization Factor Score
        url_factor = url = api_url + '/companies/' + org_domain[i] + '/factors'

        #create dataframe

        scorecard_dataframe = create_dataframe(url_summary, url_factor, org_domain[i], headers)

        dataframe_list.append(scorecard_dataframe)

        scorecard_dataframe_visualisation = create_dataframe_visualisation(url_summary, url_factor, org_domain[i], headers)

        dataframe_list_visualisation.append(scorecard_dataframe_visualisation)

    # Combine Dataframe

    scorecard = pd.concat(dataframe_list)

    scorecard_visualisation = pd.concat(dataframe_list_visualisation)

    scorecard.index.name = 'organisation'


    #output excel

    output_to_excel(scorecard)

    output_to_excel_visualisation(scorecard_visualisation)



    return