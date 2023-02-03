import pandas as pd
import os
import requests
import sys
import time
from datetime import datetime


def create_dataframe(url_summary, url_factor, org, headers):

    date_stamp = datetime.today().strftime("%d/%m/%Y")

    response = requests.get(url_summary, headers=headers)

    summary_name = response.json()['name']
    summary_score = response.json()['score']
    summary_grade = response.json()['grade']

    # Get Company Factor Score

    response = requests.get(url_factor, headers=headers)

    factor_scores = response.json()['entries']


    # Convert Factor_Scores to Dataframe

    fsdf = pd.DataFrame(factor_scores)

    fsdf_drop = fsdf.drop(['grade_url', 'issue_summary'], axis=1)

    fsdf_list = fsdf_drop.values.tolist()


    score = []
    grade = []

    for i in range(len(fsdf_list)):
        score.append(fsdf_list[i][1])
        grade.append(fsdf_list[i][2])

    score_grade = []

    for i in range(len(score)):
        score_grade.append(score[i])
        score_grade.append(grade[i])



    # assign data of lists.
    data = {'Org': ['application security score', 'application security grade',
                    'cubit score', 'cubit grade', 'dns health score', 'dns health grade', 'endpoint security score', 'endpoint security grade',
                    'hacker chatter score', 'hacker chatter grade', 'ip reputation score', 'ip reputation grade',
                    'leaked information score',
                    'leaked information grade',
                    'network security score', 'network security grade', 'patching cadence score', 'patching cadence grade',
                    'social engineering score', 'social engineering grade'],
           summary_name: score_grade}

    # Create DataFrame
    df = pd.DataFrame(data)

    df_transposed = df.T

    # Further Dataframe Processing

    new_header = df_transposed.iloc[0]  # grab the first row for the header
    df_transposed = df_transposed[1:]  # take the data less the header row
    df_transposed.columns = new_header

    # Add Columns to Dataframe

    df_transposed.insert(0, "summary grade", summary_grade)

    df_transposed.insert(0, "summary score", summary_score)

    #df_transposed.insert(0, "organization", summary_name)

    df_transposed.insert(0, "date", date_stamp)

    df_transposed.insert(0, "domain", org)

    """
    #original_header = [ 'summary_score', 'summary_score', 'application_security',
                       'application_security',
                       'cubit_score', 'cubit_score', 'dns_health', 'dns_health', 'endpoint_security',
                       'endpoint_security',
                       'hacker_chatter', 'hacker_chatter', 'ip_reputation', 'ip_reputation', 'leaked_information',
                       'leaked_information',
                       'network_security', 'network_security', 'patching_cadence', 'patching_cadence',
                       'social_engineering', 'social_engineering']

    #header = [original_header,
              ['Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade',
               'Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade', 'Score', 'Grade', 'Score',
               'Grade']]
    """
    #df_transposed.columns = header
    

    return df_transposed
    

