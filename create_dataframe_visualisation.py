import pandas as pd
import os
import requests
import sys
import time
from datetime import datetime


def create_dataframe_visualisation(url_summary, url_factor, org, headers):
    response = requests.get(url_summary, headers=headers)

    date_stamp = datetime.today().strftime("%d/%m/%Y")

    summary_name = response.json()['name']
    summary_score = response.json()['score']

    # Get Company Factor Score

    response = requests.get(url_factor, headers=headers)

    factor_scores = response.json()['entries']

    # Convert Factor_Scores to Dataframe

    fsdf = pd.DataFrame(factor_scores)

    fsdf_drop = fsdf.drop(['grade_url', 'issue_summary', 'grade'], axis=1)

    fsdf_list = fsdf_drop.values.tolist()

    df = pd.DataFrame(fsdf_list)

    df_transposed = df.T

    new_header = df_transposed.iloc[0]  # grab the first row for the header
    df_transposed = df_transposed[1:]  # take the data less the header row
    df_transposed.columns = new_header

    df_transposed.insert(0, "summary_score", summary_score)

    df_transposed.insert(0, "organization", summary_name)

    df_transposed.insert(0, "date", date_stamp)

    df_transposed.insert(0, "domain", org)

    df_final = df_transposed.set_index('domain')

    return df_final